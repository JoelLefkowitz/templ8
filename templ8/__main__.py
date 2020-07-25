# TODO Dont say overwriting if nfile doesnt exist
# TODO List specs that match
# TODO Specify skipped files
# TODO Break into functions
# TODO Dependencies are not being included
# TODO Dont allow none values unless --allow-none set
# TODO Add to readmes readthedocs may need to be configured
# TODO Add to readmes gitflow use
# TODO Add to readmes use of statuses to test pull requests
# TODO Add to readmes buildbot use
# TODO Add to readmes available manual jobs


import os
from distutils.util import strtobool

from art import text2art

from .cli import parse_cli
from .templater.options import TemplaterOptions
from .templater.scheme import TemplaterScheme
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
        print(
            text2art("Templ8", font="cybermedium") + "Plan:"
            if plan_mode
            else text2art("Generating", font="cybermedium")
        )

    generated_paths = []

    for templater_spec in templater_scheme.templater_specs:
        for template in templater_spec.templates:

            include_file = (
                not templater_scheme.specified_files
                or template.name in templater_options.specified_files
            )

            output_path = os.path.normpath(
                os.path.join(templater_scheme.output_dir, template.rel_output_path)
            )

            path_motion = (
                f"{os.path.normpath(template.rel_output_path)} -> {output_path}"
            )

            if include_file and templater_options.overwrite:
                step_msg = f"{'Overwrite' if plan_mode else 'Overwritting'}: {template.name} ({path_motion})"

            elif include_file and (
                not os.path.exists(output_path) or output_path in generated_paths
            ):
                step_msg = f"{'Generate' if plan_mode else 'Generating'}: {template.name} ({path_motion})"

            else:
                continue

            if not templater_options.silent:
                print(step_msg)

            if not plan_mode:
                generated_paths.append(output_path)
                write_file(template.render(templater_spec.context), output_path)

        if not templater_options.skip_callbacks:
            for callback in templater_spec.callbacks:

                if not templater_options.silent:
                    print(
                        f"{'Run' if plan_mode else 'Running'}: {callback.name} ({callback.call})"
                    )

                if not plan_mode:
                    callback(
                        cwd=templater_scheme.output_dir,
                        capture_output=not templater_options.silent,
                    )


if __name__ == "__main__":
    entrypoint()
