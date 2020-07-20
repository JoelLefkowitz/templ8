# {{name}}

{{description}}
{% if not private %}
### Status

| Source     | Shields                                                        |
| ---------- | -------------------------------------------------------------- |
| Project    | ![license][license] ![release][release]                        |
| Downloads  | ![pypi_downloads][pypi_downloads]                              |
| Raised     | [![issues][issues]][issues_link] [![pulls][pulls]][pulls_link] |

<!--- Table links --->

[license]: https://img.shields.io/github/license/{{author_github}}/{{name}}
[release]: https://img.shields.io/github/v/tag/{{author_github}}/{{name}}

[issues]: https://img.shields.io/github/issues/{{author_github}}/{{name}} "Issues"
[issues_link]: https://github.com/{{author_github}}/{{name}}/issues

[pulls]: https://img.shields.io/github/issues-pr/{{author_github}}/{{name}} "Pull requests"
[pulls_link]: https://github.com/{{author_github}}/{{name}}/pulls
{% endif %}

### Usage
{{readme_body}}

### Author

- **{{author}}** - _Initial work_ - [{{author}}](https://github.com/{{author_github}})

See also the list of contributors who participated in this project.

### License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

### Acknowledgments

None yet!
