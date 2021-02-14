
from setuptools import setup, find_packages
import flask_xcaptcha

PACKAGE = flask_xcaptcha

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name=PACKAGE.__NAME__,
    version=PACKAGE.__version__,
    license=PACKAGE.__license__,
    author=PACKAGE.__author__,
    author_email='max@maxlevine.co.uk',
    description="The new xCaptcha implementation for Flask without Flask-WTF",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/bmaximuml/flask-xcaptcha',
    download_url='https://github.com/bmaximuml/flask-xcaptcha/tarball/master',
    py_modules=['flask_xcaptcha'],
    include_package_data=True,
    packages=find_packages(),
    install_requires=[
        "flask",
        "requests"
    ],
    keywords=['flask', 'recaptcha', 'hcaptcha', 'xcaptcha', "validate"],
    platforms='any',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    zip_safe=False
)
