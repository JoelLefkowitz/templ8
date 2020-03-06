from pyimport import path_guard
from inspect import cleandoc

from pyimport import path_guard; path_guard(__file__, "..")
from models import Context, Spec, Alias, Callback
from utils import to_app_name, to_camelcase_app_name, to_server_name

CLI = cleandoc(
    """
    Usage:
      templ8 <config_path> <output_dir> [--overwrite | --dry-run] [NAMES ...]

    Options:
      --overwrite
      --dry-run
    """
)

webapp_alias = Alias(Context("name"), lambda x: to_app_name(x))
webapp_camelcase_alias = Alias(Context("name"), lambda x: to_camelcase_app_name(x))
webserver_alias = Alias(Context("name"), lambda x: to_server_name(x))

SPECS = [
    Spec(
        root_name="common",
        context_set=[
            Context("name"),
            Context("version", "0.1.0"),
            Context("description"),
            Context("author"),
            Context("readme", "No description provided"),
        ],
    ),
    Spec(
        root_name="package",
        context_set=[
            Context("author_email"),
            Context("author_github"),
            Context("github_url"),
            Context("twine_username"),
            Context("console_scripts", []),
            Context("install_requires", []),
            Context("extra_requirements", []),
        ],
        folder_aliases={"src": Alias(Context("name"))},
    ),
    Spec(
        root_name="webapp",
        dependencies=["common"],
        context_set=[Context("github_url"),],
        include_root_dir=True,
        folder_aliases={"webapp": webapp_alias,},
        callbacks=[
            Callback(["ng", "config", "-g", "cli.packageManager", "yarn"]),
            Callback(
                [
                    "ng",
                    "new",
                    "--routing=true",
                    "--style=scss",
                    webapp_camelcase_alias,
                    "--directory",
                    webapp_alias,
                ]
            ),
        ],
    ),
    Spec(
        root_name="server",
        dependencies=["webapp"],
        folder_aliases={"server": webserver_alias,},
        include_root_dir=True,
        callbacks=[
            Callback(["django-admin", "startproject", webserver_alias, webserver_alias])
        ],
    ),
]
