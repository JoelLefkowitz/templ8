import subprocess
from setuptools import find_packages, setup
from distutils.core import Command

__version__ = "{{version}}"

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
        subprocess.run(["sphinx-apidoc", "-o", "docs/", "{{src}}/", "tests/"])


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
    name="{{name}}",
    version=__version__,
    license="MIT",
    description="{{description}}",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="{{github_url}}",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    entry_points={"console_scripts": [""]},
    cmdclass={"updateDocs": UpdateDocs, "generateDocs": GenerateDocs},
    python_requires=">= 3.6",
    author="{{author}}",
    author_email="{{author_email}}",
)
