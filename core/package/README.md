# {{ canonical_name }}

{{ description }}

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
pip install {{ package_name }}
```

Alternatively, you can clone the repo and build the package locally.

### Docs

Examples and additional details are available in the [full documentation](https://{{ name }}.readthedocs.io/en/latest/).

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

- **{{author}}** - _Initial work_ - [{{author}}](https://github.com/{{ github_username }})

See also the list of contributors who participated in this project.

### License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

### Acknowledgments

None yet!

<!--- Table links --->

[license]: https://img.shields.io/github/license/{{ github_username }}/{{ name }}
[issues]: https://img.shields.io/github/issues/{{ github_username }}/{{ name }} "Issues"
[issues_link]: https://github.com/{{ github_username}}/{{ name }}/issues
[pulls]: https://img.shields.io/github/issues-pr/j{{ github_username }}/{{ name }} "Pull requests"
[pulls_link]: https://github.com/{{ github_username }}/{{ name }}/pulls

[release]: https://img.shields.io/github/v/tag/{{ github_username }}/{{ name }}
[pypi_downloads]: https://img.shields.io/pypi/dw/{{ package_name }}
[pypi]: https://img.shields.io/pypi/v/{{ package_name }} "PyPi"
[pypi_link]: https://pypi.org/project/{{ package_name }}
