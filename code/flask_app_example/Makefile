init:
	pip install -r requirements.txt
test:
	pytest -v tests
coverage:
	pytest --cov=mysite --cov-report=html -v tests

run:
	gunicorn manage:app \
	-b "0.0.0.0:5000" \
	-w 2 \
	--pid=mysite.pid \
	-D
stop:
	cat mysite.pid | xargs kill
reload:
	cat mysite.pid | xargs kill -HUP
flake8:
	flake8 --max-complexity 10 --max-line-length=120 mysite
isort:
	isort -rc mysite
