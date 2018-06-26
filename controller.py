#!/usr/bin/env python3


from flask import Flask, render_template

import model


app = Flask(__name__)

@app.route("/say/<message>")
def say(message):
	return render_template("say.html", message=message, response=model.get_response(message))


if __name__ == "__main__":
	app.run(host="127.0.0.1", port=5000, debug=True)
