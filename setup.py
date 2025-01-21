from setuptools import find_packages, setup

try:
    with open("src/README.md", "r") as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = "Provides methods, classes and classbuilders to integrate with the Weclapp API"
    
    
try:
    with open('requirements.txt') as f:
        required = f.read().splitlines()
except FileNotFoundError:
    required = ["requests>=2.28.2",
                "pydantic>=1.10.4",
                "jsonschema>=4.17.3",
                # "pymupdf>=1.21.1",
                "pytz>=2022.7.1"]

setup(
    name="pyWeclapp",
    version="0.0.7",
    description="Provides methods, classes and classbuilders to integrate with the Weclapp API",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AltruanGmbH/weclappFunctions",
    author="Altruan GmbH",
    author_email="jakob.goesswald@altruan.de",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    install_requires=required,
    extras_require={
        "dev": ["twine>=4.0.2"],
    },
    python_requires=">=3.9",
)