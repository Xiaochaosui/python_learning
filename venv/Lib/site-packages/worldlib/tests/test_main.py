# Copyright (C) 2015-2019 Barry A. Warsaw
#
# This file is part of world
#
# world is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, version 3 of the License.
#
# world is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# world.  If not, see <http://www.gnu.org/licenses/>.

"""Test main."""

import sys
import worldlib

from contextlib import ExitStack
from functools import partial
from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from worldlib.__main__ import main


def argv(*args):
    args = list(args)
    args.insert(0, 'argv0')
    return args


class TestMain(TestCase):
    """Test the command line."""

    def setUp(self):
        super().setUp()
        self._resources = ExitStack()
        self.addCleanup(self._resources.close)
        self._stdout = StringIO()
        self._stderr = StringIO()
        # Patch argparse's stderr to capture its error messages.
        self._resources.enter_context(
            patch('argparse._sys.stderr', self._stderr))
        # Patch sys.stdout.write() since that's how argparse's version action
        # works.
        self._resources.enter_context(
            patch('argparse._sys.stdout', self._stdout))
        # Capture print output.
        try:
            # Python 3
            self._resources.enter_context(
                patch('builtins.print', partial(print, file=self._stdout)))
        except ImportError:
            # Python 2
            self._resources.enter_context(
                patch('__builtin__.print', partial(print, file=self._stdout)))

    def _output(self, which=None):
        # Return stdout/stderr, stripped of its trailing newline.
        if which is None:
            which = self._stdout
        output = which.getvalue()
        self.assertEqual(output[-1], '\n')
        return output[:-1]

    def test_version(self):
        with self.assertRaises(SystemExit) as cm:
            main(('--version',))
        self.assertEqual(cm.exception.code, 0)
        # In Python 2, the version string gets written to stderr; in Python 3
        # it gets written to stdout.
        if sys.version_info < (3,):
            stream = self._stderr
        else:
            stream = self._stdout
        self.assertEqual(self._output(stream),
                         'world {}'.format(worldlib.__version__))

    def test_main(self):
        # We also have to capture stderr.
        main(('de',))
        self.assertEqual(self._output(), 'de originates from Germany')

    def test_main_unknown_code(self):
        main(('xx',))
        self.assertEqual(self._output(), 'Where in the world is xx?')

    def test_reverse(self):
        main(('-r', 'Germany'))
        self.assertMultiLineEqual(self._stdout.getvalue(), """\
Matches for "Germany":
  de: Germany
""")

    def test_multiple_reverse_matches(self):
        main(('-r', 'united'))
        self.assertMultiLineEqual(self._stdout.getvalue(), """\
Matches for "united":
  ae: United Arab Emirates (the)
  gb: United Kingdom of Great Britain and Northern Ireland (the)
  tz: Tanzania, United Republic of
  uk: United Kingdom (common practice)
  um: United States Minor Outlying Islands (the)
  us: United States of America (the)
""")

    def test_no_reverse_match(self):
        main(('-r', 'freedonia'))
        self.assertEqual(self._output(), 'Where in the world is freedonia?')

    def test_multiple_reverse_searches(self):
        main(('-r', 'canada', 'mexico'))
        self.assertMultiLineEqual(self._stdout.getvalue(), """\
Matches for "canada":
  ca: Canada

Matches for "mexico":
  mx: Mexico
""")

    def test_all(self):
        main(('--all',))
        # Rather than test the entire output, just test the first and last.
        output = self._stdout.getvalue().splitlines()
        self.assertEqual(output[1].strip(), 'ad: Andorra')
        self.assertEqual(output[-1].strip(), 'xxx   : adult entertainment')

    def test_no_domains(self):
        main(())
        output = self._stdout.getvalue().splitlines()
        self.assertEqual(
            output[0].strip(),
            'usage: world [-h] [--version] [-r] [-a] [domain [domain ...]]')
