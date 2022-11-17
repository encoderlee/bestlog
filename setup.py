import setuptools

with open("README.md", "r") as file:
    description = file.read()
    file.close()

setuptools.setup(
    name="bestlog",
    version="1.0.0",
    author="encoderlee",
    author_email="encoderlee@gmail.com",
    description="a simple python logger that logs to file and stdout",
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://github.com/encoderlee/bestlog",
    packages=["bestlog"],
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
