# Flask-ReCaptcha

A simple recaptcha implementation for Flask without Flask-WTF.

---

## Install

    pip install flask-recaptcha

# Usage

### Implementation view.py

    from flask import Flask
    from flask_recaptcha import ReCaptcha

    app = Flask(__name__)
    recaptcha = ReCaptcha(app)

### In your template: **{{ recaptcha }}**

Inside of the form you want to protect, include the tag: **{{ recaptcha }}**

It will insert the code auutomatically


    <form method="post" action="/submit">
        ... your field
        ... your field

        {{ recaptcha }}

        [submit button]
    </form>


### Verify the captcha

In the view that's going to validate the captcha

    from flask import Flask
    from flask_recaptcha import ReCaptcha

    app = Flask(__name__)
    recaptcha = ReCaptcha(app)

    @route("/submit", methods=["POST"])
    def submit():

        if recaptcha.verify():
            # SUCCESS
            pass
        else:
            # FAILED
            pass


## Api

**reCaptcha.__init__(app, public_key, private_key)**

**reCaptcha.get_code()**

Returns the HTML code to implement. But you can use
**{{ recaptcha }}** directly in your template

**reCaptcha.verfiy()**

Returns bool

## In Template

Just include **{{ recaptcha }}** wherever you want to show the recaptcha


## Config

Flask-ReCaptcha is configured through the standard Flask config API.
These are the available options:

**RECAPTCHA_SITE_KEY** : Public key

**RECAPTCHA_SECRET_KEY**: Private key

    RECAPTCHA_SITE_KEY = ""
    RECAPTCHA_SECRET_KEY = ""

---

(c) 2015 Mardix

