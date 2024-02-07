from setuptools import setup, find_packages

setup(
    name="slowrest",
    version="1.0",
    install_requires=[
        "flask~=3.0.0",
        "flask_restful~=0.3.10",
        "flask_caching~=2.1.0",
        "click~=8.1.7",
        "oracledb~=2.0.0",
        "wheel~=0.42.0",
    ],
)
