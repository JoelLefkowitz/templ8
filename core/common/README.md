# {{ name }}

{{ description }}

### Status

| Source     | Shields                                                        |
| ---------- | -------------------------------------------------------------- |
| Project    | ![license][license]                                            |
| Raised     | [![issues][issues]][issues_link] [![pulls][pulls]][pulls_link] |

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
