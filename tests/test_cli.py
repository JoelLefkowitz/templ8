# coding=utf-8
"""Cli feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('tests/cli.feature', 'Invalid command handling')
def test_invalid_command_handling():
    """Invalid command handling."""


@when('I call <call>')
def i_call_call():
    """I call <call>."""
    raise NotImplementedError


@then('An InvalidCommand Exception is raised')
def an_invalidcommand_exception_is_raised():
    """An InvalidCommand Exception is raised."""
    raise NotImplementedError


@then('Command issues are reported')
def command_issues_are_reported():
    """Command issues are reported."""
    raise NotImplementedError


@then('Correct usage examples are shown')
def correct_usage_examples_are_shown():
    """Correct usage examples are shown."""
    raise NotImplementedError

