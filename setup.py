
from setuptools import setup, find_packages
import flask_xcaptcha

PACKAGE = flask_xcaptcha

setup(
    name=PACKAGE.__NAME__,
    version=PACKAGE.__version__,
    license=PACKAGE.__license__,
    author=PACKAGE.__author__,
    author_email='mardix@pylot.io',
    description="The new xCaptcha implementation for Flask without Flask-WTF",
    long_description=PACKAGE.__doc__,
    url='https://github.com/benjilev08/flask-recaptcha',
    download_url='https://github.com/benjilev08/flask-recaptcha/tarball/master',
    py_modules=['flask_xcaptcha'],
    include_package_data=True,
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
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    zip_safe=False
)
