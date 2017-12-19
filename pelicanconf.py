#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Nick Hand'
SITEURL = 'http://localhost:8000'
SITENAME = "Offhand Remarks"
SITETITLE = AUTHOR
SITESUBTITLE = 'Astrophysics PhD, Aspiring Data Scientist'
SITEDESCRIPTION = '%s\'s Thoughts and Writings' % AUTHOR
SITELOGO = '/images/profile.jpg'
FAVICON = '/images/favicon.ico'
BROWSER_COLOR = '#333333'


AUTHOR = 'Nick Hand'
SITENAME = 'Offhand Remarks'
SITEURL = ''
PATH = 'content'
TIMEZONE = 'America/New_York'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

SOCIAL = (('linkedin', 'https://br.linkedin.com/in/nickhand1/en'),
          ('github', 'https://github.com/nickhand'),
          ('twitter', 'https://twitter.com/nicholashand'),)

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
HOME_HIDE_TAGS = False

MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),
             ('Sitemap', '/sitemap.xml'),)

LINKS = (('About me', '../index.html#page-welcome'),
)

CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}

COPYRIGHT_YEAR = 2017

ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

PLUGIN_PATHS = ['./blog/plugins/pelican-plugins', './blog/plugins/']
PLUGINS = [
    'i18n_subsites',
    'ipynb.liquid',  # for embedding notebooks
    'liquid_tags.img',  # embedding images
    'liquid_tags.video',  # embedding videos
    'liquid_tags.include_code',  # including code blocks
    'liquid_tags.literal'
]

IGNORE_FILES = ['.ipynb_checkpoints']

THEME = './blog/pelican-themes/Flex'

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

# for liquid tags
CODE_DIR = 'downloads/code'
NOTEBOOK_DIR = 'downloads/notebooks'

DEFAULT_PAGINATION = 10

ENABLE_MATHJAX = True

STATIC_PATHS = ['images', 'figures', 'videos', 'downloads', 'favicon.ico']

# DISPLAY_CATEGORIES_ON_MENU = False
# DISPLAY_PAGES_ON_MENU = False
#
# MENUITEMS = (
#     ('About', '../index.html#page-profile'),
#     ('Vita', '../cv/cv.pdf')
#     )

# SHOW_ARCHIVES = True
# SHOW_FEED = False  # Need to address large feeds

RELATIVE_URLS = True
