from pyimport import path_guard

path_guard("..", "../..")
from models import Context, Alias
from formatters import to_app_name, to_camelcase_app_name, to_server_name

webapp_alias = Alias(Context("name"), to_app_name)
webapp_camelcase_alias = Alias(Context("name"), to_camelcase_app_name)
webserver_alias = Alias(Context("name"), to_server_name)
