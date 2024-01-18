# This file has been modified by the Nextpy Team in 2023 using AI tools and automation scripts. 
# We have rigorously tested these modifications to ensure reliability and performance. Based on successful test results, we are confident in the quality and stability of these changes.

from __future__ import annotations

from typing import Any

import pytest

import nextpy as xt
from nextpy.backend.vars import Var
from nextpy.frontend import style

test_style = [
    ({"a": 1}, {"a": 1}),
    ({"a": Var.create("abc")}, {"a": "abc"}),
    ({"test_case": 1}, {"testCase": 1}),
    ({"test_case": {"a": 1}}, {"testCase": {"a": 1}}),
    ({":test_case": {"a": 1}}, {":testCase": {"a": 1}}),
    ({"::test_case": {"a": 1}}, {"::testCase": {"a": 1}}),
    (
        {"::-webkit-scrollbar": {"display": "none"}},
        {"::-webkit-scrollbar": {"display": "none"}},
    ),
]


@pytest.mark.parametrize(
    "style_dict,expected",
    test_style,
)
def test_convert(style_dict, expected):
    """Test Format a style dictionary.

    Args:
        style_dict: The style to check.
        expected: The expected formatted style.
    """
    converted_dict, _var_data = style.convert(style_dict)
    assert converted_dict == expected


@pytest.mark.parametrize(
    "style_dict,expected",
    test_style,
)
def test_create_style(style_dict, expected):
    """Test style dictionary.

    Args:
        style_dict: The style to check.
        expected: The expected formatted style.
    """
    assert style.Style(style_dict) == expected


def compare_dict_of_var(d1: dict[str, Any], d2: dict[str, Any]):
    """Compare two dictionaries of Var objects.

    Args:
        d1: The first dictionary.
        d2: The second dictionary.
    """
    assert len(d1) == len(d2)
    for key, value in d1.items():
        assert key in d2
        if isinstance(value, dict):
            compare_dict_of_var(value, d2[key])
        elif isinstance(value, Var):
            assert value.equals(d2[key])
        else:
            assert value == d2[key]


