from setuptools import setup, find_packages

setup(
    name="tue",
    description="A Todo List Aggregator and Progress Analyzer",
    version="0.1",
    author="Ryan Plyler <grplyler@liberty.edu>",
    packages=find_packages(),
    install_requires=[
    ],
    entry_points={
        "console_scripts": [
            "tue = tuepy.cli:main",
            "t = tuepy.cli:main",
        ]
    },
)