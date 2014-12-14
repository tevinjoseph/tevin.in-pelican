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
COVER_IMG_URL = 'https://scontent-a-lga.xx.fbcdn.net/hphotos-xpa1/v/t1.0-9/1526199_748445591869475_8342512785994427492_n.jpg?oh=f6d6dd2b21546315136bf9b2499466a1&oe=55446D5D'
PROFILE_IMAGE_URL = 'https://fbcdn-sphotos-c-a.akamaihd.net/hphotos-ak-xpf1/v/t1.0-9/10157186_658152540898781_7445448101037810379_n.jpg?oh=7bbd0644a226962d6015b69141cbc4ab&oe=550281BC&__gda__=1427357654_0634af07603f4a7d905940f8775c24c9'

DEFAULT_PAGINATION = 10
DISQUS_SITENAME ='tevinjosephko'
RELATIVE_URLS = True
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['gravatar']
