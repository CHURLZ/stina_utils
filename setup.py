from setuptools import find_packages, setup

setup(name='stina_utils',
      version='0.1.0',
      description='Support utils for Stina',
      author='Ludvig Gee, Carl Berglund',
      author_email='ludvig.gee@stena.io',
      url='https://github.com/StenaTransformations/stina_utils',
      license='MIT',
      install_requires=['Flask'],
      packages=find_packages())
