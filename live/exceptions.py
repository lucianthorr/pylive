class LiveException(Exception):
	"""Base class for all Live-related errors
	"""
	pass

class LiveConnectionError(LiveException):
	""" Error establishing a connection to LiveOSC. """
	pass