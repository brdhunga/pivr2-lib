"""Python setup.py for pivr2_lib package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("pivr2_lib", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="pivr2_lib",
    version=read("pivr2_lib", "VERSION"),
    description="Awesome pivr2_lib created by brdhunga",
    url="https://github.com/brdhunga/pivr2-lib/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="brdhunga",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["pivr2_lib = pivr2_lib.__main__:main"]
    },
    extras_require={"test": read_requirements("requirements-test.txt")},
)
