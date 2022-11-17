"""Search Engine enums o standardize the search engine input"""
import enum


class App(enum.Enum):
	"""To standardize the variable for switching URL destinations"""
	# TODO add new enums here to scale this framework and return URLs from AppSetup.py
	google = 1
	bing = 2
	yandex = 3
