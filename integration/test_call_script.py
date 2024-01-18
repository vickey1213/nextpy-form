# This file has been modified by the Nextpy Team in 2023 using AI tools and automation scripts. 
# We have rigorously tested these modifications to ensure reliability and performance. Based on successful test results, we are confident in the quality and stability of these changes.

"""Integration tests for client side storage."""
from __future__ import annotations

from typing import Generator

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from nextpy.build.testing import AppHarness


def CallScript():
    """A test app for browser javascript integration."""
    import nextpy as xt

    inline_scripts = """
    let inline_counter = 0
    function inline1() {
        inline_counter += 1
        return "inline1"
    }
    function inline2() {
        inline_counter += 1
        console.log("inline2")
    }
    function inline3() {
        inline_counter += 1
        return {inline3: 42, a: [1, 2, 3], s: 'js', o: {a: 1, b: 2}}
    }
    async function inline4() {
        inline_counter += 1
        return "async inline4"
    }
    """

    external_scripts = inline_scripts.replace("inline", "external")

    class CallScriptState(xt.State):
        results: list[str | dict | list | None] = []
        inline_counter: int = 0
        external_counter: int = 0

        def call_script_callback(self, result):
            self.results.append(result)

        def call_script_callback_other_arg(self, result, other_arg):
            self.results.append([other_arg, result])

        def call_scripts_inline_yield(self):
            yield xt.call_script("inline1()")
            yield xt.call_script("inline2()")
            yield xt.call_script("inline3()")
            yield xt.call_script("inline4()")

        def call_script_inline_return(self):
            return xt.call_script("inline2()")

        def call_scripts_inline_yield_callback(self):
            yield xt.call_script(
                "inline1()", callback=CallScriptState.call_script_callback
            )
            yield xt.call_script(
                "inline2()", callback=CallScriptState.call_script_callback
            )
            yield xt.call_script(
                "inline3()", callback=CallScriptState.call_script_callback
            )
            yield xt.call_script(
                "inline4()", callback=CallScriptState.call_script_callback
            )

        def call_script_inline_return_callback(self):
            return xt.call_script(
                "inline3()", callback=CallScriptState.call_script_callback
            )

        def call_script_inline_return_lambda(self):
            return xt.call_script(
                "inline2()",
                callback=lambda result: CallScriptState.call_script_callback_other_arg(  # type: ignore
                    result, "lambda"
                ),
            )

        def get_inline_counter(self):
            return xt.call_script(
                "inline_counter",
                callback=CallScriptState.set_inline_counter,  # type: ignore
            )

        def call_scripts_external_yield(self):
            yield xt.call_script("external1()")
            yield xt.call_script("external2()")
            yield xt.call_script("external3()")
            yield xt.call_script("external4()")

        def call_script_external_return(self):
            return xt.call_script("external2()")

        def call_scripts_external_yield_callback(self):
            yield xt.call_script(
                "external1()", callback=CallScriptState.call_script_callback
            )
            yield xt.call_script(
                "external2()", callback=CallScriptState.call_script_callback
            )
            yield xt.call_script(
                "external3()", callback=CallScriptState.call_script_callback
            )
            yield xt.call_script(
                "external4()", callback=CallScriptState.call_script_callback
            )

        def call_script_external_return_callback(self):
            return xt.call_script(
                "external3()", callback=CallScriptState.call_script_callback
            )

        def call_script_external_return_lambda(self):
            return xt.call_script(
                "external2()",
                callback=lambda result: CallScriptState.call_script_callback_other_arg(  # type: ignore
                    result, "lambda"
                ),
            )

        def get_external_counter(self):
            return xt.call_script(
                "external_counter",
                callback=CallScriptState.set_external_counter,  # type: ignore
            )

        def reset_(self):
            yield xt.call_script("inline_counter = 0; external_counter = 0")
            self.reset()

    app = xt.App(state=xt.State)
    with open("assets/external.js", "w") as f:
        f.write(external_scripts)

    @app.add_page
    def index():
        return xt.vstack(
            xt.input(
                value=CallScriptState.router.session.client_token,
                is_read_only=True,
                id="token",
            ),
            xt.input(
                value=CallScriptState.inline_counter.to(str),  # type: ignore
                id="inline_counter",
                is_read_only=True,
            ),
            xt.input(
                value=CallScriptState.external_counter.to(str),  # type: ignore
                id="external_counter",
                is_read_only=True,
            ),
            xt.text_area(
                value=CallScriptState.results.to_string(),  # type: ignore
                id="results",
                is_read_only=True,
            ),
            xt.script(inline_scripts),
            xt.script(src="/external.js"),
            xt.button(
                "call_scripts_inline_yield",
                on_click=CallScriptState.call_scripts_inline_yield,
                id="inline_yield",
            ),
            xt.button(
                "call_script_inline_return",
                on_click=CallScriptState.call_script_inline_return,
                id="inline_return",
            ),
            xt.button(
                "call_scripts_inline_yield_callback",
                on_click=CallScriptState.call_scripts_inline_yield_callback,
                id="inline_yield_callback",
            ),
            xt.button(
                "call_script_inline_return_callback",
                on_click=CallScriptState.call_script_inline_return_callback,
                id="inline_return_callback",
            ),
            xt.button(
                "call_script_inline_return_lambda",
                on_click=CallScriptState.call_script_inline_return_lambda,
                id="inline_return_lambda",
            ),
            xt.button(
                "call_scripts_external_yield",
                on_click=CallScriptState.call_scripts_external_yield,
                id="external_yield",
            ),
            xt.button(
                "call_script_external_return",
                on_click=CallScriptState.call_script_external_return,
                id="external_return",
            ),
            xt.button(
                "call_scripts_external_yield_callback",
                on_click=CallScriptState.call_scripts_external_yield_callback,
                id="external_yield_callback",
            ),
            xt.button(
                "call_script_external_return_callback",
                on_click=CallScriptState.call_script_external_return_callback,
                id="external_return_callback",
            ),
            xt.button(
                "call_script_external_return_lambda",
                on_click=CallScriptState.call_script_external_return_lambda,
                id="external_return_lambda",
            ),
            xt.button(
                "Update Inline Counter",
                on_click=CallScriptState.get_inline_counter,
                id="update_inline_counter",
            ),
            xt.button(
                "Update External Counter",
                on_click=CallScriptState.get_external_counter,
                id="update_external_counter",
            ),
            xt.button("Reset", id="reset", on_click=CallScriptState.reset_),
        )


