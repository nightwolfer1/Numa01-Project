# Denna fil är endast till för att det ska gå att installera hehemaker.py.
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_descritiption = fh.read()

setup(
    name='haar_wavelets',
    version='0.0.1b',
    author=['Carl Henrik \"CH\" Dahmén', 'Daniel Nilsson', 
    'Daniel Levin', 'Emil Jonathan Eriksson'],
    description='',
    long_description=long_descritiption,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/ginger51011/numa01-projekt",
    packages=find_packages(),
    entry_points={  # Tells python what to run
        "console_scripts": [
            "hwnuma = haar_wavelets.__main__:main"   # Name of console script
        ]
    },
    python_requires=">3.0.0",
    install_requires=[      # So that pip also installs required packages
        "scipy",
        "numpy",
        "scikit-image", # For imread and imsave
    ],
)
