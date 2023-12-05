from setuptools import find_packages
from setuptools import setup

p = find_packages()

setup(
    name="game",
    version="0.0.0",
    description=(
        """Implementation of a Pokemon-like game for fun and training."""
    ),
    license="MIT",
    url="https://github.com/manuhuth/game",
    author="manuhuth",
    author_email="manuel.huth@yahoo.com",
    packages=p,
    zip_safe=False,
    package_data={"utilities": []},
    include_package_data=True,
)
