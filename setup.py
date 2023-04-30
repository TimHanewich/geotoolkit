from distutils.core import setup
import setuptools

with open("readme.md", "r") as f:
    long_desc:str = f.read()

setup(name='geotoolkit',
    version='0.1.0',
    description='Peforming calculations with geographic points',
    long_description=long_desc,
    author='Tim Hanewich',
    url='https://github.com/TimHanewich/geotoolkit',
    packages=setuptools.find_packages()
    )