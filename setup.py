import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="maptoplib", # Replace with your own username
    version="3.1.1",
    author="fulibacsi",
    author_email="fulibacsi@gmail.com",
    description="A forwarder lib for matplotlib",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fulibacsi/maptoplib",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPL v3.0",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)