.PHONY: help init install package _register _upload release browse

help:
	@echo "主要なターゲットの一覧"
	@grep -A1 -E '^([[:alnum:]])([[:alnum:]]|-|_)+:' Makefile

init:
	eval "$(pyenv init -)" && pyenv activate ch_wordcloud

install:
	pip install -e .

package:
	python setup.py bdist_wheel

_register:
	python setup.py register

_upload:
	python setup.py bdist_wheel upload

release: _register _upload

browse:
	open https://pypi.python.org/pypi/command_history_wordcloud
