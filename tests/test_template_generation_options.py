# coding=utf-8
"""Template generation options feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('tests/template_generation_options.feature', 'Dont generate files for a dry run')
def test_dont_generate_files_for_a_dry_run():
    """Dont generate files for a dry run."""


@scenario('tests/template_generation_options.feature', 'Dont run callbacks when deactivated')
def test_dont_run_callbacks_when_deactivated():
    """Dont run callbacks when deactivated."""


@scenario('tests/template_generation_options.feature', 'Generate specific files only')
def test_generate_specific_files_only():
    """Generate specific files only."""


@scenario('tests/template_generation_options.feature', 'Overwrite files')
def test_overwrite_files():
    """Overwrite files."""


@scenario('tests/template_generation_options.feature', 'Skip callbacks when files skipped')
def test_skip_callbacks_when_files_skipped():
    """Skip callbacks when files skipped."""


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


@then('All files are skipped')
def all_files_are_skipped():
    """All files are skipped."""
    raise NotImplementedError


@then('Clashing files are overwritten')
def clashing_files_are_overwritten():
    """Clashing files are overwritten."""
    raise NotImplementedError


@then('Only matching templates are generated in the output directory')
def only_matching_templates_are_generated_in_the_output_directory():
    """Only matching templates are generated in the output directory."""
    raise NotImplementedError


@then('The callbacks that would have been called are reported')
def the_callbacks_that_would_have_been_called_are_reported():
    """The callbacks that would have been called are reported."""
    raise NotImplementedError


@then('The files overwritten are reported')
def the_files_overwritten_are_reported():
    """The files overwritten are reported."""
    raise NotImplementedError


@then('The files that would have been generated are reported')
def the_files_that_would_have_been_generated_are_reported():
    """The files that would have been generated are reported."""
    raise NotImplementedError


@then('The files that would not have been generated are reported')
def the_files_that_would_not_have_been_generated_are_reported():
    """The files that would not have been generated are reported."""
    raise NotImplementedError


@then('The resolver callbacks are not called')
def the_resolver_callbacks_are_not_called():
    """The resolver callbacks are not called."""
    raise NotImplementedError

