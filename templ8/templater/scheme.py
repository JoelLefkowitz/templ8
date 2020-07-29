import os
from dataclasses import dataclass
from typing import List

from walkmate import get_child_files
from yummy_cereal import AnnotationsParser, ValidatedParser

from ..utils.files import load_yaml
from .callback import Callback
from .context import Context
from .path_replacement import PathReplacement
from .spec import RawTemplaterSpec, TemplaterSpec


@dataclass
class TemplaterScheme:
    config_path: str
    output_dir: str
    template_dirs: List[str]
    specified_files: List[str]

    @property
    def context(self) -> List[Context]:
        context_parser = ValidatedParser(
            parser=Context.from_dict, validators=[lambda x: isinstance(x, dict)]
        )
        return context_parser(load_yaml(self.config_path))

    @property
    def templater_specs(self) -> List[TemplaterSpec]:
        return TemplaterSpec.from_raw_specs(
            [
                self.parse_raw_template_spec(templater_spec_path)
                for template_dir in self.template_dirs
                for templater_spec_path in get_child_files(
                    template_dir, match_name="spec.yml"
                )
            ],
            self.context,
        )

    @staticmethod
    def parse_raw_template_spec(templater_spec_path: str) -> TemplaterSpec:
        spec_parser = AnnotationsParser(
            RawTemplaterSpec,
            specified_parsers={
                Context: AnnotationsParser(Context),
                Callback: AnnotationsParser(Callback),
                PathReplacement: AnnotationsParser(PathReplacement),
            },
            field_defaults={"root_path": os.path.dirname(templater_spec_path)},
        )

        return spec_parser(load_yaml(templater_spec_path))
