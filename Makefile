test: export PYTHONPATH := ./mdtest:$(PYTHONPATH)
test: export PATH := ./bin:$(PATH)
test:
	python3 -m pytest -vv .
	./mdtest/tests/check_mdtest.sh
	mdtest
	@echo
	@echo SUCCESS

run: export PYTHONPATH := ./mdtest:$(PYTHONPATH)
run: export PATH := ./bin:$(PATH)
run:
	mdtest
clean:
	rm -rf */*.pyc  .cache/ .pytest_cache/ __pycache__/ */*/__pycache__/
install:
	pip3 uninstall -y mdtest || true
	pip3 install . --user

.PHONY: test run clean install