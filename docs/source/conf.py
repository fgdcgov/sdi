# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'SDI Knowledge Directory'
copyright = '2023, FGDC'
author = 'FGDC'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

# Values of the intersphinx_mapping keys that you want to enable hoverxref on
hoverxref_intersphinx = [
   "astropy",
   "numpy",
   "scipy",
   "matplotlib",
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
