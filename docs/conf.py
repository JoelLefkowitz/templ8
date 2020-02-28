from os.path import abspath, dirname, join

project = "templater"
copyright = "Joel Lefkowitz"
author = "Joel Lefkowitz"

master_doc = "templater/docs/modules"
output_dir = dirname(abspath(__file__))
source_dir = dirname(abspath(join(__file__, "..")))

extensions = ["sphinx.ext.napoleon", "sphinx.ext.autodoc", "sphinxcontrib.apidoc"]

apidoc_module_dir = source_dir
apidoc_output_dir = output_dir
apidoc_extra_args = ["-d=1"]

napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True

# Must exclude venv rst files
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "venv"]
html_theme = "yummy_sphinx_theme"