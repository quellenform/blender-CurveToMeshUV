# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Geometry Nodes Overview'
copyright = '2023, Stephan Kellermayr'
author = 'Quellenform'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx_rtd_theme',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output
# https://sphinx-rtd-theme.readthedocs.io/en/stable/configuring.html

html_theme = 'sphinx_rtd_theme'
html_logo = 'images/logo.png'
html_favicon = 'images/icon.ico'
html_theme_options = {
    'analytics_anonymize_ip': True,
    'display_version': False,
    'logo_only': False,
    'titles_only': False,
    'display_github': 'raw',
    #'style_nav_header_background': '#343131'
}

# -- Options for EPUB output
epub_show_urls = 'footnote'
