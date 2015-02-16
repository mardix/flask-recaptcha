"""
The new Google ReCaptcha implementation for Flask without Flask-WTF
"""

__NAME__ = "Flask-ReCaptcha"
__version__ = "0.3"
__license__ = "MIT"
__author__ = "Mardix"
__copyright__ = "(c) 2015 Mardix"

try:
    from flask import request
    from jinja2 import Markup
    import requests
except ImportError as ex:
    print("Missing dependencies")

class ReCaptcha(object):

    VERIFY_URL = "https://www.google.com/recaptcha/api/siteverify"
    site_key = None
    secret_key = None

    def __init__(self, app=None, site_key=None, secret_key=None):
        if app or site_key:
            self.init_app(app=app, site_key=site_key, secret_key=secret_key)

    def init_app(self, app=None, site_key=None, secret_key=None):
        self.site_key = site_key or app.config.get("RECAPTCHA_SITE_KEY")
        self.secret_key = secret_key or app.config.get("RECAPTCHA_SECRET_KEY")

        @app.context_processor
        def get_code():
            return dict(recaptcha=Markup(self.get_code()))

    def get_code(self):
        """
        Returns the new ReCaptcha code
        :return:
        """
        return """
        <script src='//www.google.com/recaptcha/api.js'></script>
        <div class="g-recaptcha" data-sitekey="{SITE_KEY}"></div>
        """.format(SITE_KEY=self.site_key)

    def verify(self, response=None, remote_ip=None):
        data = {
            "secret": self.secret_key,
            "response": response or request.form.get('g-recaptcha-response'),
            "remoteip": remote_ip or request.environ.get('REMOTE_ADDR')
        }

        r = requests.get(self.VERIFY_URL, params=data)
        if r.status_code == 200:
            return r.json()["success"]
        else:
            return False
