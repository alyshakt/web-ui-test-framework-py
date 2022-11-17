"""To standardize the variable for switching URL destinations"""
import enum


class App(enum.Enum):
	# TODO add new enums here to scale this framework and return URLs from AppSetup.py
	google = 1
	bing = 2
	yandex = 3
