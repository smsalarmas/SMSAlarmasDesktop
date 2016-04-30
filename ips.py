# -*- coding: latin-1 -*-

import textwrap

text = 'holaaaaaaaaaaaaaaaaaaaaaaaaaaa'
n = 10

lines = textwrap.wrap(text, n, break_long_words=True)

print lines
