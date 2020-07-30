from setuptools import setup

if __name__ == "__main__":
    setup(
        entry_points={"console_scripts": ["templ8 = templ8.__main__:entrypoint"]},
        install_requires=[
            "dataclasses",
            "pyimport",
            "ruamel.yaml",
            "docopts",
            "jinja2",
            "emoji",
            "art",
            "toposort",
            "walkmate",
            "yummy_cereal",
        ],
        extras_require={
            "dist": ["wheel", "twine", "bump2version"],
            "docs": [
                "sphinx",
                "pyimport",
                "pypandoc",
                "sphinxcontrib.apidoc",
                "sphinxcontrib.pandoc_markdown",
                "sphinx-autodoc-annotation",
                "yummy_sphinx_theme",
            ],
            "tests": [
                "pytest",
                "pytest-cov",
                "pytest-html",
                "pytest-sugar",
                "pytest-bdd",
                "pytest-watch",
            ],
        },
    )
