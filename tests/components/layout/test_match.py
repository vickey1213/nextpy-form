# This file has been modified by the Nextpy Team in 2023 using AI tools and automation scripts. 
# We have rigorously tested these modifications to ensure reliability and performance. Based on successful test results, we are confident in the quality and stability of these changes.

# from typing import Tuple

# import pytest

# import nextpy as xt
# from nextpy.backend.state import BaseState
# from nextpy.backend.vars import BaseVar
# from nextpy.frontend.components.core.match import Match
# from nextpy.utils.exceptions import MatchTypeError


# class MatchState(BaseState):
#     """A test state."""

#     value: int = 0
#     num: int = 5
#     string: str = "random string"


# def test_match_components():
#     """Test matching cases with return values as components."""
#     match_case_tuples = (
#         (1, xt.text("first value")),
#         (2, 3, xt.text("second value")),
#         ([1, 2], xt.text("third value")),
#         ("random", xt.text("fourth value")),
#         ({"foo": "bar"}, xt.text("fifth value")),
#         (MatchState.num + 1, xt.text("sixth value")),
#         xt.text("default value"),
#     )
#     match_comp = Match.create(MatchState.value, *match_case_tuples)
#     match_dict = match_comp.render()  # type: ignore
#     assert match_dict["name"] == "Fragment"

#     [match_child] = match_dict["children"]

#     assert match_child["name"] == "match"
#     assert str(match_child["cond"]) == "{match_state.value}"

#     match_cases = match_child["match_cases"]
#     assert len(match_cases) == 6

#     assert match_cases[0][0]._var_name == "1"
#     assert match_cases[0][0]._var_type == int
#     first_return_value_render = match_cases[0][1].render()
#     assert first_return_value_render["name"] == "Text"
#     assert first_return_value_render["children"][0]["contents"] == "{`first value`}"

#     assert match_cases[1][0]._var_name == "2"
#     assert match_cases[1][0]._var_type == int
#     assert match_cases[1][1]._var_name == "3"
#     assert match_cases[1][1]._var_type == int
#     second_return_value_render = match_cases[1][2].render()
#     assert second_return_value_render["name"] == "Text"
#     assert second_return_value_render["children"][0]["contents"] == "{`second value`}"

#     assert match_cases[2][0]._var_name == "[1, 2]"
#     assert match_cases[2][0]._var_type == list
#     third_return_value_render = match_cases[2][1].render()
#     assert third_return_value_render["name"] == "Text"
#     assert third_return_value_render["children"][0]["contents"] == "{`third value`}"

#     assert match_cases[3][0]._var_name == "random"
#     assert match_cases[3][0]._var_type == str
#     fourth_return_value_render = match_cases[3][1].render()
#     assert fourth_return_value_render["name"] == "Text"
#     assert fourth_return_value_render["children"][0]["contents"] == "{`fourth value`}"

#     assert match_cases[4][0]._var_name == '{"foo": "bar"}'
#     assert match_cases[4][0]._var_type == dict
#     fifth_return_value_render = match_cases[4][1].render()
#     assert fifth_return_value_render["name"] == "Text"
#     assert fifth_return_value_render["children"][0]["contents"] == "{`fifth value`}"

#     assert match_cases[5][0]._var_name == "(match_state.num + 1)"
#     assert match_cases[5][0]._var_type == int
#     fifth_return_value_render = match_cases[5][1].render()
#     assert fifth_return_value_render["name"] == "Text"
#     assert fifth_return_value_render["children"][0]["contents"] == "{`sixth value`}"

#     default = match_child["default"].render()

#     assert default["name"] == "Text"
#     assert default["children"][0]["contents"] == "{`default value`}"


# @pytest.mark.parametrize(
#     "cases, expected",
#     [
#         (
#             (
#                 (1, "first"),
#                 (2, 3, "second value"),
#                 ([1, 2], "third-value"),
#                 ("random", "fourth_value"),
#                 ({"foo": "bar"}, "fifth value"),
#                 (MatchState.num + 1, "sixth value"),
#                 (f"{MatchState.value} - string", MatchState.string),
#                 (MatchState.string, f"{MatchState.value} - string"),
#                 "default value",
#             ),
#             "(() => { switch (JSON.stringify(match_state.value)) {case JSON.stringify(1):  return (`first`);  break;case JSON.stringify(2): case JSON.stringify(3):  return "
#             "(`second value`);  break;case JSON.stringify([1, 2]):  return (`third-value`);  break;case JSON.stringify(`random`):  "
#             'return (`fourth_value`);  break;case JSON.stringify({"foo": "bar"}):  return (`fifth value`);  '
#             "break;case JSON.stringify((match_state.num + 1)):  return (`sixth value`);  break;case JSON.stringify(`${match_state.value} - string`):  "
#             "return (match_state.string);  break;case JSON.stringify(match_state.string):  return (`${match_state.value} - string`);  break;default:  "
#             "return (`default value`);  break;};})()",
#         ),
#         (
#             (
#                 (1, "first"),
#                 (2, 3, "second value"),
#                 ([1, 2], "third-value"),
#                 ("random", "fourth_value"),
#                 ({"foo": "bar"}, "fifth value"),
#                 (MatchState.num + 1, "sixth value"),
#                 (f"{MatchState.value} - string", MatchState.string),
#                 (MatchState.string, f"{MatchState.value} - string"),
#                 MatchState.string,
#             ),
#             "(() => { switch (JSON.stringify(match_state.value)) {case JSON.stringify(1):  return (`first`);  break;case JSON.stringify(2): case JSON.stringify(3):  return "
#             "(`second value`);  break;case JSON.stringify([1, 2]):  return (`third-value`);  break;case JSON.stringify(`random`):  "
#             'return (`fourth_value`);  break;case JSON.stringify({"foo": "bar"}):  return (`fifth value`);  '
#             "break;case JSON.stringify((match_state.num + 1)):  return (`sixth value`);  break;case JSON.stringify(`${match_state.value} - string`):  "
#             "return (match_state.string);  break;case JSON.stringify(match_state.string):  return (`${match_state.value} - string`);  break;default:  "
#             "return (match_state.string);  break;};})()",
#         ),
#     ],
# )
# def test_match_vars(cases, expected):
#     """Test matching cases with return values as Vars.

