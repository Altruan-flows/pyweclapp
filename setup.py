from setuptools import find_packages, setup

with open("src/README.md", "r") as f:
    long_description = f.read()

setup(
    name="pyWeclapp",
    version="0.0.1",
    description="Provides methods, classes and classbuildes to integrate with th eWeclapp API",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AltruanGmbH/weclappFunctions",
    author="Altruan gmbh",
    author_email="jakob.goesswald@altruan.de",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    install_requires=["urllib3<2.0",
                      "requests>=2.28.2",
                      "pydantic>=1.10.4",
                      "jsonschema>=4.17.3",
                      # "pymupdf>=1.21.1",
                      "pytz>=2022.7.1"],
    extras_require={
        "dev": ["twine>=4.0.2"],
    },
    python_requires=">=3.9",
)