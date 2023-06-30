from setuptools import setup
import os

with open(os.path.join(os.path.dirname(__file__), "README.md"), encoding="utf-8") as f:
    readme = f.read()

setup(
    name="pipevcr",
    version="0.1.1",
    url="https://github.com/laktak/pipevcr",
    author="Christian Zangl",
    author_email="laktak@cdak.net",
    description="Record and play back pipes.",
    long_description=readme,
    long_description_content_type="text/markdown",
    packages=[],
    install_requires=[],
    scripts=["pipevcr"],
    py_modules=["pipevcr"],
)
