import subprocess
from setuptools import find_packages, setup
from distutils.core import Command

__version__ = "0.1.0"

with open("README.md", "r") as f:
    long_description = f.read()


class UpdateDocs(Command):
    description = "Update build configuration using sphinx-apidoc"
    user_options = []

    def initialize_options(self) -> None:
        self.version = __version__

    def finalize_options(self) -> None:
        pass

    def run(self) -> None:
        subprocess.run(["sphinx-apidoc", "-o", "docs/", "src/", "tests/"])


class GenerateDocs(Command):
    description = "Generate docs using sphinx-autodoc"
    user_options = []

    def initialize_options(self) -> None:
        self.version = __version__

    def finalize_options(self) -> None:
        pass

    def run(self) -> None:
        subprocess.run(["sphinx-build", "docs/", "build/"])


s = setup(
    name="templater",
    version=__version__,
    license="MIT",
    description="Configurable, intelligent project template generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JoelLefkowitz/tempalter",
    packages=find_packages(),
    install_requires=[],
    entry_points={"console_scripts": ["templater=templater.main:entrypoint"]},
    cmdclass={"updateDocs": UpdateDocs, "generateDocs": GenerateDocs},
    python_requires=">= 3.6",
    author="Joel Lefkowitz",
    author_email="joellefkowitz@hotmail.com",
)