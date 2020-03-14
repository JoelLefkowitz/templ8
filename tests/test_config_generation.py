# coding=utf-8
"""Configuration file generation feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario("tests/config_generation.feature", "Configuration file is generated")
def test_configuration_file_is_generated():
    """Configuration file is generated."""


@when('I call "templ8 generate"')
def i_call_templ8_generate():
    """I call "templ8 generate"."""
    raise NotImplementedError


@then("A configuration file is generated")
def a_configuration_file_is_generated():
    """A configuration file is generated."""
    raise NotImplementedError


@then("A sequence of interactive text questions are offered")
def a_sequence_of_interactive_text_questions_are_offered():
    """A sequence of interactive text questions are offered."""
    raise NotImplementedError
