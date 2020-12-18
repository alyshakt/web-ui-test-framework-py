"""Search Engine enums o standardize the search engine input"""
import enum


class SearchEngineType(enum.Enum):
	"""To standardize the search engine input"""
	google = 1
	bing = 2
	yandex = 3
