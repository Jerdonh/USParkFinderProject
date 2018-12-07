from setuptools import setup

setup(name='US-Park-Finder', # the package/module name
      version='1.0',
      author='Jerdon Helgeson', 
      author_email='jerdonhelgeson@hotmail.com', 
      py_modules=[ 'FlaskPage','Weather','Conversions','Importer','PARKSMODEL' ], # modules in the package 
      )
