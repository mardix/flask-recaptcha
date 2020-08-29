# Flask-xCaptcha

The new xCaptcha implementation for Flask without Flask-WTF.

Can also be used as standalone

Compatible with:

* Google ReCaptcha (default)
* hCaptcha
* Any other similarly configured captcha

This project was forked from [Mardix's Flask-ReCaptcha](https://github.com/mardix/flask-recaptcha) project

---

## Install

`pip install flask-xcaptcha`

## Usage

### Minimal Implementation

#### Google ReCaptcha (default)

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

#### hCaptcha

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

## Api

### XCaptcha.__init__(app, site_key, secret_key, is_enabled=True)

### XCaptcha.get_code()

Returns the HTML code to implement. But you can use
`{{ xcaptcha }}` directly in your template

### XCaptcha.verfiy()

Returns bool

## In Template

Just include `{{ xcaptcha }}` wherever you want to show the recaptcha

(c) 2020 benjilev08
