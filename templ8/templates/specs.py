from pyimport import path_guard

path_guard("..", "../..")
from models import Context, Spec, Alias, Callback
from aliases import webapp_alias, webapp_camelcase_alias, webserver_alias
from callbacks import angular_callback, django_callback, yarn_callback

common_spec = Spec(
    root_name="common",
    context_set=[
        Context("name"),
        Context("version", "0.1.0"),
        Context("description"),
        Context("author"),
        Context("readme", "No description provided"),
    ],
)
package_spec = Spec(
    root_name="package",
    dependencies=["common"],
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
)
webapp_spec = Spec(
    root_name="webapp",
    dependencies=["common"],
    context_set=[Context("github_url"), Context("deploy_url")],
    folder_aliases={"webapp": webapp_alias,},
    callbacks=[yarn_callback, angular_callback],
)
server_spec = Spec(
    root_name="server",
    dependencies=["webapp"],
    folder_aliases={"server": webserver_alias,},
    callbacks=[django_callback],
)
