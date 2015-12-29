#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://blackhorus.github.io'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
DATE_FORMAT = {
    'en': '%m. %d, %Y'
 }
 
REVERSE_CATEGORY_ORDER = True
DEFAULT_CATEGORY = 'Uncategorized'


DELETE_OUTPUT_DIRECTORY = True

# Navigation sections and relative URL:
SECTIONS = [('Blog', 'index.html'),
            ('Archive', 'archives.html'),
            ('About', 'pages/about-me.html')]

DEFAULT_PAGINATION = 10
# Following items are often useful when publishing

DISQUS_SITENAME = "blackhorus"
#GOOGLE_ANALYTICS = ""

AUTHOR = u'Black Horus'
SITENAME = u'Blog'
TIMEZONE = "America/New_York"
LOCALE = 'en'
THEME = "../../pelican-themes/flasky"
DEFAULT_LANG = u'en'

MD_EXTENSIONS = ['fenced_code', 'codehilite(css_class=highlight)', 'extra']