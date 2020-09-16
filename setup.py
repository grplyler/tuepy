from setuptools import setup, find_packages

setup(
    name="tue",
    description="A Command-Line Task and Course Workload Manager written in Python (Great for College Students!)",
    version="0.1",
    author="Ryan Plyler <grplyler@liberty.edu>",
    packages=find_packages(),
    install_requires=[
    ],
    entry_points={
        "console_scripts": [
            "t = tuepy.cli:main",
        ]
    },
)