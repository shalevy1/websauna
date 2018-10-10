# !/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Websauna documentation build configuration file, created by
# sphinx-quickstart on Sun Jun 28 21:46:46 2015.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# Standard Library
import os

import pkg_resources
from datetime import datetime

import sphinx_rtd_theme


# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
# sys.path.insert(0, os.path.abspath('.'))

_release = pkg_resources.get_distribution("websauna").version
_version = _release.split('.')

major_version = _version[0]
minor_version = _version[1]

this_year = datetime.now().year

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here. needs_sphinx = '1.0'
# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
    'sphinx_autodoc_typehints',
    'sphinxcontrib.zopeext.autointerface'
]

# Add any paths that contain templates here, relative to this directory.
# templates_path = ['_templates', os.path.dirname(sphinx_rtd_theme.__file__)]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'Websauna'
copyright = '2015-{0}, Mikko Ohtamaa'.format(this_year)
author = 'Mikko Ohtamaa'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '{0}.{1}'.format(major_version, minor_version)
# The full version, including alpha/beta/rc tags.
release = _release

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = [
    # "api/websauna.tests.test_*.rst",
]

# The reST default role (used for this markup: `text`) to use for all
# documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
# keep_warnings = False

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "sphinx_rtd_theme"

html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# Add Edit on GitHub link
html_context = {
    'display_github': True,
    'github_user': "websauna",
    'github_repo': "websauna",
    'github_version': "master",
    'conf_py_path': "/docs/source/",
    'page_source_suffix': '.rst',
}

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
# html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
# html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = "Websauna Documentation"

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
# html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
# html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
# html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
# html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
# html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no module index is generated.
# html_domain_indices = True

# If false, no index is generated.
# html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
# html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
# html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
# html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# Language to be used for generating the HTML full-text search index.
# Sphinx supports the following languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'h', 'it', 'ja'
#   'nl', 'no', 'pt', 'ro', 'r', 'sv', 'tr'
# html_search_language = 'en'

# A dictionary with options for the search language support, empty by default.
# Now only 'ja' uses this config value
# html_search_options = {'type': 'default'}

# The name of a javascript file (relative to the configuration directory) that
# implements a search results scorer. If empty, the default will be used.
# html_search_scorer = 'scorer.js'

# Output file base name for HTML help builder.
htmlhelp_basename = 'Websaunadoc'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    # 'preamble': '',

    # Latex figure (float) alignment
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'Websauna.tex', 'Websauna Documentation', 'Mikko Ohtamaa', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
# latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
# latex_use_parts = False

# If true, show page references after internal links.
# latex_show_pagerefs = False

# If true, show URL addresses after external links.
# latex_show_urls = False

# Documents to append as an appendix to all manuals.
# latex_appendices = []

# If false, no module index is generated.
# latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'websauna', 'Websauna Documentation',
     [author], 1)
]

# If true, show URL addresses after external links.
# man_show_urls = False

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'Websauna', 'Websauna Documentation', author, 'Websauna', 'One line description of project.', 'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
# texinfo_appendices = []

# If false, no module index is generated.
# texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
# texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
# texinfo_no_detailmenu = False

# Example configuration for intersphinx: refer to the Python standard library.
# Looks for objects in external projects
intersphinx_mapping = {
    'colander': ('https://docs.pylonsproject.org/projects/colander/en/latest', None),
    'cookbook': ('https://docs.pylonsproject.org/projects/pyramid-cookbook/en/latest/', None),
    'deform': ('https://docs.pylonsproject.org/projects/deform/en/latest', None),
    'jinja2': ('https://docs.pylonsproject.org/projects/pyramid-jinja2/en/latest/', None),
    'pylonswebframework': ('https://docs.pylonsproject.org/projects/pylons-webframework/en/latest/', None),
    'python': ('https://docs.python.org/3', None),
    'splinter': ('http://splinter.readthedocs.io/en/latest/', None),
    'sqla': ('https://docs.sqlalchemy.org/en/latest', None),
    'tm': ('https://docs.pylonsproject.org/projects/pyramid_tm/en/latest/', None),
    'toolbar': ('https://docs.pylonsproject.org/projects/pyramid-debugtoolbar/en/latest', None),
    'tstring': ('https://docs.pylonsproject.org/projects/translationstring/en/latest', None),
    'tutorials': ('https://docs.pylonsproject.org/projects/pyramid-tutorials/en/latest/', None),
    'venusian': ('https://docs.pylonsproject.org/projects/venusian/en/latest', None),
    'webob': ('https://docs.pylonsproject.org/projects/webob/en/latest', None),
    'webtest': ('https://docs.pylonsproject.org/projects/webtest/en/latest/', None),
    'who': ('https://repozewho.readthedocs.io/en/latest/', None),
    'zcml': ('https://docs.pylonsproject.org/projects/pyramid-zcml/en/latest', None),
    'zcomponent': ('https://zopecomponent.readthedocs.io/en/latest/', None),
    "celery": ("http://docs.celeryproject.org/en/latest/", None),
}

# -- Options for Epub output ---------------------------------------------------
epub_theme = 'epub'

epub_theme_options = {
    'relbar1': False,
    'footer': False,
}

# Bibliographic Dublin Core info.
epub_title = 'Websauna Documentation, Version {0}'.format(release)
epub_author = author
epub_publisher = author
epub_copyright = '2015-{0}'.format(this_year)

# The language of the text. It defaults to the language option
# or en if the language is not set.
epub_language = 'en'

# The scheme of the identifier. Typical schemes are ISBN or URL.
epub_scheme = 'ISBN'

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
epub_identifier = 'https://websauna.org'

# A unique identification for the text.
epub_uid = epub_title

# A list of files that should not be packed into the epub file.
epub_exclude_files = []

# The depth of the table of contents in toc.ncx.
epub_tocdepth = 2
