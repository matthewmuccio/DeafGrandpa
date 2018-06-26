#!/usr/bin/env python3


import random


# The possible "witty responses" that the grandpa could say to the user.
responses = ["Did you hear about the restaurant on the moon? Great food, no atmosphere.", \
		"What do you call a fake noodle? An impasta.", \
		"Why did the coffee file a police report? It got mugged.", \
		"How does a penguin build its house? Igloos it together.", \
		"What you call cheese that isn't yours? Nacho Cheese.", \
		"Want to hear a joke about construction? I'm still working on it.", \
		"What do you call a man with a rubber toe? Roberto.", \
		"Y'know, the rotation of Earth really makes my day.", \
		"Y'know, the shovel was really a ground-breaking invention.", \
		"Y'know, I thought about going on an all-almond diet. But that's just nuts."]

# Function gets called when the user visits URI host:port/say/<message>.
def get_response(message):
	if message.isupper():
		return get_witty_response()
	else:
		return "What? I can't hear you!"

# Function that gets called when the user enters a variable in the URI that is written in upper case.
def get_witty_response():
	return responses[random.randint(0, len(responses) - 1)]
