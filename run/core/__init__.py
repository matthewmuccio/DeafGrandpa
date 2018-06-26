#!/usr/bin/env python3


from flask import Flask

from core.controllers.say import controller as say


omnibus = Flask(__name__)

omnibus.register_blueprint(say)
