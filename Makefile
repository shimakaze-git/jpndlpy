.PHONY: deploy
deploy: build
	twine upload dist/*

.PHONY: test-deploy
test-deploy: build
	twine upload --repository testpypi dist/*

.PHONY: build
build:
	rm -rf dist build jpndlpy.egg-info
	python setup.py sdist bdist_wheel

.PHONY: delete
delete:
	rm -rf dist build jpndlpy.egg-info
