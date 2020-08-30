
from flask import Flask
from flask_xcaptcha import XCaptcha

app = Flask(__name__)
app.config.update({
    "debug": True,
    "XCAPTCHA_SITE_KEY": "SITE_KEY",
    "XCAPTCHA_SITE_SECRET": "SECRET",
    "XCAPTCHA_ENABLED": True
})

def test_xcaptcha_enabled():
    xcaptcha = XCaptcha(site_key="SITE_KEY", secret_key="SECRET_KEY")
    assert isinstance(xcaptcha, XCaptcha)
    assert xcaptcha.is_enabled == True
    assert "script" in xcaptcha.get_code()
    assert xcaptcha.verify(response="None", remote_ip="0.0.0.0") == False

def test_xcaptcha_enabled_flask():
    xcaptcha = XCaptcha(app=app)
    assert isinstance(xcaptcha, XCaptcha)
    assert xcaptcha.is_enabled == True
    assert "script" in xcaptcha.get_code()
    assert xcaptcha.verify(response="None", remote_ip="0.0.0.0") == False

def test_xcaptcha_disabled():
    xcaptcha = XCaptcha(site_key="SITE_KEY", secret_key="SECRET_KEY", is_enabled=False)
    assert xcaptcha.is_enabled == False
    assert xcaptcha.get_code() == ""
    assert xcaptcha.verify(response="None", remote_ip="0.0.0.0") == True

def test_xcaptcha_disabled_flask():
    app.config.update({
        "XCAPTCHA_ENABLED": False
    })
    xcaptcha = XCaptcha(app=app)
    assert xcaptcha.is_enabled == False
    assert xcaptcha.get_code() == ""
    assert xcaptcha.verify(response="None", remote_ip="0.0.0.0") == True