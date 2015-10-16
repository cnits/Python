try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'Author': 'Cnit',
    'Url': 'pt.cnit',
    'Download_Url': 'download.pt.cnit/bingball-pt',
    'Author_Email': 'bingball@pt.cnit',
    'version': '0.1',
    'Install_Requires': ['nose'],
    'Packages': ['BingBallPT'],
    'Name': 'Bing-Ball-PT',
    'Description': 'Bing ball game project'
}

setup(**config)