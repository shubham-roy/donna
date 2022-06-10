from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()  # path to project root directory

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="donna",
    version="0.0.1",
    description="A CLI tool to work for you when you are with your PC.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Shubham Roy",
    packages=find_packages(),
    python_requires=">=3.10, <4",
    install_requires=[
        "click==8.1.3",
        "loguru==0.6.0",
        "Pillow==9.1.1",
        "PyAutoGUI==0.9.53",
    ],
    entry_points={
        "console_scripts": [
            "donna=donna.cli:entry_point",
        ],
    },
)
