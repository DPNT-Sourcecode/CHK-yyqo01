test:
	PYTHONPATH=lib python -m unittest discover -s test 
test-q:
	PYTHONPATH=lib python -m unittest -q ${TEST}
deploy:
	PYTHONPATH=lib python lib/send_command_to_server.py

.PHONY: all test clean