# Flask-ReCaptcha

The new Google ReCaptcha implementation for Flask without Flask-WTF.

Can also be used as standalone

---

## Install

    pip install flask-recaptcha

# Usage

### Implementation view.py

    from flask import Flask
    from flask_recaptcha import ReCaptcha

    app = Flask(__name__)
    recaptcha = ReCaptcha(app=app)
    
    #or 
    
    recaptcha = Recaptcha()
    recaptcha.init_app(app)
    

### In your template: **{{ recaptcha }}**

Inside of the form you want to protect, include the tag: **{{ recaptcha }}**

It will insert the code automatically


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
    recaptcha = ReCaptcha(app=app)

    @route("/submit", methods=["POST"])
    def submit():

        if recaptcha.verify():
            # SUCCESS
            pass
        else:
            # FAILED
            pass


## Api

**reCaptcha.__init__(app, site_key, secret_key, is_enabled=True)**

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

**RECAPTCHA_ENABLED**: Bool - True by default, when False it will bypass validation

**RECAPTCHA_SITE_KEY** : Public key

**RECAPTCHA_SECRET_KEY**: Private key

    RECAPTCHA_ENABLED = True
    RECAPTCHA_SITE_KEY = ""
    RECAPTCHA_SECRET_KEY = ""

---

(c) 2015 Mardix

