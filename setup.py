
from setuptools import setup, find_packages
import flask_recaptcha

PACKAGE = flask_recaptcha

setup(
    name=PACKAGE.__NAME__,
    version=PACKAGE.__version__,
    license=PACKAGE.__license__,
    author=PACKAGE.__author__,
    author_email='mardix@github.com',
    description="The new Google ReCaptcha implementation for Flask without Flask-WTF",
    long_description=PACKAGE.__doc__,
    url='http://github.com/mardix/flask-recaptcha/',
    download_url='http://github.com/mardix/flask-recaptcha/tarball/master',
    py_modules=['flask_recaptcha'],
    include_package_data=True,
    install_requires=[
        "flask",
        "requests"
    ],
    keywords=['flask', 'recaptcha', "validate"],
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
