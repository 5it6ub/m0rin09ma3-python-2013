#!/usr/bin/env python
""" Factorial project """
from setuptools import find_packages, setup

setup(name = 'test-pkg-upload',
    version = '0.1',
    description = "Factorial module.",
    long_description = "A test module for Kushal's book.",
    platforms = ["Linux"],
    author = "Shungoh Kaetsu",
    author_email = "shungoh.kaetsu@gmail.com",
    url = "http://www.example.com",
    license = "MIT",
    packages = find_packages()
)

