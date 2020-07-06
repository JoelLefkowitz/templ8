from typing import List
from dataclasses import dataclass
from inspect import cleandoc

docopts_cli = cleandoc(
    """
    Usage:
        templ8 <config_path> 
               [--output-dir <output_dir>]
               [--template-dirs <template_dirs>]...
               [--specified-files <specified_files>]... 
               [(--overwrite | --dry-run) --skip-callbacks]

    Options:
      --dry-run
      --overwrite
      --skip-callbacks
    """
)


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
