from distutils.core import setup

from mbz2nx import __version__ as version


metadata = {
    'name': 'mbz2nx',
    'description': 'Generates NetworkX databases populated from MusicBrainz databases',
    'version': version,
    'author': 'Corey Farwell',
    'author_email': 'coreyf@rwell.org',
    'maintainer': 'Corey Farwell',
    'maintainer_email': 'coreyf@rwell.org',
    'url': 'http://github.com/frewsxcv/mbz2nx',
    'license': 'http://www.gnu.org/licenses/gpl-3.0.html',
    'keywords': ['musicbrainz', 'networkx'],
    'packages': ['mbz2nx'],
    'classifiers': [
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Topic :: Multimedia :: Sound/Audio',
        'Topic :: Scientific/Engineering :: Information Analysis',
    ]
}

setup(**metadata)
