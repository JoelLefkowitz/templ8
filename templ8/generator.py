import os, pathlib, functools
from typing import List, Dict
from .models import Spec
from .utils import pretty_log
from collections import namedtuple

Summary = namedtuple("Summary", ["generated", "skipped"])

def generate_templates(
    config: Dict,
    specs: List[Spec],
    output_dir: str,
    specified_files: List[str],
    options: Dict,
) -> None:

    for spec in filter(lambda x: x.include(config), specs):
        summary = Summary(generated=[], skipped=[])
        
        for proxy in spec.templates:
            template, source_path = proxy
            output = template.render(config)
            processed_path = functools.reduce(
                lambda res, f: f(res), spec.path_replacements, source_path
            )

            file_name = os.path.basename(os.path.normpath(processed_path))
            output_path = os.path.join(output_dir, processed_path)

            if (
                options["specified_files"]
                and file_name not in options["specified_files"]
            ):
                pretty_log(f"Skipping {output_path} - Not in specified files")
                summary.skipped.append(output_path)

            elif os.path.exists(output_path) and not options["overwrite"]:
                pretty_log(f"Skipping {output_path} - File already exists")
                summary.skipped.append(output_path)

            elif options["dry-run"]:
                pretty_log(f"Dry run - would write: {output_path}")
                summary.skipped.append(output_path)

            else:
                pathlib.Path(os.path.dirname(output_path)).mkdir(
                    parents=True, exist_ok=True
                )
                summary.generated.append(output_path)
                pretty_log(
                    "Overwriting "
                    if os.path.exists(output_path) and options["overwrite"]
                    else "Generating " + output_path
                )

                with open(output_path, "w") as f:
                    f.write(output)

        for callback in spec.callbacks:
            if summary.skipped:
                pretty_log(f"Skipping {callback.name} - Didn\'t generate entire spec\n{callback.call}")

            elif options["no_callbacks"]:
                pretty_log(f"Skipping {callback.name} - Callbacks skipped\n{callback.call}")

            else:
                pretty_log(f"Running {callback.name}\n{callback.call}")
                callback(output_dir)

        generated, skipped = '\n'.join(summary.generated), '\n'.join(summary.skipped)
        pretty_log(f"Summary - {spec.name}:\nGenerated: {generated}\nSkipped: {skipped}")