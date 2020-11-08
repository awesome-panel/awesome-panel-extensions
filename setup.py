"""Setup file for the Awesome Panel Extensions"""
from typing import List

import setuptools

# I only want to include a short README with a focus on the package
with open("README_PACKAGE.md", "r") as fh:
    long_description = fh.read()

install_requires = [
    "panel",
    "bokeh",
    "lxml",  # Required by the WebComponent
]

_recommended: List[str] = []

_tests = [
    "autoflake",
    "invoke",
    "isort",
    "jupyter-repo2docker",
    "mypy",
    "pylint>=2.6.0",
    "pytest",
    "pytest-cov",
    "rope",
    "twine",
]

_examples = [
    "notebook",
    "pandas-profiling",
    "matplotlib",
    "pandas",
    "seaborn",
    "holoviews",
    "hvplot",
    "plotly",
    "altair",
]

_doc: List[str] = []

extras_require = {
    "examples": _recommended + _examples,
    "tests": _tests,
    "recommended": _recommended,
    "doc": _recommended + _doc,
}

extras_require["all"] = sorted(set(sum(extras_require.values(), [])))

setuptools.setup(
    name="awesome-panel-extensions",
    version="20201102.1",
    description="A package of awesome Panel extensions. Provided by awesome-panel.org",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Marc Skov Madsen",
    author_email="marc.skov.madsen@gmail.com",
    platforms=["Windows", "Mac OS X", "Linux"],
    license="GPLv3",
    url="https://github.com/marcskovmadsen/awesome-panel-extensions",
    # My Project contains more folders/ packages but they should not be included
    packages=setuptools.find_packages(
        include=["awesome_panel_extensions", "awesome_panel_extensions.*"]
    ),
    include_package_data=True,
    classifiers=[
        # I would like to indicate that this package is a package for the Panel framework
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Financial and Insurance Industry",
        "Intended Audience :: Healthcare Industry",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Legal Industry",
        "Intended Audience :: Other Audience",
        "Intended Audience :: Science/Research",
        "Natural Language :: English",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Visualization",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Office/Business",
        "Topic :: Office/Business :: Financial",
        "Topic :: Software Development :: Libraries",
    ],
    python_requires=">=3.6",
    install_requires=install_requires,
    extras_require=extras_require,
    tests_require=extras_require["tests"],
)
