# Templ8


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
pip install yummy_cereal
```

Alternatively, you can clone the repo and build the package locally.

### Motivation

Parsing and serializing objects to and from configurations can become overly complicated, particularly if the objects are listed by name. Suitable factories avoid having to make specific parsers or an overly verbose configuration.

#### Parsing

```yaml
---
name: Big munch grill
languages:
  - English
  - French

courses:
  Appetizers:
    Pico de Gallo:
    Pineapple Salsa:
    Oven Baked Soft Pretzels:
    Taco Ring:
    Pizza bites:

  Main course:
    Pasta:
      Sauce:
        - Rose
        - Alfredo
        - Cream
      Shapes:
        - Penne
        - Bow-tie
        - Ravioli
    Pizza:
      Toppings:
        - Beef
        - Bazil
        - Tomato
        - Peppers

  Desserts:
    Gooey Brownies:
    Butterfinger Cookie Dough:

drinks:
  Fruit juice:
  Green tea:
  Coffee:

specials:
  Banana split:
```

We can make simple annotated classes:

```python
from dataclasses import dataclass, field
from typing import Any, Dict, List


@dataclass
class Dish:
    name: str
    details: Any = None


@dataclass
class Course:
    name: str
    dishes: List[Dish] = field(default_factory=list)


@dataclass
class Menu:
    name: str
    languages: List[str]
    courses: List[Course] = field(default_factory=list)
    specials: List[Dish] = field(default_factory=list)
    drinks: List[Dish] = field(default_factory=list)
```

And then create parsers:

```python
  dish_parser = AnnotationsParser(Dish)
  
  course_parser = AnnotationsParser(Course, specified_parsers={Dish: dish_parser})

  menu_parser = AnnotationsParser(
      Menu, specified_parsers={Course: course_parser, Dish: dish_parser}
  )
```

Finally, we can parse the objects:

```python
from ruamel.yaml import load, Loader

with open(config, "r") as stream:
    menu_config = load(stream, Loader=Loader)

menu = menu_parser(menu_config)
```

```bash
>>> menu
Menu(name='Big munch grill', languages=['English', 'French'], courses=[Course(name='Appetizers'...
```

Attributes called "name" have been inferred from the dictionary style layout of the configuration.

#### Validation

We can specify a list of validation checks to perform before parsing the configuration data:

```python
from yummy_cereal import ValidatedParser

validators = [
  lambda config: config["name"] != "Big munch grill"
]

ValidatedParser(menu_parser, validators)
```

#### Serializing

Just as we did with parsers, we can use class annotations to construct serializers:

```python
from yummy_cereal import AnnotationsSerializer

dish_serializer = AnnotationsSerializer(Dish)

course_serializer = AnnotationsSerializer(
    Course, specified_serializers={Dish: dish_serializer}
)

menu_serializer = AnnotationsSerializer(
    Menu, specified_serializers={Course: course_serializer, Dish: dish_serializer}
)
```

### Docs

Additional details are available in the [full documentation](https://yummy-cereal.readthedocs.io/en/latest/).

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

[license]: https://img.shields.io/github/license/joellefkowitz/yummy-cereal
[release]: https://img.shields.io/github/v/tag/joellefkowitz/yummy-cereal
[pypi_downloads]: https://img.shields.io/pypi/dw/yummy-cereal

[pypi]: https://img.shields.io/pypi/v/yummy-cereal "PyPi"
[pypi_link]: https://pypi.org/project/yummy-cereal

[issues]: https://img.shields.io/github/issues/joellefkowitz/yummy-cereal "Issues"
[issues_link]: https://github.com/JoelLefkowitz/yummy-cereal/issues

[pulls]: https://img.shields.io/github/issues-pr/joellefkowitz/yummy-cereal "Pull requests"
[pulls_link]: https://github.com/JoelLefkowitz/yummy-cereal/pulls