@pytest.mark.parametrize(
    ("kwargs", "style_dict", "expected_get_style"),
    [
        ({}, {}, {"css": None}),
        ({"color": "hotpink"}, {}, {"css": Var.create({"color": "hotpink"})}),
        ({}, {"color": "red"}, {"css": Var.create({"color": "red"})}),
        (
            {"color": "hotpink"},
            {"color": "red"},
            {"css": Var.create({"color": "hotpink"})},
        ),
        (
            {"_hover": {"color": "hotpink"}},
            {},
            {"css": Var.create({"&:hover": {"color": "hotpink"}})},
        ),
        (
            {},
            {"_hover": {"color": "red"}},
            {"css": Var.create({"&:hover": {"color": "red"}})},
        ),
        (
            {},
            {":hover": {"color": "red"}},
            {"css": Var.create({"&:hover": {"color": "red"}})},
        ),
        (
            {},
            {"::-webkit-scrollbar": {"display": "none"}},
            {"css": Var.create({"&::-webkit-scrollbar": {"display": "none"}})},
        ),
        (
            {},
            {"::-moz-progress-bar": {"background_color": "red"}},
            {"css": Var.create({"&::-moz-progress-bar": {"backgroundColor": "red"}})},
        ),
        (
            {"color": ["#111", "#222", "#333", "#444", "#555"]},
            {},
            {
                "css": Var.create(
                    {
                        "@media screen and (min-width: 0)": {"color": "#111"},
                        "@media screen and (min-width: 30em)": {"color": "#222"},
                        "@media screen and (min-width: 48em)": {"color": "#333"},
                        "@media screen and (min-width: 62em)": {"color": "#444"},
                        "@media screen and (min-width: 80em)": {"color": "#555"},
                    }
                )
            },
        ),
        (
            {
                "color": ["#111", "#222", "#333", "#444", "#555"],
                "background_color": "#FFF",
            },
            {},
            {
                "css": Var.create(
                    {
                        "@media screen and (min-width: 0)": {"color": "#111"},
                        "@media screen and (min-width: 30em)": {"color": "#222"},
                        "@media screen and (min-width: 48em)": {"color": "#333"},
                        "@media screen and (min-width: 62em)": {"color": "#444"},
                        "@media screen and (min-width: 80em)": {"color": "#555"},
                        "backgroundColor": "#FFF",
                    }
                )
            },
        ),
        (
            {
                "color": ["#111", "#222", "#333", "#444", "#555"],
                "background_color": ["#FFF", "#EEE", "#DDD", "#CCC", "#BBB"],
            },
            {},
            {
                "css": Var.create(
                    {
                        "@media screen and (min-width: 0)": {
                            "color": "#111",
                            "backgroundColor": "#FFF",
                        },
                        "@media screen and (min-width: 30em)": {
                            "color": "#222",
                            "backgroundColor": "#EEE",
                        },
                        "@media screen and (min-width: 48em)": {
                            "color": "#333",
                            "backgroundColor": "#DDD",
                        },
                        "@media screen and (min-width: 62em)": {
                            "color": "#444",
                            "backgroundColor": "#CCC",
                        },
                        "@media screen and (min-width: 80em)": {
                            "color": "#555",
                            "backgroundColor": "#BBB",
                        },
                    }
                )
            },
        ),
        (
            {
                "_hover": [
                    {"color": "#111"},
                    {"color": "#222"},
                    {"color": "#333"},
                    {"color": "#444"},
                    {"color": "#555"},
                ]
            },
            {},
            {
                "css": Var.create(
                    {
                        "&:hover": {
                            "@media screen and (min-width: 0)": {"color": "#111"},
                            "@media screen and (min-width: 30em)": {"color": "#222"},
                            "@media screen and (min-width: 48em)": {"color": "#333"},
                            "@media screen and (min-width: 62em)": {"color": "#444"},
                            "@media screen and (min-width: 80em)": {"color": "#555"},
                        }
                    }
                )
            },
        ),
        (
            {"_hover": {"color": ["#111", "#222", "#333", "#444", "#555"]}},
            {},
            {
                "css": Var.create(
                    {
                        "&:hover": {
                            "@media screen and (min-width: 0)": {"color": "#111"},
                            "@media screen and (min-width: 30em)": {"color": "#222"},
                            "@media screen and (min-width: 48em)": {"color": "#333"},
                            "@media screen and (min-width: 62em)": {"color": "#444"},
                            "@media screen and (min-width: 80em)": {"color": "#555"},
                        }
                    }
                )
            },
        ),
        (
            {
                "_hover": {
                    "color": ["#111", "#222", "#333", "#444", "#555"],
                    "background_color": ["#FFF", "#EEE", "#DDD", "#CCC", "#BBB"],
                }
            },
            {},
            {
                "css": Var.create(
                    {
                        "&:hover": {
                            "@media screen and (min-width: 0)": {
                                "color": "#111",
                                "backgroundColor": "#FFF",
                            },
                            "@media screen and (min-width: 30em)": {
                                "color": "#222",
                                "backgroundColor": "#EEE",
                            },
                            "@media screen and (min-width: 48em)": {
                                "color": "#333",
                                "backgroundColor": "#DDD",
                            },
                            "@media screen and (min-width: 62em)": {
                                "color": "#444",
                                "backgroundColor": "#CCC",
                            },
                            "@media screen and (min-width: 80em)": {
                                "color": "#555",
                                "backgroundColor": "#BBB",
                            },
                        }
                    }
                )
            },
        ),
        (
            {
                "_hover": {
                    "color": ["#111", "#222", "#333", "#444", "#555"],
                    "background_color": "#FFF",
                }
            },
            {},
            {
                "css": Var.create(
                    {
                        "&:hover": {
                            "@media screen and (min-width: 0)": {"color": "#111"},
                            "@media screen and (min-width: 30em)": {"color": "#222"},
                            "@media screen and (min-width: 48em)": {"color": "#333"},
                            "@media screen and (min-width: 62em)": {"color": "#444"},
                            "@media screen and (min-width: 80em)": {"color": "#555"},
                            "backgroundColor": "#FFF",
                        }
                    }
                )
            },
        ),
    ],
)
def test_style_via_component(
    kwargs: dict[str, Any],
    style_dict: dict[str, Any],
    expected_get_style: dict[str, Any],
):
    """Pass kwargs and style_dict to a component and assert the final, combined style dict.

    Args:
        kwargs: The kwargs to pass to the component.
        style_dict: The style_dict to pass to the component.
        expected_get_style: The expected style dict.
    """
    comp = xt.el.div(style=style_dict, **kwargs)  # type: ignore
    compare_dict_of_var(comp._get_style(), expected_get_style)


