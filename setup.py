from setuptools import setup, find_packages

setup(
    name="super_init",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    author="Abhijeet Kumar",
    author_email="abhijeet151@gmail.com",
    description="A decorator for flexible inheritance in Python",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/csabhijeet/super-init",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)

