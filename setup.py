from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(name='django-modelmerge',
      version=version,
      description="Lazy signup for Django",
      long_description=open("README").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: BSD License"],
      keywords='django lazy signup app user',
      author='Dan Fairs',
      author_email='dan@fezconsulting.com',
      url='http://github.com/danfairs/django-modelmerge',
      license='BSD',
      packages=find_packages(exclude=['ez_setup']),
      package_data={
        'modelmerge': ['templates/modelmerge/*html'],
        '': ['*.txt', '*.rst'],
      },
      namespace_packages=[],
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools', 'Django'],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
