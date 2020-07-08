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
