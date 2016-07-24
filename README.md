# Generates word cloud images for frequency of commands usage on your shell

"Word Cloud" is effective way to glasp some kind of frequencies.
This is utility to generate word cloud images from the command `history` in your shell.


## What is "Word Cloud"

* Images that has the shapes & textures like cloud, made from some words.
* Size of each word reflect their own weight.
* The weight is frequency of usage or existence or something else.

See [Google image search with "wordcloud"](https://www.google.co.jp/search?q=wordcloud&tbm=isch) because seeing is simpler than describing.

This tool use https://github.com/amueller/word_cloud .  
The `word_cloud` is very easy to use and awesome!


## Getting started

### Install

Install from [PyPi](https://pypi.python.org/pypi/command_history_wordcloud)

```sh
pip install command_history_wordcloud
```

Or install manually from GitHub

```sh
git clone https://github.com/hatappo/terminal_word_cloud
cd terminal_word_cloud
python setup.py install -e
```

### Usage

    chwc


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
