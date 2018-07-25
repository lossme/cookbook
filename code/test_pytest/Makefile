test:
	pytest -v -s tests
coverage:
	pytest --cov=mypackage --cov-report=html -v -s tests
flake8:
	flake8 --max-complexity 10 --max-line-length=120 mypackage
isort:
	isort -rc mypackage
