from setuptools import setup
__version__ = '0.0.4'

setup(
    name="pymusiccast",
    packages=["pymusiccast"],
    version=__version__,
    description="",
    author="Jan Almeroth",
    author_email="jan+pymusiccast@almeroth.com",
    url="https://github.com/jalmeroth/pymusiccast",
    download_url="https://github.com/jalmeroth/pymusiccast/tarball/" + __version__,
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Topic :: Home Automation"
    ],
    install_requires=['requests>=2.14.2']
)
