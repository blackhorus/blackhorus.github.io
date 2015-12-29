#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Black Horus'
SITENAME = u'Blog'
TIMEZONE = "America/New_York"
LOCALE = 'en'
THEME = "../../pelican-themes/flasky"
DEFAULT_LANG = u'en'

# Navigation sections and relative URL:
SECTIONS = [('Blog', 'index.html'),
			('Archive', 'archives.html'),
            ('About', 'pages/about-me.html')]

DEFAULT_PAGINATION = 10
DATE_FORMAT = {
    'en': '%m. %d, %Y'
 }
REVERSE_CATEGORY_ORDER = True
FEED_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'
DEFAULT_CATEGORY = 'Uncategorized'

MD_EXTENSIONS = ['fenced_code', 'codehilite(css_class=highlight)', 'extra']

