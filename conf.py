 -- Options for Epub output -------------------------------------------
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