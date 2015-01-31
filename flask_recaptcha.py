"""
Flask-reCaptcha
"""

__NAME__ = "Flask-reCaptcha"
__version__ = "0.2"
__license__ = "MIT"
__author__ = "Mardix"
__copyright__ = "(c) 2014 Mardix"

import urllib2
import urllib

try:
    from flask import request
except ImportError as ex:
    print("Flask is missing")
try:
    from jinja2 import Markup
except ImportError as ex:
    print("Jinja2 is missing. pip --install jinja2")

API_SSL_SERVER = "https://www.google.com/recaptcha/api"
API_SERVER = "http://www.google.com/recaptcha/api"
VERIFY_SERVER = "www.google.com"


class reCaptcha(object):

    is_valid = False
    error_code = None
    use_ssl = False

    def __init__(self, public_key=None, private_key=None, ssl=False):
        if public_key:
            self.public_key = public_key
        if private_key:
            self.private_key = private_key

        self.use_ssl = ssl

    def init_app(self, app):
        self.public_key = app.config.get("RECAPTCHA_PUBLIC_KEY")
        self.private_key = app.config.get("RECAPTCHA_PRIVATE_KEY")
        self.use_ssl = app.config.get("RECAPTCHA_USE_SSL", False)

        @app.context_processor
        def get_code():
            return dict(recaptcha=Markup(self.get_code()))

    def validate(self,
                 challenge_field=None,
                 response_field=None,
                 remote_ip=None):
        """
        To validate the recaptcha

        recaptcha_challenge_field -- The value of recaptcha_challenge_field from the form
        recaptcha_response_field -- The value of recaptcha_response_field from the form
        private_key -- your reCAPTCHA private key
        remoteip -- the user's ip address

        returns bool
        """

        recaptcha_challenge_field = challenge_field or request.form.get('recaptcha_challenge_field')
        recaptcha_response_field = response_field or request.form.get('recaptcha_response_field')
        remoteip = remote_ip or request.environ.get('REMOTE_ADDR')

        if not recaptcha_challenge_field or not recaptcha_response_field:
            self.is_valid = False
            self.error_code = "incorrect-captach-sol"
        else:

            params = {
                'privatekey':self.private_key,
                'remoteip':  self._encode(remoteip),
                'challenge': self._encode(recaptcha_challenge_field),
                'response':  self._encode(recaptcha_response_field),
            }

            headers = {
                "Content-type": "application/x-www-form-urlencoded",
                "User-agent": "reCAPTCHA Python"
            }

            _request = urllib2.Request (
                url="http://%s/recaptcha/api/verify" % VERIFY_SERVER,
                data=urllib.urlencode(params),
                headers=headers)

            httpresp = urllib2.urlopen(_request)

            return_values = httpresp.read().splitlines()
            httpresp.close()

            return_code = return_values[0]
            if return_code == "true":
                self.is_valid = True
                self.error_code = None
            else:
                self.is_valid = False
                self.error_code = return_values[1]

        return self.is_valid


    def _encode(self, s):
        if isinstance(s, unicode):
            return s.encode('utf-8')
        return s


    def get_code(self, error=None):
        """Gets the HTML to display for reCAPTCHA

        error -- An error message to display (from RecaptchaResponse.error_code)"""

        error_param = '&error=%s' % error if error else ""
        server = API_SSL_SERVER if self.use_ssl else API_SERVER

        return """
    <script type="text/javascript" src="{API_SERVER}/challenge?k={PUBLIC_KEY}{ERROR_PARAM}"></script>
    <noscript>
      <iframe src="{API_SERVER}/noscript?k={PUBLIC_KEY}{ERROR_PARAM}" height="300" width="500" frameborder="0"></iframe><br />
      <textarea name="recaptcha_challenge_field" rows="3" cols="40"></textarea>
      <input type='hidden' name='recaptcha_response_field' value='manual_challenge' />
    </noscript>
    """.format(API_SERVER=server,
               PUBLIC_KEY=self.public_key,
               ERROR_PARAM=error_param)

