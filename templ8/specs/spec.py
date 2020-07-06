# TODO Redesign specs
# import re
# import os
# import pathlib
# import subprocess
# from typing import Any, Dict, Iterator, List, Optional, Type, TypeVar
# from dataclasses import dataclass, field
# from jinja2 import Environment, FileSystemLoader, Template, StrictUndefined
# from exceptions import MissingContext

# T = TypeVar("T")

# @dataclass
# class Spec:
#     name: str
#     root_path: str
#     required_context: List[str] = field(default_factory=list)
#     required_context_extends: List[str] = field(default_factory=list)
#     path_replacements: List[PathReplacement] = field(default_factory=list)
#     callbacks: List[Callback] = field(default_factory=list)

#     @property
#     def templates(self) -> Iterator[TemplateProxy]:
#         template_base = os.path.dirname(self.root_path)

#         loader = Environment(
#             loader=FileSystemLoader(template_base),
#             trim_blocks=True,
#             lstrip_blocks=True,
#             keep_trailing_newline=True,
#             undefined=StrictUndefined,
#         )

#         for file_path in get_child_files(template_base):

#             if file_path == self.root_path:
#                 continue

#             source_path = os.path.relpath(file_path, template_base)
#             template = loader.get_template(source_path)
#             yield TemplateProxy(template, source_path)

#     def check_sufficient(self, config: Dict) -> bool:
#         return set(self.required_context) <= set(config)

#     def check_condition(self, config: Dict) -> bool:
#         return self.name in config and config[self.name] is True

#     def decode(self, config) -> None:
#         if self.path_replacements:
#             for pr in self.path_replacements:
#                 pr.replacement = Context.resolve_in_str(pr.replacement, config)

#         if self.callbacks:
#             for cb in self.callbacks:
#                 cb.call = Context.resolve_in_str(cb.call, config)

#     def __str__(self) -> str:
#         return str(self.__dict__)
