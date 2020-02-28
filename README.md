# templater
Configurable, intelligent project template generator
## Status

| Source  | Shields  |
|-----|--------------|
| Project  | ![license][license] ![release][release]  |
| Publishers  | [![pypi][pypi]][pypi_link]    |
| Downloads  | ![pypi_downloads][pypi_downloads] |
| Raised  | [![issues][issues]][issues_link] [![pulls][pulls]][pulls_link]  |

[license]: https://img.shields.io/github/license/joellefkowitz/templater

[release]: https://img.shields.io/github/v/tag/joellefkowitz/templater

[pypi]: https://img.shields.io/pypi/v/templater (PyPi)
[pypi_link]: https://pypi.org/project/templater

[python_version]: https://img.shields.io/pypi/pyversions/templater

[pypi_downloads]: https://img.shields.io/pypi/dw/templater

[issues]: https://img.shields.io/github/issues/joellefkowitz/templater (Issues)
[issues_link]: https://github.com/JoelLefkowitz/templater/issues

[pulls]: https://img.shields.io/github/issues-pr/joellefkowitz/templater (Pull requests)
[pulls_link]: https://github.com/JoelLefkowitz/templater/pulls

### Installing

Install the package from pypi:

```bash
pip install templater
```

Alternatively, you can clone the repo:

```bash
git clone https://github.com/JoelLefkowitz/tempalter
```

## Running tests
Tests are not included in the package build. Clone the repo to include all the source files.

```bash
pytest tests
```

## Docs
Docs are not included in the package build. Clone the repo to include all the source files.

To automatically update the documentation generation configuration:

```bash
python setup.py updateDocs
```

Documentation can be generated locally:

```bash
python setup.py generateDocs
```

Then to view the generated docs visit ./build/sphinx/html/templater/docs/modules.html:

```bash
open -a "Google Chrome" ./build/sphinx/html/templater/docs/modules.html
```

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the tags on this repository. 

Bumpversion is used to version and tag changes.
For example:

```bash
bump2version patch
```

Releases are made on every major change.
## Author

* **Joel Lefkowitz** - *Initial work* - [Joel Lefkowitz](JoelLefkowitz)

See also the list of contributors who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

None