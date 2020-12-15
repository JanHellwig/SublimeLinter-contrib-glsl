#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by numb3r23 - Sebastian Schaefer
# Copyright (c) 2015 Sebastian Schaefer
#
# License: MIT
#
# ******
#
# GLSLLint interface to glslangValidator written by numb3r23

"""This module exports the GLSLLint plugin linter class."""

from SublimeLinter.lint import Linter, util


class GlslangValidator(Linter):

    """Provides an interface to glslangValidator."""

    cmd = ('glslangValidator', '@')
    multiline = False
    defaults = {
        'selector': 'source.glsl, source.essl'
    }
    regex = (r'^ERROR:\s.*:(?P<line>\d+):\s\'(?P<near>.*)\'\s:\s+(?P<message>.+)')
    error_stream = util.STREAM_BOTH
    tempfile_suffix = '-'
