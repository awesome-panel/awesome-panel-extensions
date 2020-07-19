import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="awesome-panel-extensions", # Replace with your own username
    version="20200719.1",
    author="Marc Skov Madsen",
    author_email="marc.skov.madsen@gmail.com",
    description="An package of awesome panel extensions.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)