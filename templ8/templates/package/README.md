# {{name}}

{{description}}
{% if not private %}
### Status

| Source     | Shields                                                        |
| ---------- | -------------------------------------------------------------- |
| Project    | ![license][license] ![release][release]                        |
| Publishers | [![pypi][pypi]][pypi_link]                                     |
| Downloads  | ![pypi_downloads][pypi_downloads]                              |
| Raised     | [![issues][issues]][issues_link] [![pulls][pulls]][pulls_link] |

<!--- Table links --->

[license]: https://img.shields.io/github/license/{{author_github}}/{{name}}
[release]: https://img.shields.io/github/v/tag/{{author_github}}/{{name}}
[pypi_downloads]: https://img.shields.io/pypi/dw/{{package_name}}

[pypi]: https://img.shields.io/pypi/v/{{package_name}} "PyPi"
[pypi_link]: https://pypi.org/project/{{package_name}}

[issues]: https://img.shields.io/github/issues/{{author_github}}/{{name}} "Issues"
[issues_link]: https://github.com/{{author_github}}/{{name}}/issues

[pulls]: https://img.shields.io/github/issues-pr/{{author_github}}/{{name}} "Pull requests"
[pulls_link]: https://github.com/{{author_github}}/{{name}}/pulls
{% endif %}

### Usage
{{readme_body}}

### Installing

To install the package from pypi:

```bash
pip install {{package_name}}
```

Alternatively, you can clone the repo and build the package locally.

### Docs

Additional details are available in the [full documentation](https://{{name}}.readthedocs.io/en/latest/).

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

### Buildbot

To run the buildbot server:

```bash
cd ci
docker-compose up -d
```

* Builders are configured in master.cfg.
* Build masters read their configuration from https://github.com/{{author_github}}/{{name}}/{{package_name}}/ci/master.cfg
* Worker and database passwords are configured as environment variables

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

- **{{author}}** - _Initial work_ - [{{author}}](https://github.com/{{author_github}})

See also the list of contributors who participated in this project.

### License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

### Acknowledgments

None yet!
