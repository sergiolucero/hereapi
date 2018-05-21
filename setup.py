import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hereapi",
    version="0.0.1",
    author="Sergio Lucero",
    author_email="sergiolucero@gmail.com",
    description="A small example package",
    long_description=long_description,
	install_requires=['requests','folium'],
    long_description_content_type="text/markdown",
    url="https://github.com/sergiolucero/hereapi",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)