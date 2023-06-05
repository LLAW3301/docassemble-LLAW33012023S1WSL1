import os
import sys
from setuptools import setup, find_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')

def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.LLAW33012023S1WSL1',
      version='0.0.1',
      description=('A docassemble extension.'),
      long_description='# LegallyFit for Westside Community Lawyers\r\n\r\nThis application assists **WestSide Community Lawyers** and their clients to access relevant, non-legal resources specific to the clients needs. \r\nThe application filters a directory of services/applications based on the information provided by the client. It  provides a list of the most relevant applications based on the users selected hardship, location, gender, and Aboriginal or Torres Strait Islander identification.\r\n\r\n\r\n## Authors\r\n\r\n* Hannah Esmaeili, esma0019@flinders.edu.au \r\n* Rosa Lindon, lind0217@flinders.edu.au \r\n* Tyson Young, youn0440@flinders.edu.au \r\n* Richard Hancock, hanc0152@flinders.edu.au \r\n',
      long_description_content_type='text/markdown',
      author='Hannah Esmaeili',
      author_email='esma0019@flinders.edu.au',
      license='The MIT License (MIT)',
      url='https://docassemble.org',
      packages=find_packages(),
      namespace_packages=['docassemble'],
      install_requires=[],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/LLAW33012023S1WSL1/', package='docassemble.LLAW33012023S1WSL1'),
     )

