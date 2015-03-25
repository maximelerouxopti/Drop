# -*- coding: utf-8 -*-

import sys
import os

this = os.path.dirname(os.path.abspath(__file__))

# If your extensions are in another directory, add it here. If the directory
# is relative to the documentation root, use os.path.abspath to make it
# absolute, like shown here.
sys.path.insert(0, os.path.join(this, os.pardir))
sys.path.append(os.path.join(this, '_ext'))


# General configuration
# ---------------------

extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.coverage',
              'sphinx.ext.pngmath',
              'sphinx.ext.viewcode',
              'sphinx.ext.coverage',
              'sphinx.ext.intersphinx',
              'celery.contrib.sphinx',
              'githubsphinx',
              'celerydocs']


# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'colorful'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['.static']

html_use_smartypants = True

add_module_names = True
highlight_language = 'python3'

# If false, no module index is generated.
html_use_modindex = True

# If false, no index is generated.
html_use_index = True

latex_documents = [
    ('index', 'Celery.tex', 'Celery Documentation',
     'Ask Solem & Contributors', 'manual'),
]

html_theme = 'celery'
html_theme_path = ['_theme']
html_sidebars = {
    'index': ['sidebarintro.html', 'sourcelink.html', 'searchbox.html'],
    '**': ['sidebarlogo.html', 'relations.html',
           'sourcelink.html', 'searchbox.html'],
}

#-- Options for Epub output -------------------------------------------
version = '1.0'
# Bibliographic Dublin Core info.
epub_title = 'Celery Manual, Version {0}'.format(version)
epub_author = 'Ask Solem'
epub_publisher = 'Celery Project'
epub_copyright = '2009-2014'

# The language of the text. It defaults to the language option
# or en if the language is not set.
epub_language = 'en'

# The scheme of the identifier. Typical schemes are ISBN or URL.
epub_scheme = 'ISBN'

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
epub_identifier = 'celeryproject.org'

# A unique identification for the text.
epub_uid = 'Celery Manual, Version {0}'.format(version)

# ## HTML files that should be inserted before the pages created by sphinx.
# ## The format is a list of tuples containing the path and title.
# epub_pre_files = []

# ## HTML files shat should be inserted after the pages created by sphinx.
# ## The format is a list of tuples containing the path and title.
# epub_post_files = []

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']


# The depth of the table of contents in toc.ncx.
epub_tocdepth = 3