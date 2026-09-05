test:
	python -m pytest -q

smoke:
	python -m src

check: test smoke