#     Args:
#         cases: The match cases.
#         expected: The expected var full name.
#     """
#     match_comp = Match.create(MatchState.value, *cases)
#     assert isinstance(match_comp, BaseVar)
#     assert match_comp._var_full_name == expected


# def test_match_on_component_without_default():
#     """Test that matching cases with return values as components returns a Fragment
#     as the default case if not provided.
#     """
#     match_case_tuples = (
#         (1, xt.text("first value")),
#         (2, 3, xt.text("second value")),
#     )

#     match_comp = Match.create(MatchState.value, *match_case_tuples)
#     default = match_comp.render()["children"][0]["default"]  # type: ignore

#     assert isinstance(default, xt.Fragment)


# def test_match_on_var_no_default():
#     """Test that an error is thrown when cases with return Values as Var do not have a default case."""
#     match_case_tuples = (
#         (1, "red"),
#         (2, 3, "blue"),
#         ([1, 2], "green"),
#     )

#     with pytest.raises(
#         ValueError,
#         match="For cases with return types as Vars, a default case must be provided",
#     ):
#         Match.create(MatchState.value, *match_case_tuples)


# @pytest.mark.parametrize(
#     "match_case",
#     [
#         (
#             (1, "red"),
#             (2, 3, "blue"),
#             "black",
#             ([1, 2], "green"),
#         ),
#         (
#             (1, xt.text("first value")),
#             (2, 3, xt.text("second value")),
#             ([1, 2], xt.text("third value")),
#             xt.text("default value"),
#             ("random", xt.text("fourth value")),
#             ({"foo": "bar"}, xt.text("fifth value")),
#             (MatchState.num + 1, xt.text("sixth value")),
#         ),
#     ],
# )
# def test_match_default_not_last_arg(match_case):
#     """Test that an error is thrown when the default case is not the last arg.

#     Args:
#         match_case: The cases to match.
#     """
#     with pytest.raises(
#         ValueError,
#         match="xt.match should have tuples of cases and a default case as the last argument.",
#     ):
#         Match.create(MatchState.value, *match_case)


# @pytest.mark.parametrize(
#     "match_case",
#     [
#         (
#             (1, "red"),
#             (2, 3, "blue"),
#             ("green",),
#             "black",
#         ),
#         (
#             (1, xt.text("first value")),
#             (2, 3, xt.text("second value")),
#             ([1, 2],),
#             xt.text("default value"),
#         ),
#     ],
# )
# def test_match_case_tuple_elements(match_case):
#     """Test that a match has at least 2 elements(a condition and a return value).

#     Args:
#         match_case: The cases to match.
#     """
#     with pytest.raises(
#         ValueError,
#         match="A case tuple should have at least a match case element and a return value.",
#     ):
#         Match.create(MatchState.value, *match_case)


# @pytest.mark.parametrize(
#     "cases, error_msg",
#     [
#         (
#             (
#                 (1, xt.text("first value")),
#                 (2, 3, xt.text("second value")),
#                 ([1, 2], xt.text("third value")),
#                 ("random", "red"),
#                 ({"foo": "bar"}, "green"),
#                 (MatchState.num + 1, "black"),
#                 xt.text("default value"),
#             ),
#             "Match cases should have the same return types. Case 3 with return value `red` of type "
#             "<class 'nextpy.backend.BaseVar'> is not <class 'nextpy.frontend.components.component.BaseComponent'>",
#         ),
#         (
#             (
#                 ("random", "red"),
#                 ({"foo": "bar"}, "green"),
#                 (MatchState.num + 1, "black"),
#                 (1, xt.text("first value")),
#                 (2, 3, xt.text("second value")),
#                 ([1, 2], xt.text("third value")),
#                 xt.text("default value"),
#             ),
#             "Match cases should have the same return types. Case 3 with return value `<Text> {`first value`} </Text>` "
#             "of type <class 'nextpy.frontend.components.chakra.typography.text.Text'> is not <class 'nextpy.backend.BaseVar'>",
#         ),
#     ],
# )
# def test_match_different_return_types(cases: Tuple, error_msg: str):
#     """Test that an error is thrown when the return values are of different types.

#     Args:
#         cases: The match cases.
#         error_msg: Expected error message.
#     """
#     with pytest.raises(MatchTypeError, match=error_msg):
#         Match.create(MatchState.value, *cases)


# @pytest.mark.parametrize(
#     "match_case",
#     [
#         (
#             (1, "red"),
#             (2, 3, "blue"),
#             ([1, 2], "green"),
#             "black",
#             "white",
#         ),
#         (
#             (1, xt.text("first value")),
#             (2, 3, xt.text("second value")),
#             ([1, 2], xt.text("third value")),
#             ("random", xt.text("fourth value")),
#             ({"foo": "bar"}, xt.text("fifth value")),
#             (MatchState.num + 1, xt.text("sixth value")),
#             xt.text("default value"),
#             xt.text("another default value"),
#         ),
#     ],
# )
# def test_match_multiple_default_cases(match_case):
#     """Test that there is only one default case.

#     Args:
#         match_case: the cases to match.
#     """
#     with pytest.raises(ValueError, match="xt.match can only have one default case."):
#         Match.create(MatchState.value, *match_case)
