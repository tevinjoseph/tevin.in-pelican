#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Tevin Joseph K O'
SITENAME = u"Tevin's Views"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Calcutta'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('github', 'https://github.com/tevinjoseph'),
		   ('twitter-square', 'https://twitter.com/TevinJosephKO'),
          ('facebook-square', 'https://www.facebook.com/tevin.joseph.92'),)

THEME ='themes/pure' 
COVER_IMG_URL = 'https://scontent-a-lax.xx.fbcdn.net/hphotos-xaf1/v/t1.0-9/426744_521682301212473_788212376_n.jpg?oh=9a39ea0358dc079f831f9c57d6392ffe&oe=5509FA37'
PROFILE_IMAGE_URL = 'https://fbcdn-sphotos-c-a.akamaihd.net/hphotos-ak-xpf1/v/t1.0-9/10157186_658152540898781_7445448101037810379_n.jpg?oh=7bbd0644a226962d6015b69141cbc4ab&oe=550281BC&__gda__=1427357654_0634af07603f4a7d905940f8775c24c9'

DEFAULT_PAGINATION = 10
DISQUS_SITENAME ='tevinjosephko'
GOOGLE_ANALYTICS = 'UA-57981880-1'
RELATIVE_URLS = True
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['gravatar']
