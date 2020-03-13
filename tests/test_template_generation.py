# coding=utf-8
"""Template generation feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('tests/template_generation.feature', 'Alias handling')
def test_alias_handling():
    """Alias handling."""


@scenario('tests/template_generation.feature', 'Callback handling')
def test_callback_handling():
    """Callback handling."""


@scenario('tests/template_generation.feature', 'Folder renaming')
def test_folder_renaming():
    """Folder renaming."""


@scenario('tests/template_generation.feature', 'Invalid configuration file path')
def test_invalid_configuration_file_path():
    """Invalid configuration file path."""


@scenario('tests/template_generation.feature', 'Invalid output directory')
def test_invalid_output_directory():
    """Invalid output directory."""


@scenario('tests/template_generation.feature', 'Missing configuration')
def test_missing_configuration():
    """Missing configuration."""


@scenario('tests/template_generation.feature', 'Output files already exist')
def test_output_files_already_exist():
    """Output files already exist."""


@scenario('tests/template_generation.feature', 'Output resolver')
def test_output_resolver():
    """Output resolver."""


@scenario('tests/template_generation.feature', 'Spec handling')
def test_spec_handling():
    """Spec handling."""


@given('A spec is set to True in the configuration file')
def a_spec_is_set_to_true_in_the_configuration_file():
    """A spec is set to True in the configuration file."""
    raise NotImplementedError


@given('Context is missing without defualt values')
def context_is_missing_without_defualt_values():
    """Context is missing without defualt values."""
    raise NotImplementedError


@given('Files already exists in the output paths')
def files_already_exists_in_the_output_paths():
    """Files already exists in the output paths."""
    raise NotImplementedError


@given('The spec declares a callback')
def the_spec_declares_a_callback():
    """The spec declares a callback."""
    raise NotImplementedError


@given('The spec declares a folder to rename')
def the_spec_declares_a_folder_to_rename():
    """The spec declares a folder to rename."""
    raise NotImplementedError


@given('The spec declares an alias')
def the_spec_declares_an_alias():
    """The spec declares an alias."""
    raise NotImplementedError


@when('I call "templ8 <config-file> <output-dir>"')
def i_call_templ8_configfile_outputdir():
    """I call "templ8 <config-file> <output-dir>"."""
    raise NotImplementedError


@when('I call "templ8 config-file output-dir"')
def i_call_templ8_configfile_outputdir():
    """I call "templ8 config-file output-dir"."""
    raise NotImplementedError


@when('I give an invalid configuration file path')
def i_give_an_invalid_configuration_file_path():
    """I give an invalid configuration file path."""
    raise NotImplementedError


@when('I give an invalid output directory')
def i_give_an_invalid_output_directory():
    """I give an invalid output directory."""
    raise NotImplementedError


@then('A ConfigPathInvalid Exception is raised')
def a_configpathinvalid_exception_is_raised():
    """A ConfigPathInvalid Exception is raised."""
    raise NotImplementedError


@then('A MissingConfig Exception is raised')
def a_missingconfig_exception_is_raised():
    """A MissingConfig Exception is raised."""
    raise NotImplementedError


@then('An OutputDirInvalid Exception is raised')
def an_outputdirinvalid_exception_is_raised():
    """An OutputDirInvalid Exception is raised."""
    raise NotImplementedError


@then('Clashing templates are not generated')
def clashing_templates_are_not_generated():
    """Clashing templates are not generated."""
    raise NotImplementedError


@then('Missing configuration names are reported')
def missing_configuration_names_are_reported():
    """Missing configuration names are reported."""
    raise NotImplementedError


@then('Templates are generated in the output directory')
def templates_are_generated_in_the_output_directory():
    """Templates are generated in the output directory."""
    raise NotImplementedError


@then('The alias is resolved and included in the resolver context')
def the_alias_is_resolved_and_included_in_the_resolver_context():
    """The alias is resolved and included in the resolver context."""
    raise NotImplementedError


@then('The callback is included in the resolver callbacks, resolving aliases')
def the_callback_is_included_in_the_resolver_callbacks_resolving_aliases():
    """The callback is included in the resolver callbacks, resolving aliases."""
    raise NotImplementedError


@then('The files generated are reported')
def the_files_generated_are_reported():
    """The files generated are reported."""
    raise NotImplementedError


@then('The files skipped are reported')
def the_files_skipped_are_reported():
    """The files skipped are reported."""
    raise NotImplementedError


@then('The folder to rename is included in the resolver renames, resolving aliases')
def the_folder_to_rename_is_included_in_the_resolver_renames_resolving_aliases():
    """The folder to rename is included in the resolver renames, resolving aliases."""
    raise NotImplementedError


@then('The resolver callbacks are called')
def the_resolver_callbacks_are_called():
    """The resolver callbacks are called."""
    raise NotImplementedError


@then('The resolver context is resolved')
def the_resolver_context_is_resolved():
    """The resolver context is resolved."""
    raise NotImplementedError


@then('The resolver renames are resolved')
def the_resolver_renames_are_resolved():
    """The resolver renames are resolved."""
    raise NotImplementedError


@then('The spec name is set to True in the resolver context')
def the_spec_name_is_set_to_true_in_the_resolver_context():
    """The spec name is set to True in the resolver context."""
    raise NotImplementedError


@then('The specs context are included in the resolver context')
def the_specs_context_are_included_in_the_resolver_context():
    """The specs context are included in the resolver context."""
    raise NotImplementedError

