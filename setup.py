#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(name='command_history_wordcloud',
      version='1.0.7',
      description='Generate word cloud images for frequency of commands usage on your shell',
      author='Fumihiko Hata',
      author_email='hatappo44+command_history_wordcloud@gmail.com',
      url='https://github.com/hatappo/command_history_wordcloud',
      packages=find_packages(),
      include_package_data=True,
      keywords=['wordcloud'],
      license='MIT License',
      install_requires=[
          'Django',
          'image',
          'numpy',
          'Pillow',
          'wordcloud',
      ],
      entry_points={
          "console_scripts": [
              "chwc=command_history_wordcloud.command_history_wordcloud:main",
          ],
      }
)
