from pyimport import path_guard

path_guard("..", "../..")
from aliases import webserver_alias, webapp_alias, webapp_camelcase_alias
from models import Callback

yarn_callback = Callback(["ng", "config", "-g", "cli.packageManager", "yarn"])
angular_callback = Callback(
    [
        "ng",
        "new",
        "--routing=true",
        "--style=scss",
        webapp_camelcase_alias,
        "--directory",
        webapp_alias,
    ]
)
django_callback = Callback(
    ["django-admin", "startproject", webserver_alias, webserver_alias]
)
readme_callback = Callback(["pandoc", "config.pandoc"])
