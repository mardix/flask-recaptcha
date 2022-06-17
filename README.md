# Flask-xCaptcha

[![Build Status](https://app.travis-ci.com/bmaximuml/flask-xcaptcha.svg?branch=master)](https://app.travis-ci.com/bmaximuml/flask-xcaptcha)

The new xCaptcha implementation for Flask without Flask-WTF.

Can also be used as standalone

Compatible with:

* Google ReCaptcha (default)
* hCaptcha
* Any other similarly configured captcha

This project was forked from [Mardix's Flask-ReCaptcha](https://github.com/mardix/flask-recaptcha) project

---

## Installation

`pip install flask-xcaptcha`

## Usage - Minimal Implementation

### Google ReCaptcha - Using app variable

```python
from flask import Flask
from flask_xcaptcha import XCaptcha

app = Flask(__name__)
app.config.update(
    XCAPTCHA_SITE_KEY=#<your_site_key>,
    XCAPTCHA_SECRET_KEY=#<your_secret_key>
)
xcaptcha = XCaptcha(app=app)
```

### Google ReCaptcha - Without app variable

```python
from flask_xcaptcha import XCaptcha

xcaptcha = XCaptcha(
    site_key=#<your_site_key>,
    secret_key=#<your_secret_key>
)
```

### hCaptcha - Using app variable

```python
from flask import Flask
from flask_xcaptcha import XCaptcha

app = Flask(__name__)
app.config.update(
    XCAPTCHA_SITE_KEY=#<your_site_key>,
    XCAPTCHA_SECRET_KEY=#<your_secret_key>,
    XCAPTCHA_VERIFY_URL=https://hcaptcha.com/siteverify,
    XCAPTCHA_API_URL=https://hcaptcha.com/1/api.js,
    XCAPTCHA_DIV_CLASS=h-captcha
)
xcaptcha = XCaptcha(app=app)
```

### hCaptcha - Without app variable

```python
from flask_xcaptcha import XCaptcha

xcaptcha = XCaptcha(
    site_key=#<your_site_key>,
    secret_key=#<your_secret_key>,
    verify_url=https://hcaptcha.com/siteverify,
    api_url=https://hcaptcha.com/1/api.js,
    div_class=h-captcha
)
```

### App Config Variables

Flask-xCaptcha is configured through the standard Flask config API.
Add these to your app config as shown above to further configure your xCaptcha

Variable            | Description | Allowed Values | Default | Required?
---                 | ---         | ---            | ---     | ---
XCAPTCHA_SITE_KEY   | Site key provided by xCaptcha service | Your site key | | Required
XCAPTCHA_SECRET_KEY | Secret key provided by xCaptcha service | Your secret key | | Required
XCAPTCHA_ENABLED    | Enable verification. If false, verification will be disabled | True / False | True | Optional
XCAPTCHA_THEME      | Theme for the xCaptcha element | light / dark (service dependent) | "light" | Optional
XCAPTCHA_TYPE       | Type of xCaptcha | service dependent | "image" | Optional
XCAPTCHA_SIZE       | Size of xCaptcha | normal / compact (service dependent) | "normal" | Optional
XCAPTCHA_TABINDEX   | Set the tabindex of the widget and popup | integer | 0 | Optional
XCAPTCHA_VERIFY_URL | The URL to verify the filled in xCaptcha at | URL | "https://www.google.com/recaptcha/api/siteverify" | Optional
XCAPTCHA_API_URL    | The URL of the xCaptcha API JS script | URL | "//www.google.com/recaptcha/api.js" | Optional
XCAPTCHA_DIV_CLASS  | The class of the div element surrounding the xCaptcha | string | "g-recaptcha" | Optional

### In your template: `{{ xcaptcha }}`

Inside of the form you want to protect, include the tag: `{{ xcaptcha }}`

It will insert the code automatically

```html
<form method="post" action="/submit">
    ... your field
    ... your field

    {{ xcaptcha }}

    [submit button]
</form>
```

### Verify the captcha

In the view that's going to validate the captcha

```python
from flask import Flask
from flask_xcaptcha import XCaptcha

app = Flask(__name__)
app.config.update(
    XCAPTCHA_SITE_KEY=#<your_site_key>,
    XCAPTCHA_SECRET_KEY=#<your_secret_key>
)
xcaptcha = XCaptcha(app=app)

@route("/submit", methods=["POST"])
def submit():

    if xcaptcha.verify():
        # SUCCESS
        pass
    else:
        # FAILED
        pass
```

## API

### XCaptcha.__init__(app=None, site_key=None, secret_key=None, is_enabled=True, theme="light", xtype="image", size="normal", tabindex=0, verify_url="https://www.google.com/recaptcha/api/siteverify", api_url="//www.google.com/recaptcha/api.js", div_class="g-recaptcha",**kwargs)

Initialises the XCaptcha using values set in the app config (if an app is supplied), and otherwise using directly passed arguments

### XCaptcha.get_code()

Returns the HTML code to replace `{{ xcaptcha }}` with.

### XCaptcha.verify()

Returns a bool indicating whether or not the xCaptcha was successfully completed

## `{{ xcaptcha }}`

This will insert an HTML div element containing the captcha into a Jinja2 template

(c) 2022 Max Levine
