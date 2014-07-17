#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Leonid Shevtsov
# Copyright (c) 2014 Leonid Shevtsov
#
# License: MIT
#

"""This module exports the ClojureSyntaxCheck plugin class."""

from SublimeLinter.lint import Linter, util
from os.path import dirname


class ClojureSyntaxCheck(Linter):

    """Provides an interface to clojure-syntax-check."""

    syntax = 'clojure'
    cmd = ('java -jar "' + dirname(__file__) + '/bin/clojure-syntax-check-0.1.1-standalone.jar"')
    # version_args = '--version'
    # version_re = r'(?P<version>\d+\.\d+\.\d+)'
    # version_requirement = '>= 1.0'
    executable = None
    regex = r'(?P<line>\d+): (?P<message>.+)'
    multiline = False
    line_col_base = (1, 1)
    tempfile_suffix = None
    error_stream = util.STREAM_BOTH
    selectors = {}
    word_re = None
    defaults = {}
    inline_settings = None
    inline_overrides = None
    comment_re = None
