import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python-squash",
    version="0.0.1",
    author="Vladimir Protasov",
    author_email="squash-pypi@eoranged.com",
    description="Superor Queue Dashboard",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/eoranged/squash",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
