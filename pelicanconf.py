#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Susheng'
SITENAME = u'Susheng'
SITEURL = ''

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('About', '/about-me.html'),
          ('Posts', '/'),
          ('Email', 'mailto:adityz16@gmail.com'),)
'''
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)
'''

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = 'pelican-svbhack'
DISQUS_SITENAME = 'susheng'
PLUGIN_PATH = 'pelican-plugins'