class StyleState(xt.State):
    """Style vars in a substate."""

    color: str = "hotpink"
    color2: str = "red"


@pytest.mark.parametrize(
    ("kwargs", "expected_get_style"),
    [
        (
            {"color": StyleState.color},
            {"css": Var.create({"color": StyleState.color})},
        ),
        (
            {"color": f"dark{StyleState.color}"},
            {"css": Var.create_safe(f'{{"color": `dark{StyleState.color}`}}').to(dict)},
        ),
        (
            {"color": StyleState.color, "_hover": {"color": StyleState.color2}},
            {
                "css": Var.create(
                    {
                        "color": StyleState.color,
                        "&:hover": {"color": StyleState.color2},
                    }
                )
            },
        ),
        (
            {"color": [StyleState.color, "gray", StyleState.color2, "yellow", "blue"]},
            {
                "css": Var.create(
                    {
                        "@media screen and (min-width: 0)": {"color": StyleState.color},
                        "@media screen and (min-width: 30em)": {"color": "gray"},
                        "@media screen and (min-width: 48em)": {
                            "color": StyleState.color2
                        },
                        "@media screen and (min-width: 62em)": {"color": "yellow"},
                        "@media screen and (min-width: 80em)": {"color": "blue"},
                    }
                )
            },
        ),
        (
            {
                "_hover": [
                    {"color": StyleState.color},
                    {"color": StyleState.color2},
                    {"color": "#333"},
                    {"color": "#444"},
                    {"color": "#555"},
                ]
            },
            {
                "css": Var.create(
                    {
                        "&:hover": {
                            "@media screen and (min-width: 0)": {
                                "color": StyleState.color
                            },
                            "@media screen and (min-width: 30em)": {
                                "color": StyleState.color2
                            },
                            "@media screen and (min-width: 48em)": {"color": "#333"},
                            "@media screen and (min-width: 62em)": {"color": "#444"},
                            "@media screen and (min-width: 80em)": {"color": "#555"},
                        }
                    }
                )
            },
        ),
        (
            {
                "_hover": {
                    "color": [
                        StyleState.color,
                        StyleState.color2,
                        "#333",
                        "#444",
                        "#555",
                    ]
                }
            },
            {
                "css": Var.create(
                    {
                        "&:hover": {
                            "@media screen and (min-width: 0)": {
                                "color": StyleState.color
                            },
                            "@media screen and (min-width: 30em)": {
                                "color": StyleState.color2
                            },
                            "@media screen and (min-width: 48em)": {"color": "#333"},
                            "@media screen and (min-width: 62em)": {"color": "#444"},
                            "@media screen and (min-width: 80em)": {"color": "#555"},
                        }
                    }
                )
            },
        ),
    ],
)
def test_style_via_component_with_state(
    kwargs: dict[str, Any],
    expected_get_style: dict[str, Any],
):
    """Pass kwargs to a component with state vars and assert the final, combined style dict.

    Args:
        kwargs: The kwargs to pass to the component.
        expected_get_style: The expected style dict.
    """
    comp = xt.el.div(**kwargs)

    assert comp.style._var_data == expected_get_style["css"]._var_data
    # Remove the _var_data from the expected style, since the emotion-formatted
    # style dict won't actually have it.
    expected_get_style["css"]._var_data = None

    # Assert that style values are equal.
    compare_dict_of_var(comp._get_style(), expected_get_style)
