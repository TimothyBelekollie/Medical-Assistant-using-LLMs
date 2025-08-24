from setuptools import find_packages, setup

setup(
    name="medical-assistant",
    version="0.1.0",
    author="Timothy Belekollie",
    author_email="belekollietimothy2@gmail.com",
    description="An AI-powered medical assistant project",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/TimothyBelekollie/medical-assistant",
    packages=find_packages(),
    install_requires=[
        # "numpy",
        # "flask",
    ],
    
)