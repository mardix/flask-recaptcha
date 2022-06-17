"""
The new xCaptcha implementation for Flask without Flask-WTF
"""

__NAME__ = "Flask-xCaptcha"
__version__ = "0.5.3"
__license__ = "MIT"
__author__ = "Max Levine"
__copyright__ = "(c) 2022 Max Levine"

try:
    from flask import request
    try:
        from jinja2 import Markup
    except ImportError:
        from markupsafe import Markup
    import requests
except ImportError:
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
    def __init__(self,
        app=None,
        site_key=None,
        secret_key=None,
        is_enabled=DEFAULTS.IS_ENABLED,
        theme=DEFAULTS.THEME,
        xtype=DEFAULTS.TYPE,
        size=DEFAULTS.SIZE,
        tabindex=DEFAULTS.TABINDEX,
        verify_url=DEFAULTS.VERIFY_URL,
        api_url=DEFAULTS.API_URL,
        div_class=DEFAULTS.DIV_CLASS,
        **kwargs
    ):
        if app is not None:
            self.site_key = app.config.get("XCAPTCHA_SITE_KEY", site_key)
            self.secret_key = app.config.get('XCAPTCHA_SECRET_KEY', secret_key)
            self.is_enabled = app.config.get("XCAPTCHA_ENABLED", is_enabled)
            self.theme = app.config.get("XCAPTCHA_THEME", theme)
            self.type = app.config.get("XCAPTCHA_TYPE", xtype)
            self.size = app.config.get("XCAPTCHA_SIZE", size)
            self.tabindex = app.config.get("XCAPTCHA_TABINDEX", tabindex)
            self.verify_url = app.config.get("XCAPTCHA_VERIFY_URL", verify_url)
            self.api_url = app.config.get("XCAPTCHA_API_URL", api_url)
            self.div_class = app.config.get("XCAPTCHA_DIV_CLASS", div_class)

            @app.context_processor
            def get_code():
                return dict(xcaptcha=Markup(self.get_code()))

        elif site_key is not None:
            self.site_key = site_key
            self.secret_key = secret_key
            self.is_enabled = is_enabled
            self.theme = theme
            self.type = xtype
            self.size = size
            self.tabindex = tabindex
            self.verify_url = verify_url
            self.api_url = api_url
            self.div_class = div_class

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
                "response": response or request.form.get('{}-response'.format(self.div_class)),
                "remoteip": remote_ip or request.remote_addr
            }

            r = requests.get(self.verify_url, params=data)
            return r.json()["success"] if r.status_code == 200 else False
        return True

