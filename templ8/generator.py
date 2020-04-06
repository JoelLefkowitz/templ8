from typing import List, Dict
from .models import Spec


def generate_templates(
    config: Dict,
    specs: List[Spec],
    output_dir: str,
    specified_files: List[str],
    options: Dict,
) -> None:
    pass


# def resolve_template(
#     self, template: Template, file_path: str, output_dir: str
# ) -> None:
#     context_dict = {i: i.read for i in self.context}
#     output = template.resolve(context_dict)

#     output_path = self.resolve_output_path(file_path, output_dir)
#     pathlib.Path(os.path.dirname(output_path)).mkdir(parents=True, exist_ok=True)
#     with open(output_path, "w") as f:
#         f.write(output)


# spec, output_dir
# for template, file_path in spec.templates:
#     spec.resolve_output_path(file_path, output_dir)
#     template.resolve({k: v.read for k, v in spec.context.items()})
#     for spec in specs:

#         skipped_any = False
#         for template, output_path in spec.load_templates(
#             config, template_dir, output_dir
#         ):
#             success = outputter(template, output_path, context_dict, options)
#             if not success:
#                 skipped_any = True

#         for callback in spec.callbacks:
#             if skipped_any:
#                 pretty_log(f"Would callback: {callback.call}")
#             elif options["no_callbacks"]:
#                 pretty_log(f"Skippig callback: {callback.call}")
#             else:
#                 callback.run(config, output_dir)


# def bundle_context(config, specs) -> dict:
#     context = dict(
#         [
#             context.emit_from_config(config)
#             for spec in specs
#             for context in spec.context_set
#         ]
#     )
#     context.update({spec.root_name: True for spec in specs})
#     context.update(
#         {
#             folder_name: spec.folder_aliases[folder_name].resolve(config)
#             for spec in specs
#             for folder_name in spec.folder_aliases
#         }
#     )
#     return context


# def outputter(
#     template: Template, output_path: str, context_dict: dict, options: dict
# ) -> bool:
#     filename = os.path.basename(os.path.normpath(output_path))

#     if options["specified_names"] and filename not in options["specified_names"]:
#         pretty_log(output_path + " not in NAMES; skipping")
#         return False

#     if os.path.exists(output_path) and not options["overwrite"]:
#         pretty_log(output_path + " exists; skipping")
#         return False

#     if options["dry-run"]:
#         pretty_log("Would write: " + output_path)
#         return False

#     Path(os.path.dirname(output_path)).mkdir(parents=True, exist_ok=True)
#     with open(output_path, "w") as f:
#         f.write(template.render(context_dict))
#         pretty_log("Generated: " + output_path)
#     return True
