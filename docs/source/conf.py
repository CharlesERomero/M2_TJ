# Configuration file for the Sphinx documentation builder.

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import os
import sys
#sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath("../../src"))

# -- Project information

project = 'M2_ProposalTools'
copyright = '2025, Charles'
author = 'Charles Romero'

release = '1.0'
version = '1.2.2'

# -- General configuration

master_doc = 'index'

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.autosummary',
    'sphinx.ext.graphviz',
    'sphinx.ext.autosectionlabel',
    #'sphinxcontrib.plantuml',
    'sphinx.ext.napoleon',
    'nbsphinx',
    #'matplotlib.sphinxext.plot_directive',
    'sphinx.ext.inheritance_diagram',
    'sphinx.ext.mathjax'
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
