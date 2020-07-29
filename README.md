# Templ8

Configurable, intelligent project template generator

#### Features:

* Resolves a context dictionary into Jinja templates
* Supports folder renaming
* Supports callbacks

### Status

| Source     | Shields                                                        |
| ---------- | -------------------------------------------------------------- |
| Project    | ![license][license] ![release][release]                        |
| Publishers | [![pypi][pypi]][pypi_link]                                     |
| Downloads  | ![pypi_downloads][pypi_downloads]                              |
| Raised     | [![issues][issues]][issues_link] [![pulls][pulls]][pulls_link] |

### Installing

To install the package from pypi:

```bash
pip install templ8
```

Alternatively, you can clone the repo and build the package locally.

### Usage

```bash
Usage:
    templ8 <config_path> 
           [--output-dir <output_dir>]
           [--template-dirs <template_dirs>]...
           [--specified-files <specified_files>]... 
           [--silent --overwrite --assume-yes --skip-callbacks]

Options:
  --silent          Supress stdout and assume automatic yes to prompts
  --overwrite       Allow existing files to be overwritten
  --assume-yes      Automatic yes to prompts
  --skip-callbacks  Don't run callbacks
```

```bash
$ templ8 .template.yml
```

```bash
 _____                          _   ___  
|_   _|  ___  _ __ ___   _ __  | | ( _ ) 
  | |   / _ \| '_ ` _ \ | '_ \ | | / _ \ 
  | |  |  __/| | | | | || |_) || || (_) |
  |_|   \___||_| |_| |_|| .__/ |_| \___/ 
                        |_|              
Plan:
Spec plan: common (templ8/templates/common)
Generate: (new) LICENSE.md -> ./LICENSE.md
Generate: (new) README.md -> ./README.md
Generate: (new) .gitignore -> ./.gitignore
Running total: 3 template(s)

Would you like to continue?
```

#### Configuration file syntax

The configuration file should be a yaml file of key value pairs with the names of template sets to include set to True. Missing values default to None.

#### **`.template.yml`**
```yml
common: True
name: Example
version: 0.1.0
description: An example project
author: Joel Lefkowitz
author_github: JoelLefkowitz
```

#### Template specification architecture

Every template set contains Jinja templates and has a spec file. Extended specs will be generated sequentially.

#### **`templ8/templates/package/spec.yml`**
```yml
name: package

extends: 
  - common

required_context: 
  package_name:
  author_email:
  twine_username:
  python_version: 3.6
  keywords: []
  console_scripts: []
  install_requires: []
  buildbot_worker_password:
  buildbot_database_password:
  
path_replacements:
  src: <package_name>

callbacks:
   create_venv: python3 -m venv venv
```

Context values may be included in path_replacements and callbacks when enclosed in tags.

#### Important templating tasks not automated by templ8

* Creation of remote repositories
* Activation and integration of a pipeline
* Documentation host integration

### Docs

Additional details are available in the [full documentation](https://templ8.readthedocs.io/en/latest/).

To generate the documentation locally:

```bash
multi-job docs
```

### Tests

Unit tests and behaviour tests are written with the pytest framework.

To run tests:

```bash
multi-job tests
```

Additionally, an html report will be saved to the local directory.

### Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests.

### Versioning

[SemVer](http://semver.org/) is used for versioning. For a list of versions available, see the tags on this repository.

Bump2version is used to version and tag changes.
For example:

```bash
bump2version patch
```

Releases are made on every major change.

### Author

- **Joel Lefkowitz** - _Initial work_ - [Joel Lefkowitz](https://github.com/JoelLefkowitz)

See also the list of contributors who participated in this project.

### License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

### Acknowledgments

None yet!

<!--- Table links --->

[license]: https://img.shields.io/github/license/joellefkowitz/templ8
[release]: https://img.shields.io/github/v/tag/joellefkowitz/templ8
[pypi_downloads]: https://img.shields.io/pypi/dw/templ8

[pypi]: https://img.shields.io/pypi/v/templ8 "PyPi"
[pypi_link]: https://pypi.org/project/templ8

[issues]: https://img.shields.io/github/issues/joellefkowitz/templ8 "Issues"
[issues_link]: https://github.com/JoelLefkowitz/templ8/issues

[pulls]: https://img.shields.io/github/issues-pr/joellefkowitz/templ8 "Pull requests"
[pulls_link]: https://github.com/JoelLefkowitz/templ8/pulls
