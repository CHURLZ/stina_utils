import uuid
from setuptools import setup
import os
from pip.req import parse_requirements

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
reqs_file = os.path.join(BASE_DIR, 'requirements.txt')
install_reqs = parse_requirements(reqs_file, session=uuid.uuid1())

setup(
    name="stina_utils",
    version="0.1",
    author="Stina Labs @ Stena IT",
    author_email="carlos@stena.io",
    description=("Support utils for Stina project"),
    license="MIT",
    keywords="utils",
    install_requires=["Flask"],
    url="https://github.com/StenaTransformations/stina_utils",
    packages=['digest', 'data', 'templates'],
    include_package_data=True,
    package_data={'templates': ['*'], 'data': ['*']},
    long_description=read('README.md')
)
