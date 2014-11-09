# Flask-reCaptcha

A simple recaptcha implementation for Flask without Flask-WTF.

Can also be used without Flask

---

## Install

    pip install flask-recaptcha

# Usage

### Implementation view.py

    from flask import Flask
    from flask.ext.recaptcha import reCaptcha

    app = Flask(__name__)
    recaptcha = reCaptcha()

    recaptcha.init_app(app)

### In your template: **{{recaptcha}}**

Inside of the form you want to protect, include the tag: **{{recaptcha}}**

It will insert the code auutomatically


    <form method="post" action="/submit">
        ... your field
        ... your field

        {{recaptcha}}

        [submit button]
    </form>


### Verify the captcha

In the view that's going to validate the captcha

    from flask import Flask, fl
    from flask.ext.recaptcha import reCaptcha

    app = Flask(__name__)
    recaptcha = reCaptcha()

    recaptcha.init_app(app)

    @route("/submit", methods=["POST])
    def submit():

        if not recaptcha.validate():
            # recaptcha failed. Show error message
            pass

        else:
            # continue with your process
            pass


## Api

**reCaptcha.__init__(public_key, private_key)**

**reCaptcha.get_code()**

Returns the HTML code to implement. But you can use
**{{recaptcha}}** directly in your template

**reCaptcha.validate()**

Returns bool

## In Template

Just include **{{recaptcha}}** wherever you want to show the recaptcha


## Config

Flask-reCaptcha is configured through the standard Flask config API.
These are the available options:

**RECAPTCHA_PUBLIC_KEY** : Public key

**RECAPTCHA_PROVATE_KEY**: Private key

**RECAPTCHA_USE_SSL**: To use SSL


    RECAPTCHA_PUBLIC_KEY = ""
    RECAPTCHA_PRIVATE_KEY = ""
    RECAPTCHA_USE_SSL = False

---

(c) 2014 Mardix

