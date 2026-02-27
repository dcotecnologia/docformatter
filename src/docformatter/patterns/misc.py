#!/usr/bin/env python
#
#       docformatter.patterns.misc.py is part of the docformatter project
#
# Copyright (C) 2012-2023 Steven Myint
# Copyright (C) 2023-2025 Doyle "weibullguy" Rowland
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
"""This module provides docformatter's miscellaneous pattern recognition functions."""

# Standard Library Imports
import re
import tokenize
from re import Match
from typing import Union

# docformatter Package Imports
from docformatter.constants import LITERAL_REGEX, URL_REGEX

_INLINE_MATH_PATTERN = re.compile(r" *\w *:[a-zA-Z0-9_\- ]*:")
_LITERAL_PATTERN = re.compile(LITERAL_REGEX)
_PARAM_LIST_MARKER_PATTERN = re.compile(r"\s(?:@|-|\*)\s")
_BEGIN_SENTENCE_PATTERN = re.compile(r"^[-@\)]")
_PYDOC_REF_PATTERN = re.compile(r"^:\w+:")
_URL_PATTERN = re.compile(URL_REGEX)


# TODO: Create INLINE_MATH_REGEX in constants.py and use it here.
def is_inline_math(line: str) -> Union[Match[str], None]:
    """Check if the line is an inline math expression.

    Parameters
    ----------
    line : str
        The line to check for inline math patterns.

    Returns
    -------
    Match[str] | None
        A match object if the line matches an inline math pattern, None otherwise.

    Notes
    -----
    Inline math expressions have the following pattern:
        c :math:`[0, `]`
    """
    return _INLINE_MATH_PATTERN.match(line)


def is_literal_block(line: str) -> Union[Match[str], None]:
    """Check if the line is a literal block.

    Parameters
    ----------
    line : str
        The line to check for literal block patterns.

    Returns
    -------
    Match[str] | None
        A match object if the line matches a literal block pattern, None otherwise.

    Notes
    -----
    Literal blocks have the following pattern:
        ::
            code
    """
    return _LITERAL_PATTERN.match(line)


def is_probably_beginning_of_sentence(line: str) -> Union[Match[str], None, bool]:
    """Determine if the line begins a sentence.

    Parameters
    ----------
    line : str
        The line to be tested.

    Returns
    -------
    bool
        True if this token is the beginning of a sentence, False otherwise.
    """
    if _PARAM_LIST_MARKER_PATTERN.search(line):
        return True

    stripped_line = line.strip()
    is_beginning_of_sentence = _BEGIN_SENTENCE_PATTERN.match(stripped_line)
    is_pydoc_ref = _PYDOC_REF_PATTERN.match(stripped_line)

    return is_beginning_of_sentence and not is_pydoc_ref


def is_some_sort_of_code(text: str) -> bool:
    """Return True if the text looks like code.

    Parameters
    ----------
    text : str
        The text to check for code patterns.

    Returns
    -------
    bool
        True if the text contains code-like patterns, False otherwise.
    """
    return any(
        len(word) > 50 and not _URL_PATTERN.match(word)  # noqa: PLR2004
        for word in text.split()
    )


def is_string_constant(token: tokenize.TokenInfo) -> bool:
    """Determine if docstring token is actually a string constant.

    Parameters
    ----------
    token : TokenInfo
        The token immediately preceding the docstring token.

    Returns
    -------
    bool
        True if the docstring token is actually a string constant, False otherwise.
    """
    if token.type == tokenize.OP and token.string == "=":
        return True

    return False
