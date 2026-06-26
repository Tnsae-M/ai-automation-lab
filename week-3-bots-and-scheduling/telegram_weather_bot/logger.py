import logging
import sys
def setup_logger():
	# Simple, plain logging formatter (no color dependency)
	fmt = "%(asctime)s %(levelname)s: %(message)s"
	datefmt = "%Y-%m-%d %H:%M:%S"
	handler = logging.StreamHandler(stream=sys.stderr)
	handler.setFormatter(logging.Formatter(fmt=fmt, datefmt=datefmt))

	logger = logging.getLogger("weather_app")
	logger.setLevel(logging.INFO)
	if not logger.handlers:
		logger.addHandler(handler)
	return logger