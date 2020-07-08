from setuptools import setup

console_scripts = {{console_scripts}}
install_requires = ["django"] + {{install_requires}}
extras_require = {
    "dist": ["wheel", "twine", "bump2version"],
    "docs": [
        "sphinx",
        "pypandoc",
        "sphinxcontrib.apidoc",
        "sphinxcontrib.pandoc_markdown",
        "sphinx-autodoc-annotation",
        "yummy_sphinx_theme",
    ],
    "tests": ["pytest", "pytest-cov", "pytest-html", "pytest-sugar", "pytest-bdd",],
} + {{extra_requirements}}

if __name__ == "__main__":
    setup(
        console_scripts=console_scripts,
        install_requires=install_requires,
        extras_require=extras_require,
    )
