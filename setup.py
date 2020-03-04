import subprocess
from setuptools import find_packages, setup
from distutils.core import Command

__version__ = "0.6.4"

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
    name="templ8",
    version=__version__,
    license="MIT",
    description="Configurable, intelligent project template generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JoelLefkowitz/temp8",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "jinja2>=2.11.1",
        "ruamel.yaml>=0.16.10",
        "docopt>=0.6.1",
        "emoji>=0.5.4",
        "dataclasses>=0.7",
        "pyimport>=0.3.0",
    ],
    entry_points={"console_scripts": ["templ8=templ8.main:entrypoint"]},
    cmdclass={"updateDocs": UpdateDocs, "generateDocs": GenerateDocs},
    python_requires=">= 3.6",
    author="Joel Lefkowitz",
    author_email="joellefkowitz@hotmail.com",
)
