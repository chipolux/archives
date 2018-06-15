# Compiles Package
from distutils.core import setup
import py2exe
import sys; sys.argv.append('py2exe')

py2exe_options = dict(
	compressed = True,
	#bundle_files = 1,
	excludes = ['doctest', 'pdb', 'unittest', 'difflib']
	)

setup(
    options = {'py2exe': py2exe_options},
    console = [{'script': "TextAdv1.py"}],
    zipfile = None,
)
