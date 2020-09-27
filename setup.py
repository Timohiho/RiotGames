import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="RiotGames", # Replace with your own username
    version="1.0.2",
    author="Timo Hirsch-Hoffmann",
    author_email="timohiho@yahoo.com",
    description="A Python wrapper for the Riot Games API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Timohiho/RiotGames",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: Microsoft :: Windows :: Windows 10"
    ],
    python_requires='>=3.8',
)
