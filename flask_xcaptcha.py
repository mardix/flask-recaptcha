"""
The new xCaptcha implementation for Flask without Flask-WTF
"""

__NAME__ = "Flask-xCaptcha"
__version__ = "0.5.0"
__license__ = "MIT"
__author__ = "Mardix, benjilev08"
__copyright__ = "(c) 2020 Mardix, benjilev08"

try:
    from flask import request
    from jinja2 import Markup
    import requests
except ImportError as ex:
    print("Missing dependencies")


class DEFAULTS(object):
    IS_ENABLED = True
    THEME = "light"
    TYPE = "image"
    SIZE = "normal"
    TABINDEX = 0
    VERIFY_URL = "https://www.google.com/recaptcha/api/siteverify"
    API_URL = "//www.google.com/recaptcha/api.js"
    DIV_CLASS = "g-recaptcha"


class XCaptcha(object):

    site_key = None
    secret_key = None
    is_enabled = False

    def __init__(self, app=None, site_key=None, secret_key=None, is_enabled=True, **kwargs):
        if app is not None:
            self.site_key = app.config.get("XCAPTCHA_SITE_KEY") if site_key is None else site_key
            self.secret_key = app.config.get('XCAPTCHA_SECRET_KEY') if secret_key is None else secret_key
            self.is_enabled = app.config.get("XCAPTCHA_ENABLED", DEFAULTS.IS_ENABLED) if is_enabled is None else is_enabled
            self.theme = app.config.get("XCAPTCHA_THEME", DEFAULTS.THEME) if kwargs.get('theme') is None else kwargs.get('theme')
            self.type = app.config.get("XCAPTCHA_TYPE", DEFAULTS.TYPE) if kwargs.get('type') is None else kwargs.get('type')
            self.size = app.config.get("XCAPTCHA_SIZE", DEFAULTS.SIZE) if kwargs.get('size') is None else kwargs.get('size')
            self.tabindex = app.config.get("XCAPTCHA_TABINDEX", DEFAULTS.TABINDEX) if kwargs.get('tabindex') is None else kwargs.get('tabindex')
            self.verify_url = app.config.get("XCAPTCHA_VERIFY_URL", DEFAULTS.VERIFY_URL) if kwargs.get('verify_url') is None else kwargs.get('verify_url')
            self.api_url = app.config.get("XCAPTCHA_API_URL", DEFAULTS.API_URL) if kwargs.get('api_url') is None else kwargs.get('api_url')
            self.div_class = app.config.get("XCAPTCHA_DIV_CLASS", DEFAULTS.DIV_CLASS) if kwargs.get('div_class') is None else kwargs.get('div_class')

        elif site_key is not None:
            self.site_key = site_key
            self.secret_key = secret_key
            self.is_enabled = is_enabled
            self.theme = kwargs.get('theme', DEFAULTS.THEME)
            self.type = kwargs.get('type', DEFAULTS.TYPE)
            self.size = kwargs.get('size', DEFAULTS.SIZE)
            self.tabindex = kwargs.get('tabindex', DEFAULTS.TABINDEX)
            self.verify_url = kwargs.get('verify_url', DEFAULTS.VERIFY_URL)
            self.api_url = kwargs.get('api_url', DEFAULTS.API_URL)
            self.div_class = kwargs.get('div_class', DEFAULTS.DIV_CLASS)

        @app.context_processor
        def get_code():
            return dict(xcaptcha=Markup(self.get_code()))

    def get_code(self):
        """
        Returns the new XCaptcha code
        :return:
        """
        return "" if not self.is_enabled else ("""
        <script src='{API_URL}'></script>
        <div class="{DIV_CLASS}" data-sitekey="{SITE_KEY}" data-theme="{THEME}" data-type="{TYPE}" data-size="{SIZE}"\
         data-tabindex="{TABINDEX}"></div>
        """.format(
            DIV_CLASS=self.div_class,
            API_URL=self.api_url,
            SITE_KEY=self.site_key,
            THEME=self.theme,
            TYPE=self.type,
            SIZE=self.size,
            TABINDEX=self.tabindex
            )
        )

    def verify(self, response=None, remote_ip=None):
        if self.is_enabled:
            data = {
                "secret": self.secret_key,
                "response": response or request.form.get(f'{self.div_class}-response'),
                "remoteip": remote_ip or request.environ.get('REMOTE_ADDR')
            }

            r = requests.get(self.verify_url, params=data)
            return r.json()["success"] if r.status_code == 200 else False
        return True
