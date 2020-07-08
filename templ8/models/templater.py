from dataclasses import dataclass
from typing import List


@dataclass
class TemplaterOptions:
    dry_run: bool
    overwrite: bool
    skip_callbacks: bool


@dataclass
class TemplaterScheme:
    config_path: str
    output_dir: str
    template_dirs: List[str]
    specified_files: List[str]
    options: TemplaterOptions
