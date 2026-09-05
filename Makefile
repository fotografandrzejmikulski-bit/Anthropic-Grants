test:
	python -m pytest -q

smoke:
	python experiments/baseline_demo.py

check:
	python -m pytest -q
	python experiments/baseline_demo.py
