# Author: Hansheng Zhao <copyrighthero@gmail.com> (https://www.zhs.me)

# import required setup libraries
from setuptools import setup, find_packages
from codecs import open
from os import path

# import library for metadata
import seco

# project absolute directory
DIRECTORY = path.abspath(path.dirname(__file__))

# project readme file content
with open(
  path.join(DIRECTORY, 'README.rst'), encoding = 'UTF8'
) as file_descriptor:
  PROJECT_README = file_descriptor.read()

# project required dependencies
with open(
  path.join(DIRECTORY, 'requirements.txt'), encoding = 'UTF8'
) as file_descriptor:
  REQUIREMENTS = tuple(line for line in file_descriptor if line)

# project setup parameters
setup(
  name = 'SeCo',
  version = seco.__version__,
  description = 'Python data serialization and compression made easy.',
  long_description = PROJECT_README,
  url = 'https://www.github.com/copyrighthero/SeCo',
  download_url = 'https://www.github.com/copyrighthero/SeCo',
  author = seco.__author__,
  author_email = 'copyrighthero@gmail.com',
  license = seco.__license__,
  classifiers = (
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Intended Audience :: End Users/Desktop',
    'Intended Audience :: Information Technology',
    'Intended Audience :: Science/Research',
    'Intended Audience :: System Administrators',
    'License :: OSI Approved :: BSD License',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 3',
    'Topic :: Communications',
    'Topic :: Database',
    'Topic :: Internet',
    'Topic :: Software Development',
    'Topic :: System',
    'Topic :: Utilities'
  ),
  keywords = 'Data Serialization Compression Library',
  py_modules = ("seco", ),
  packages = find_packages(exclude = ()),
  install_requires = REQUIREMENTS,
  package_data = {},
  data_files = (),
  entry_points = {},
  project_urls = {
    'Source': 'https://www.github.com/copyrighthero/SeCo'
  }
)
