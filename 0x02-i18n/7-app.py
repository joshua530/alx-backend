#!/usr/bin/env python3
"""
main file of the flask application
"""
import pytz
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Union

from pytz import timezone

app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """
    configures the application.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale() -> str:
    """
    selects the locale.
    """
    locale = request.args.get('locale')
    if locale:
        if locale in app.config['LANGUAGES']:
            return locale
    elif g.user:
        locale = g.user.get('locale')
        if locale in app.config['LANGUAGES']:
            return locale
        return app.config['BABEL_DEFAULT_LOCALE']
    elif request.accept_languages:
        return request.accept_languages.best_match(app.config['LANGUAGES'])
    return app.config['BABEL_DEFAULT_LOCALE']


@babel.timezoneselector
def get_timezone() -> str:
    """
    fetches the timezone
    """
    tz = request.args.get('timezone')
    if tz:
        return validate_timezone(tz)
    elif g.user:
        tz = validate_timezone(g.user.get('timezone'))
        return tz
    return app.config['BABEL_DEFAULT_TIMEZONE']


def validate_timezone(tz: str) -> str:
    """
    validates the timezone.
    """
    try:
        return timezone(tz).zone
    except pytz.exceptions.UnknownTimeZoneError:
        return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    """
    main page - hello world

    fetches index page
    """
    return render_template('7-index.html')


def get_user() -> Union[dict, None]:
    """
    fetches the user.
    """
    login_as = request.args.get('login_as')
    if login_as and login_as.isdigit():
        return users.get(int(login_as), None)
    return None


@app.before_request
def before_request() -> None:
    """
    sets the user.
    """
    g.user = get_user()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
