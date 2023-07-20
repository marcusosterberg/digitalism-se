AUTHOR = 'Redaktion'
SITENAME = 'Digitalism'
SITEURL = 'https://digitalism.se'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'sv'
THEME = 'theme-pico'

PLUGIN_PATHS = ['plugins']
PLUGINS = ['sitemap']

SITEMAP = {
    'format': 'xml'
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'rss.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 20

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True