@pytest.fixture(scope="session")
def call_script(tmp_path_factory) -> Generator[AppHarness, None, None]:
    """Start CallScript app at tmp_path via AppHarness.

    Args:
        tmp_path_factory: pytest tmp_path_factory fixture

    Yields:
        running AppHarness instance
    """
    with AppHarness.create(
        root=tmp_path_factory.mktemp("call_script"),
        app_source=CallScript,  # type: ignore
    ) as harness:
        yield harness


@pytest.fixture
def driver(call_script: AppHarness) -> Generator[WebDriver, None, None]:
    """Get an instance of the browser open to the call_script app.

    Args:
        call_script: harness for CallScript app

    Yields:
        WebDriver instance.
    """
    assert call_script.app_instance is not None, "app is not running"
    driver = call_script.frontend()
    try:
        yield driver
    finally:
        driver.quit()


def assert_token(call_script: AppHarness, driver: WebDriver) -> str:
    """Get the token associated with backend state.

    Args:
        call_script: harness for CallScript app.
        driver: WebDriver instance.

    Returns:
        The token visible in the driver browser.
    """
    assert call_script.app_instance is not None
    token_input = driver.find_element(By.ID, "token")
    assert token_input

    # wait for the backend connection to send the token
    token = call_script.poll_for_value(token_input)
    assert token is not None

    return token


@pytest.mark.parametrize("script", ["inline", "external"])
def test_call_script(
    call_script: AppHarness,
    driver: WebDriver,
    script: str,
):
    """Test calling javascript functions from python.

    Args:
        call_script: harness for CallScript app.
        driver: WebDriver instance.
        script: The type of script to test.
    """
    assert_token(call_script, driver)
    reset_button = driver.find_element(By.ID, "reset")
    update_counter_button = driver.find_element(By.ID, f"update_{script}_counter")
    counter = driver.find_element(By.ID, f"{script}_counter")
    results = driver.find_element(By.ID, "results")
    yield_button = driver.find_element(By.ID, f"{script}_yield")
    return_button = driver.find_element(By.ID, f"{script}_return")
    yield_callback_button = driver.find_element(By.ID, f"{script}_yield_callback")
    return_callback_button = driver.find_element(By.ID, f"{script}_return_callback")
    return_lambda_button = driver.find_element(By.ID, f"{script}_return_lambda")

    yield_button.click()
    update_counter_button.click()
    assert call_script.poll_for_value(counter, exp_not_equal="0") == "4"
    reset_button.click()
    assert call_script.poll_for_value(counter, exp_not_equal="3") == "0"
    return_button.click()
    update_counter_button.click()
    assert call_script.poll_for_value(counter, exp_not_equal="0") == "1"
    reset_button.click()
    assert call_script.poll_for_value(counter, exp_not_equal="1") == "0"

    yield_callback_button.click()
    update_counter_button.click()
    assert call_script.poll_for_value(counter, exp_not_equal="0") == "4"
    assert call_script.poll_for_value(
        results, exp_not_equal="[]"
    ) == '["%s1",null,{"%s3":42,"a":[1,2,3],"s":"js","o":{"a":1,"b":2}},"async %s4"]' % (
        script,
        script,
        script,
    )
    reset_button.click()
    assert call_script.poll_for_value(counter, exp_not_equal="3") == "0"

    return_callback_button.click()
    update_counter_button.click()
    assert call_script.poll_for_value(counter, exp_not_equal="0") == "1"
    assert (
        call_script.poll_for_value(results, exp_not_equal="[]")
        == '[{"%s3":42,"a":[1,2,3],"s":"js","o":{"a":1,"b":2}}]' % script
    )
    reset_button.click()
    assert call_script.poll_for_value(counter, exp_not_equal="1") == "0"

    return_lambda_button.click()
    update_counter_button.click()
    assert call_script.poll_for_value(counter, exp_not_equal="0") == "1"
    assert (
        call_script.poll_for_value(results, exp_not_equal="[]") == '[["lambda",null]]'
    )
    reset_button.click()
    assert call_script.poll_for_value(counter, exp_not_equal="1") == "0"