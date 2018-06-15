# setup.py
from distutils.core import setup
import py2exe
import sys; sys.argv.append('py2exe')

py2exe_options = dict(
	bundle_files = 1,
	includes = ["sip"],
	excludes = ['doctest', 'pdb', 'unittest', 'difflib'],
	compressed = True,
	)

setup(
	windows = [{'script': "map_viewer.py"}],
	options = {'py2exe': py2exe_options},
	zipfile = None,
	)
