# Generate word cloud images for frequency of commands usage on your shell

"Word Cloud" is effective way to glasp some kind of frequencies.
This is utility to generate word cloud images from the command `history` in your shell.


## What is "Word Cloud"

* Images that has the shapes & textures like cloud, made from some words.
* Size of each word reflect their own weight.
* The weight is frequency of usage or existence or something else.

See [Google image search with "wordcloud"](https://www.google.co.jp/search?q=wordcloud&tbm=isch) because seeing is simpler than describing.

This tool use https://github.com/amueller/word_cloud .  
The `word_cloud` library is awesome!


## Getting started

### (0) Prerequisite

If you don't have `pyenv`, [install it](https://github.com/yyuu/pyenv#installation).

And create virtual env for this.

```sh
pyenv install 3.5.1 -s
pyenv virtualenv 3.5.1 ch_wordcloud
```

### (1-a) Install from PyPi

    pyenv activate ch_wordcloud
    pip install command_history_wordcloud

or

### (1-b) Install manually

    git clone https://github.com/hatappo/terminal_word_cloud
    cd terminal_word_cloud
    pyenv activate ch_wordcloud
	python setup.py install
    pip install -r requirements.txt
    python setup.py install

### (2) Usage

    command_history_wordcloud


## Help

```sh
$ python command_history_wordcloud.py --help
usage: command_history_wordcloud.py [-h] [-s, [STOP_WORDS]]

Parse, count and generate a word-cloud image from your command line history.

optional arguments:
  -h, --help            show this help message and exit
  -s, [STOP_WORDS], --stop_words [STOP_WORDS]
                        File path that has words you don't want to use. The
                        words must be separated by space or LineFeed.
```


## License

This software is released under the MIT License, see [LICENSE.txt](LICENSE.txt).
