test:
	PYTHONPATH=lib python -m unittest discover -s test
deploy:
	PYTHONPATH=lib python lib/send_command_to_server.py

.PHONY: all test clean
