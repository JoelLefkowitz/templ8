from setuptools import setup

if __name__ == "__main__":
    setup(
        install_requires={{install_requires}},
        console_scripts={{console_scripts}},
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
