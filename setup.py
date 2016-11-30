from setuptools import setup, find_packages

setup(
name = "neurotools",
description = ("A Python Toolbox for Statistics and Signal Processing (EEG, EDA, ECG, EMG...)."),
version = "0.0.1",
license = "MIT",
author = "Dominique Makowski",
author_email = "dom.makowski@gmail.com",
maintainer = "Dominique Makowski",
maintainer_email = "dom.makowski@gmail.com",
packages = find_packages(),
package_data = {},
install_requires = [
    'numpy>=1.11.0',
    'scipy>=0.10.0',
    'pandas>=0.18.0',
    'mne>=0.13.0',
    'nolds'],
dependency_links=[],
long_description = open('README.md').read(),
keywords = "python signal processing EEG EDA",
url = "https://github.com/neuropsychology/NeuroTools.py",
download_url = 'https://github.com/neuropsychology/NeuroTools.py/tarball/0.0.1',
test_suite='nose.collector',
tests_require=['nose'],
classifiers = [
	'Intended Audience :: Science/Research',
	'Intended Audience :: Developers',
	'Programming Language :: Python',
	'Topic :: Software Development',
	'Topic :: Scientific/Engineering',
	'Operating System :: Microsoft :: Windows',
	'Operating System :: Unix',
	'Operating System :: MacOS',
	'Programming Language :: Python :: 3.4',
	'Programming Language :: Python :: 3.5',
	'Programming Language :: Python :: 3.6']
)
