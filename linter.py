#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Andrew Grim
# Copyright (c) 2014 Andrew Grim
#
# License: MIT
#

"""This module exports the Puppet plugin class."""

from SublimeLinter.lint import Linter, util


class Puppet(Linter):

    """Provides an interface to puppet."""

    syntax = 'puppet'
    cmd = ('puppet', 'parser', 'validate', '--color=false')
    regex = r'^Error:.+?(?P<message>Syntax error at \'(?P<near>.+?)\' ).+?line (?P<line>\d+):(?P<column>\d+)|^Error:.+?(?P<message>Syntax error at \'(?P<near>.+?)\'; expected \'.+\').+?line (?P<line>\d+)'
    error_stream = util.STREAM_STDERR
