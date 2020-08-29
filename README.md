# Flask-xCaptcha

The new xCaptcha implementation for Flask without Flask-WTF.

Can also be used as standalone

Compatible with:

* Google ReCaptcha (default)
* hCaptcha
* Any other similarly configured captcha


---

## Install

    pip install flask-xcaptcha

# Usage

### Implementation view.py

    from flask import Flask
    from flask_xcaptcha import XCaptcha

    app = Flask(__name__)
    xcaptcha = XCaptcha(app=app)
    
    #or 
    
    xcaptcha = XCaptcha()
    xcaptcha.init_app(app)
    

### In your template: **{{ xcaptcha }}**

Inside of the form you want to protect, include the tag: **{{ xcaptcha }}**

It will insert the code automatically


    <form method="post" action="/submit">
        ... your field
        ... your field

        {{ xcaptcha }}

        [submit button]
    </form>


### Verify the captcha

In the view that's going to validate the captcha

    from flask import Flask
    from flask_xcaptcha import XCaptcha

    app = Flask(__name__)
    rcaptcha = XCaptcha(app=app)

    @route("/submit", methods=["POST"])
    def submit():

        if xcaptcha.verify():
            # SUCCESS
            pass
        else:
            # FAILED
            pass


## Api

**XCaptcha.__init__(app, site_key, secret_key, is_enabled=True)**

**XCaptcha.get_code()**

Returns the HTML code to implement. But you can use
**{{ xcaptcha }}** directly in your template

**XCaptcha.verfiy()**

Returns bool

## In Template

Just include **{{ xcaptcha }}** wherever you want to show the recaptcha


## Config

Flask-ReCaptcha is configured through the standard Flask config API.
These are the available options:

**XCAPTCHA_ENABLED**: Bool - True by default, when False it will bypass validation

**XCAPTCHA_SITE_KEY** : Public key

**XCAPTCHA_SECRET_KEY**: Private key

The following are **Optional** arguments.

**XCAPTCHA_THEME**: String - Theme can be 'light'(default) or 'dark'

**XCAPTCHA_TYPE**: String - Type of recaptcha can be 'image'(default) or 'audio'

**XCAPTCHA_SIZE**: String - Size of the image can be 'normal'(default) or 'compact'

**XCAPTCHA_TABINDEX**: Int - Tabindex of the widget can be used, if the page uses tabidex, to make navigation easier. Defaults to 0

    XCAPTCHA_ENABLED = True
    XCAPTCHA_SITE_KEY = ""
    XCAPTCHA_SECRET_KEY = ""
    XCAPTCHA_THEME = "dark"
    XCAPTCHA_TYPE = "image"
    XCAPTCHA_SIZE = "compact"
    XCAPTCHA_RTABINDEX = 10

---

(c) 2015 Mardix

