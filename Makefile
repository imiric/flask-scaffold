.PHONY: run clean

run:
	@python webapp/runserver.py

clean:
	@find . -name "*.pyc" -type f -exec rm {} \;
