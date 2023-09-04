# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

import os
import sys
import datetime

# -- Project information -----------------------------------------------------

project = 'Test Project'
author = 'Dominik Viererbe'
version = '1.0'
copyright = f'{author}, {datetime.date.today().year}'

# -- General configuration ---------------------------------------------------

needs_sphinx = '4.3.2'
extensions = []
root_doc = 'index'
exclude_patterns = ['.sphinx/venv/*']

manpages_url = 'https://manpages.ubuntu.com/manpages/mantic/en/man{section}/{page}.{section}.html'

# -- Options for HTML output -------------------------------------------------

html_title = 'Test Project'

# -- Options for EPUB output -------------------------------------------------

epub_basename = 'test-pproject'
epub_show_urls = 'no'

# -- Options for PDF output --------------------------------------------------

latex_engine = 'xelatex'
latex_show_pagerefs = True
latex_show_urls = 'footnote'
latex_elements = {
    'papersize': 'a4paper',
}
latex_documents = [
    (
        root_doc,
        html_title,
        author,
        'manual',
        True,
    ),
]
