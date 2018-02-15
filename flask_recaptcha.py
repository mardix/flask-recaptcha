"""
The new Google ReCaptcha implementation for Flask without Flask-WTF
Can be used as standalone
"""

__NAME__ = "Flask-ReCaptcha"
__version__ = "0.4.2"
__license__ = "MIT"
__author__ = "Mardix"
__copyright__ = "(c) 2015 Mardix"

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
    INVISIBLE = "invisible"
    ELEMENT_ID = "id_captcha"


class ReCaptcha(object):

    VERIFY_URL = "https://www.google.com/recaptcha/api/siteverify"
    site_key = None
    secret_key = None
    is_enabled = False

    def __init__(self, app=None, site_key=None, secret_key=None, is_enabled=True, **kwargs):
        if site_key:
            self.site_key = site_key
            self.secret_key = secret_key
            self.is_enabled = is_enabled
            self.theme = kwargs.get('theme', DEFAULTS.THEME)
            self.type = kwargs.get('type', DEFAULTS.TYPE)
            self.size = kwargs.get('size', DEFAULTS.SIZE)
            self.tabindex = kwargs.get('tabindex', DEFAULTS.TABINDEX)
            self.element_id = kwargs.get('element_id', DEFAULTS.ELEMENT_ID)

        elif app:
            self.init_app(app=app)

    def init_app(self, app=None):
        self.__init__(site_key=app.config.get("RECAPTCHA_SITE_KEY"),
                      secret_key=app.config.get("RECAPTCHA_SECRET_KEY"),
                      is_enabled=app.config.get("RECAPTCHA_ENABLED", DEFAULTS.IS_ENABLED),
                      theme=app.config.get("RECAPTCHA_THEME", DEFAULTS.THEME),
                      type=app.config.get("RECAPTCHA_TYPE", DEFAULTS.TYPE),
                      size=app.config.get("RECAPTCHA_SIZE", DEFAULTS.SIZE),
                      tabindex=app.config.get("RECAPTCHA_TABINDEX", DEFAULTS.TABINDEX),
                      element_id=app.config.get("RECAPTCHA_ELEMENT_ID", DEFAULTS.ELEMENT_ID))

        @app.context_processor
        def get_code():
            return dict(recaptcha=Markup(self.get_code()))

    def get_code(self):
        """
        Returns the new ReCaptcha code
        :return:
        """
        if self.is_enabled:
            if self.size == DEFAULTS.INVISIBLE:
                return """
                    <div id="{ELEMENT_ID}">
                    </div>
                    <script>
                      var recaptchaCallback = function(token) {{
                        // recaptcha has been processed
                        var captcha = document.getElementById("{ELEMENT_ID}"),
                            fields = captcha.getElementsByTagName('textarea');
                        if(!fields.length) return;
                        fields[0].value = token;
                      }};
                      var recaptchaOnloadCallback = function(){{
                        var el = document.getElementById("{ELEMENT_ID}"),
                            widget_id,
                            opts = [];
                        opts['sitekey'] = "{SITE_KEY}";
                        opts['callback'] = 'recaptchaCallback';
                        opts['size'] = "{SIZE}";
                        opts['type'] = "{TYPE}";
                        opts['tabindex'] = "{TABINDEX}";
                        widget_id = grecaptcha.render(el, opts);
                        grecaptcha.execute(widget_id);
                      }};
                    </script>
                    <script src="https://www.google.com/recaptcha/api.js?onload=recaptchaOnloadCallback&render=explicit" async defer></script>
                    """.format(SITE_KEY=self.site_key,
                               SIZE=self.size,
                               ELEMENT_ID=self.element_id,
                               TABINDEX=self.tabindex,
                               TYPE=self.type
                               )
            else:
                return """
                    <script src='//www.google.com/recaptcha/api.js'></script>
                    <div class="g-recaptcha" data-sitekey="{SITE_KEY}"\
                    data-theme="{THEME}" data-type="{TYPE}" data-size="{SIZE}"\
                    data-tabindex="{TABINDEX}"></div>
                """.format(SITE_KEY=self.site_key, THEME=self.theme,
                           TYPE=self.type, SIZE=self.size,
                           TABINDEX=self.tabindex)
        return ""

    def verify(self, response=None, remote_ip=None):
        if self.is_enabled:
            data = {
                "secret": self.secret_key,
                "response": response or request.form.get('g-recaptcha-response'),
                "remoteip": remote_ip or request.environ.get('REMOTE_ADDR')
            }

            r = requests.get(self.VERIFY_URL, params=data)
            return r.json()["success"] if r.status_code == 200 else False
        return True
