#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re, codecs, argparse
from pprint import pformat
from os import path
from subprocess import Popen, PIPE, STDOUT
from logging import getLogger, StreamHandler, Formatter, DEBUG
from wordcloud import WordCloud


####################
# Initialization
####################
logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
formatter = Formatter('%(asctime)s %(levelname)7s [%(name)s] %(message)s')
handler.setFormatter(formatter)
logger.setLevel(DEBUG)
logger.addHandler(handler)


####################
# Constants
####################
command_pattern = re.compile("[\s;=<].+$")


####################
# Functions
####################

def create_history_frequencies():
	home       = path.expanduser('~')
	logger.debug("user home path  = '%s'" % home)
	shell_byte = Popen("echo $SHELL", shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT).communicate()[0]
	shell_path = shell_byte.decode("utf-8").strip()
	shell_name = shell_path.rsplit("/", 1)[-1]
	logger.debug("shell path = '%s'" % shell_path)
	logger.debug("shell name = '%s'" % shell_name)

	words = {}

	if shell_name in ["bash", "sh", "ksh"]:
		if   shell_name in ["ksh"]:        filepath = home + "/.sh_history"
		elif shell_name in ["bash", "sh"]: filepath = home + "/.bash_history"
		else: raise Exception()
		with codecs.open(filepath, "r", encoding='utf-8', errors='ignore') as f:
			for line in f:
				word = command_pattern.sub("", line).strip()
				words[word] = words.get(word, 0) + 1

	elif shell_name in ["zsh"]:
		with codecs.open(home + "/.zsh_history", "r", encoding='utf-8', errors='ignore') as f:
			for line in f:
				parts = line.split(";", 1)
				if len(parts) < 2: continue
				word = command_pattern.sub("", parts[1]).strip()
				words[word] = words.get(word, 0) + 1

	elif shell_name in ["csh"]:
		logger.warning("Not implemented!") # TODO:

	else:
		raise Exception("Unknown shell : '%1'" % shell)

	return tuple(words.items())

def load_stop_words(path):
	if path == None: return set()
	with codecs.open(path, "r", encoding='utf-8', errors='ignore') as f:
		return set(f.read().split())

def create_wordcloud(frequencies, stop_words):
	if len(frequencies) == 0: Exception("No history is found.")
	logger.debug("word frequencies count = %s" % len(frequencies))
	logger.debug("stop words = %s" % pformat(stop_words))
	wordcloud = WordCloud(background_color="black", width=900, height=600, stopwords=stop_words).generate_from_frequencies(frequencies)
	image = wordcloud.to_image()
	image.show()

def main():
	# Command line args
	parser = argparse.ArgumentParser(description="Parse, count and generate a word-cloud image from your command line history.")
	parser.add_argument("-s,", "--stop_words", nargs="?", help="File path that has words you don't want to use. The words must be separated by space or LineFeed.")
	args = parser.parse_args()
	stop_words_file = args.stop_words
	logger.debug("stop words file = '%s'" % stop_words_file)

	# main
	logger.info("Started %s." % path.basename(__file__))
	words = create_history_frequencies()
	stop_words = load_stop_words(stop_words_file)
	create_wordcloud(words, stop_words)
	logger.info("Finished %s." % path.basename(__file__))

####################
# Main
####################
if __name__ == '__main__':
	main()
