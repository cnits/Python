try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'author': 'cnit',
    'url': 'http://github.com/cnits',
    'author_email': 'bingball@pt.cnit',
    'version': '1.0',
    'install_requires': ['Python >= 2.7', 'Tkinter'],
    'packages': ['BingBallGame.BingBall'],
    'name': 'Bing-Ball-Game',
    'description': 'Bing ball game project'
}

setup(**config)
