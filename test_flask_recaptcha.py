
from flask import Flask
from flask_recaptcha import ReCaptcha

app = Flask(__name__)
app.config.update({
    "debug": True,
    "RECAPTCHA_SITE_KEY": "SITE_KEY",
    "RECAPTCHA_SITE_SECRET": "SECRET",
    "RECAPTCHA_ENABLED": True
})

def test_recaptcha_enabled():
    recaptcha = ReCaptcha(site_key="SITE_KEY", secret_key="SECRET_KEY")
    assert isinstance(recaptcha, ReCaptcha)
    assert recaptcha.is_enabled == True
    assert "script" in recaptcha.get_code()
    assert recaptcha.verify(response="None", remote_ip="0.0.0.0") == False

def test_recaptcha_enabled_flask():
    recaptcha = ReCaptcha(app=app)
    assert isinstance(recaptcha, ReCaptcha)
    assert recaptcha.is_enabled == True
    assert "script" in recaptcha.get_code()
    assert recaptcha.verify(response="None", remote_ip="0.0.0.0") == False

def test_recaptcha_disabled():
    recaptcha = ReCaptcha(site_key="SITE_KEY", secret_key="SECRET_KEY", is_enabled=False)
    assert recaptcha.is_enabled == False
    assert recaptcha.get_code() == ""
    assert recaptcha.verify(response="None", remote_ip="0.0.0.0") == True

def test_recaptcha_disabled_flask():
    app.config.update({
        "RECAPTCHA_ENABLED": False
    })
    recaptcha = ReCaptcha(app=app)
    assert recaptcha.is_enabled == False
    assert recaptcha.get_code() == ""
    assert recaptcha.verify(response="None", remote_ip="0.0.0.0") == True