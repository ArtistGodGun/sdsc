from setuptools import setup, find_packages

setup(
    name="sdsc",
    version="0.1.0",
    description="SingleDrumSourceClassification (Classes : 10 or 16)",
    author="ArtistGodGun",
    author_email="artistgodgun@gmail.com",
    packages=find_packages(),
    package_data={
      'sdsc' : ['*.pth']
    },
    install_requires=[
        "argparse",
        "torch",
        "torchaudio",
        "numpy"
    ],
    entry_points={
        "console_scripts": [
            "sdsc=sdsc.main:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Natural Language :: Korean",
        "Topic :: Multimedia :: Sound/Audio",
        "Topic :: Multimedia :: Sound/Audio :: Analysis"
    ],
)
