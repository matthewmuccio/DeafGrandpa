#!/usr/bin/env python3


from flask import Blueprint, render_template

from core.models import model


controller = Blueprint("say", __name__, url_prefix="/say")

@controller.route("/<message>", methods=["GET"])
def say(message):
	return render_template("say.html", message=message, response=model.get_response(message))
