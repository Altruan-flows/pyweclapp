"""Setup script for the pyweclapp package."""

from setuptools import find_packages, setup

try:
    with open("src/README.md", "r", encoding="utf-8") as f:
        LONG_DESCRIPTION = f.read()
except FileNotFoundError:
    LONG_DESCRIPTION = (
        "Provides methods, classes and classbuilders to interact with the Weclapp API"
    )

try:
    with open("requirements.txt", "r", encoding="utf-8") as f:
        REQUIRED = f.read().splitlines()
except FileNotFoundError:
    REQUIRED = [
        "requests>=2.28.2",
        "pydantic>=1.10.4",
        "jsonschema>=4.17.3",
        "pytz>=2022.7.1",
    ]

setup(
    name="pyweclapp",
    version="0.1.15",
    description="Provides methods, classes and classbuilders to interact with the Weclapp API",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/AltruanGmbH/pyweclapp",
    author="Altruan GmbH",
    author_email="admin@altruan.de",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    install_requires=REQUIRED,
    extras_require={
        "dev": ["twine>=4.0.2"],
    },
    python_requires=">=3.9",
)
