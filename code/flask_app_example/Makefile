PACKAGE=mysite
TEST_PACKAGE=tests
PID_NAME=$(PACKAGE).pid

init:
	pip install -r requirements.txt
test:
	pytest -v $(TEST_PACKAGE)
coverage:
	pytest --cov=$(PACKAGE) --cov-report=html -v $(TEST_PACKAGE)
run:
	gunicorn manage:app \
	-b "0.0.0.0:5000" \
	-w 2 \
	--pid=$(PID_NAME) \
	-D
stop:
	cat $(PID_NAME) | xargs kill
reload:
	cat $(PID_NAME) | xargs kill -HUP
flake8:
	flake8 --max-complexity 10 --max-line-length=120 $(PACKAGE)
isort:
	isort -rc $(PACKAGE)
