# coding=utf-8
"""Cli feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('template_generation.feature', 'Alias handling')
def test_alias_handling():
    """Alias handling."""


@scenario('template_generation.feature', 'Callback handling')
def test_callback_handling():
    """Callback handling."""


@scenario('config_generation.feature', 'Configuration file is generated')
def test_configuration_file_is_generated():
    """Configuration file is generated."""


@scenario('template_generation_options.feature', 'Dont generate files for a dry run')
def test_dont_generate_files_for_a_dry_run():
    """Dont generate files for a dry run."""


@scenario('template_generation_options.feature', 'Dont run callbacks when deactivated')
def test_dont_run_callbacks_when_deactivated():
    """Dont run callbacks when deactivated."""


@scenario('template_generation.feature', 'Folder renaming')
def test_folder_renaming():
    """Folder renaming."""


@scenario('template_generation_options.feature', 'Generate specific files only')
def test_generate_specific_files_only():
    """Generate specific files only."""


@scenario('cli.feature', 'Invalid command handling')
def test_invalid_command_handling():
    """Invalid command handling."""


@scenario('template_generation.feature', 'Invalid configuration file path')
def test_invalid_configuration_file_path():
    """Invalid configuration file path."""


@scenario('template_generation.feature', 'Invalid output directory')
def test_invalid_output_directory():
    """Invalid output directory."""


@scenario('template_generation.feature', 'Missing configuration')
def test_missing_configuration():
    """Missing configuration."""


@scenario('template_generation.feature', 'Output files already exist')
def test_output_files_already_exist():
    """Output files already exist."""


@scenario('template_generation.feature', 'Output resolver')
def test_output_resolver():
    """Output resolver."""


@scenario('template_generation_options.feature', 'Overwrite files')
def test_overwrite_files():
    """Overwrite files."""


@scenario('template_generation_options.feature', 'Skip callbacks when files skipped')
def test_skip_callbacks_when_files_skipped():
    """Skip callbacks when files skipped."""


@scenario('template_generation.feature', 'Spec handling')
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


@given('Filenames are specified')
def filenames_are_specified():
    """Filenames are specified."""
    raise NotImplementedError


@given('Files already exists in the output paths')
def files_already_exists_in_the_output_paths():
    """Files already exists in the output paths."""
    raise NotImplementedError


@given('Not all of a specs files are specified')
def not_all_of_a_specs_files_are_specified():
    """Not all of a specs files are specified."""
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


@when('I call "templ8 config-file output-dir --dry-run"')
def i_call_templ8_configfile_outputdir_dryrun():
    """I call "templ8 config-file output-dir --dry-run"."""
    raise NotImplementedError


@when('I call "templ8 config-file output-dir --no-callbacks"')
def i_call_templ8_configfile_outputdir_nocallbacks():
    """I call "templ8 config-file output-dir --no-callbacks"."""
    raise NotImplementedError


@when('I call "templ8 config-file output-dir --overwrite"')
def i_call_templ8_configfile_outputdir_overwrite():
    """I call "templ8 config-file output-dir --overwrite"."""
    raise NotImplementedError


@when('I call "templ8 config-file output-dir"')
def i_call_templ8_configfile_outputdir():
    """I call "templ8 config-file output-dir"."""
    raise NotImplementedError


@when('I call "templ8 generate"')
def i_call_templ8_generate():
    """I call "templ8 generate"."""
    raise NotImplementedError


@when('I call <call>')
def i_call_call():
    """I call <call>."""
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


@then('A configuration file is generated')
def a_configuration_file_is_generated():
    """A configuration file is generated."""
    raise NotImplementedError


@then('A sequence of interactive text questions are offered')
def a_sequence_of_interactive_text_questions_are_offered():
    """A sequence of interactive text questions are offered."""
    raise NotImplementedError


@then('All files are skipped')
def all_files_are_skipped():
    """All files are skipped."""
    raise NotImplementedError


@then('An InvalidCommand Exception is raised')
def an_invalidcommand_exception_is_raised():
    """An InvalidCommand Exception is raised."""
    raise NotImplementedError


@then('An OutputDirInvalid Exception is raised')
def an_outputdirinvalid_exception_is_raised():
    """An OutputDirInvalid Exception is raised."""
    raise NotImplementedError


@then('Clashing files are overwritten')
def clashing_files_are_overwritten():
    """Clashing files are overwritten."""
    raise NotImplementedError


@then('Clashing templates are not generated')
def clashing_templates_are_not_generated():
    """Clashing templates are not generated."""
    raise NotImplementedError


@then('Command issues are reported')
def command_issues_are_reported():
    """Command issues are reported."""
    raise NotImplementedError


@then('Correct usage examples are shown')
def correct_usage_examples_are_shown():
    """Correct usage examples are shown."""
    raise NotImplementedError


@then('Missing configuration names are reported')
def missing_configuration_names_are_reported():
    """Missing configuration names are reported."""
    raise NotImplementedError


@then('Only matching templates are generated in the output directory')
def only_matching_templates_are_generated_in_the_output_directory():
    """Only matching templates are generated in the output directory."""
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


@then('The callbacks that would have been called are reported')
def the_callbacks_that_would_have_been_called_are_reported():
    """The callbacks that would have been called are reported."""
    raise NotImplementedError


@then('The files generated are reported')
def the_files_generated_are_reported():
    """The files generated are reported."""
    raise NotImplementedError


@then('The files overwritten are reported')
def the_files_overwritten_are_reported():
    """The files overwritten are reported."""
    raise NotImplementedError


@then('The files skipped are reported')
def the_files_skipped_are_reported():
    """The files skipped are reported."""
    raise NotImplementedError


@then('The files that would have been generated are reported')
def the_files_that_would_have_been_generated_are_reported():
    """The files that would have been generated are reported."""
    raise NotImplementedError


@then('The files that would not have been generated are reported')
def the_files_that_would_not_have_been_generated_are_reported():
    """The files that would not have been generated are reported."""
    raise NotImplementedError


@then('The folder to rename is included in the resolver renames, resolving aliases')
def the_folder_to_rename_is_included_in_the_resolver_renames_resolving_aliases():
    """The folder to rename is included in the resolver renames, resolving aliases."""
    raise NotImplementedError


@then('The resolver callbacks are called')
def the_resolver_callbacks_are_called():
    """The resolver callbacks are called."""
    raise NotImplementedError


@then('The resolver callbacks are not called')
def the_resolver_callbacks_are_not_called():
    """The resolver callbacks are not called."""
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

