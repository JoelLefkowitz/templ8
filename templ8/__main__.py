import os
from distutils.util import strtobool
from typing import List

from art import text2art

from .cli import parse_cli
from .templater.callback import Callback
from .templater.options import TemplaterOptions
from .templater.scheme import TemplaterScheme
from .templater.spec import Template
from .templater.spec import TemplaterSpec
from .utils.files import write_file


def entrypoint() -> None:
    templater_scheme, templater_options = parse_cli()
    generate_and_report(templater_scheme, templater_options, plan_mode=True)

    if templater_options.silent or templater_options.assume_yes or prompt_check():
        generate_and_report(templater_scheme, templater_options, plan_mode=False)


def prompt_check() -> bool:
    try:
        return strtobool(input("Would you like to continue? "))
    except ValueError:
        return False


def generate_and_report(
    templater_scheme: TemplaterScheme,
    templater_options: TemplaterOptions,
    plan_mode: bool,
) -> None:

    if not templater_options.silent:
        report_heading(plan_mode)

    accepted_paths = []  # type: List[str]

    for templater_spec in templater_scheme.templater_specs:

        if not templater_options.silent:
            report_spec(templater_spec, plan_mode)

        generate_templates(
            templater_scheme,
            templater_options,
            templater_spec,
            accepted_paths,
            plan_mode,
        )

        report_tally(accepted_paths)

        if not templater_options.skip_callbacks:
            run_callbacks(
                templater_scheme, templater_options, templater_spec, plan_mode
            )


def generate_templates(
    templater_scheme: TemplaterScheme,
    templater_options: TemplaterOptions,
    templater_spec: TemplaterSpec,
    accepted_paths: List[str],
    plan_mode: bool,
):
    for template in templater_spec.templates:

        include_file = (
            not templater_scheme.specified_files
            or template.name in templater_options.specified_files
        )

        output_path = os.path.normpath(
            os.path.join(templater_scheme.output_dir, template.rel_output_path)
        )

        if include_file and not os.path.exists(output_path):
            status = "new"

        elif (
            include_file
            and os.path.exists(output_path)
            and output_path in accepted_paths
        ):
            status = "rewrite"

        elif (
            include_file and os.path.exists(output_path) and templater_options.overwrite
        ):
            status = "overwrite"

        else:
            continue

        accepted_paths.append(output_path)

        if not templater_options.silent:
            report_template(template, output_path, status, plan_mode)

        if not plan_mode:
            write_file(template.render(templater_spec.context), output_path)


def run_callbacks(
    templater_scheme: TemplaterScheme,
    templater_options: TemplaterOptions,
    templater_spec: TemplaterSpec,
    plan_mode: bool,
):
    for callback in templater_spec.callbacks:

        if not templater_options.silent:
            report_callback(callback, plan_mode)

        if not plan_mode:
            callback(
                cwd=templater_scheme.output_dir,
                capture_output=not templater_options.silent,
            )


def report_heading(plan_mode: bool) -> None:
    if plan_mode:
        print(text2art("Templ8") + "Plan:")
    else:
        print(text2art("Generating", font="cybermedium"))


def report_spec(templater_spec: TemplaterSpec, plan_mode: bool) -> None:
    spec_path = os.path.relpath(templater_spec.root_path, os.getcwd())
    if plan_mode:
        print(f"Spec plan: {templater_spec.name} ({spec_path})")
    else:
        print(f"Spec: {templater_spec.name} ({spec_path})")


def report_template(
    template: Template, output_path: str, status: str, plan_mode: bool
) -> None:
    path_motion = f"{os.path.normpath(template.rel_output_path)} -> {output_path}"

    if plan_mode:
        print(f"Generate: ({status}) {path_motion}")
    else:
        print(f"Generating: ({status}) {path_motion}")


def report_tally(accepted_paths: List[str]) -> None:
    print(f"Running total: {len(accepted_paths)} template(s)\n")


def report_callback(callback: Callback, plan_mode: bool) -> None:
    if plan_mode:
        print(f"Run: {callback.name} ({callback.call})")
    else:
        print(f"Running: {callback.name} ({callback.call})")


if __name__ == "__main__":
    entrypoint()
