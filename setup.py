from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'Python Package for Openware Peatio Cryptocurrency Exchange & Accounting Software'
LONG_DESCRIPTION = 'A Python package that allows you to do API based operation on Peatio Cryptocurrency Exchange. This Package is based on following [API](https://www.openware.com/sdk/2.3/docs/peatio/api/peatio-user-api-v2.html) documentation. Peatio is core open-source accounting software for a cryptocurrency and digital asset exchange platform. The mission of Peatio is to facilitate asset base, accounting, and trading activities. It is built on Rails framework and designed for micro-services architecture, with external frontend and server components.'

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()
# Setting up
setup(
    name="Python_Peatio",
    version=VERSION,
    author="athenasaurav (Kumar Saurav)",
    author_email="<kumar@prescient-automation.com>",
    website = "https://prescient-automation.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['python-http-client'],
    keywords=['python', 'peatio', 'crypto', 'crypto currency', 'open source', 'exchanges', 'open source exchange', 'openware exchange'],
    classifiers=[
        "Development Status :: 1 - Deployment",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)