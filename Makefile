.PHONY: help init install package register upload release

help:
	@echo "主要なターゲットの一覧"
	@grep -A1 -E '^([[:alnum:]])([[:alnum:]]|-|_)+:' Makefile

init:
	eval "$(pyenv init -)" && pyenv activate ch_wordcloud

install:
	pip install -e .

package:
	python setup.py bdist_wheel

register:
	python setup.py register

upload:
	python setup.py bdist_wheel upload

release: register upload
