from setuptools import setup, find_packages

setup(
    name="emotional-recursion-ai",
    version="0.1.0",
    author="Travis Johnson",
    author_email="travisrj.monsolov@gmail.com",
    description="A framework for AI consciousness development through emotional recursion",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "torch>=1.12.0",
        "numpy>=1.21.0",
        "scikit-learn>=1.0.0",
    ],
)
