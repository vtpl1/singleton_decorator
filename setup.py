#!/usr/bin/env python3

from setuptools import setup, find_packages
import singleton_decorator

setup(
    name="singleton-decorator",
    version=singleton_decorator.__version__,
    fullname="Singleton Decorator with key",
    description="A testable singleton decorator with key",
    author="Monotosh Das",
    author_email="monotosh.das@videonetics.com.com",
    keywords="singleton decorator unittest",
    long_description=open("README.rst").read(),
    url="https://github.com/vtpl1/singleton_decorator",
    license="GPLv3",
    packages=find_packages(exclude=["*.tests", "tests"]),
)
