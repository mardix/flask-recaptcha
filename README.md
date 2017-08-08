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

The following are **Optional** arguments.

**RECAPTCHA_THEME**: String - Theme can be 'light'(default) or 'dark'

**RECAPTCHA_TYPE**: String - Type of recaptcha can be 'image'(default) or 'audio'

**RECAPTCHA_SIZE**: String - Size of the image can be 'normal'(default) or 'compact'

**RECAPTCHA_TABINDEX**: Int - Tabindex of the widget can be used, if the page uses tabidex, to make navigation easier. Defaults to 0

**RECAPTCHA_LANGUAGE**: String - You can choose one from the [languages available](https://developers.google.com/recaptcha/docs/language). Default is 'en'

**RECAPTCHA_ASYNC_DEFER**: Bool - Set scripts opcions async and defer available. Default is True

    RECAPTCHA_ENABLED = True
    RECAPTCHA_SITE_KEY = ""
    RECAPTCHA_SECRET_KEY = ""
    RECAPTCHA_THEME = "dark"
    RECAPTCHA_TYPE = "image"
    RECAPTCHA_SIZE = "compact"
    RECAPTCHA_TABINDEX = 10
    RECAPTCHA_LANGUAGE = "es"
    RECAPTCHA_ASYNC_DEFER = False

---

(c) 2015 Mardix

