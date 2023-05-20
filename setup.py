from setuptools import setup

from cmdtools_helper import __version__

setup(
    name="cmdtools_helper",
    version=__version__,
    description="A collections of helper functions for the cmdtools library.",
    author="HugeBrain16",
    py_modules=["cmdtools_helper"],
    install_requires=["cmdtools-py"],
)
