# Copyright (C) 2013-2019 Barry A. Warsaw
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

"""Test the Database class."""

from unittest import TestCase
from worldlib.database import Database


class TestDatabase(TestCase):
    def test_basic(self):
        db = Database()
        self.assertEqual(db.lookup_code('it'), 'Italy')

    def test_find_matches(self):
        db = Database()
        matches = db.find_matches('italy')
        self.assertEqual(len(matches), 1)
        self.assertEqual(matches[0], ('it', 'Italy'))

    def test_find_matches_uppercase(self):
        db = Database()
        matches = db.find_matches('ITALY')
        self.assertEqual(len(matches), 1)
        self.assertEqual(matches[0], ('it', 'Italy'))

    def test_find_matches_multiple(self):
        db = Database()
        matches = db.find_matches('united')
        self.assertEqual(len(matches), 6)
        self.assertEqual(sorted(matches), [
            ('ae', 'United Arab Emirates (the)'),
            ('gb',
             'United Kingdom of Great Britain and Northern Ireland (the)'),
            ('tz', 'Tanzania, United Republic of'),
            ('uk', 'United Kingdom (common practice)'),
            ('um', 'United States Minor Outlying Islands (the)'),
            ('us', 'United States of America (the)'),
            ])

    def test_iteration(self):
        codes = []
        for code in Database():
            codes.append(code)
        top_5 = sorted(codes)[:5]
        self.assertEqual(top_5, ['ac', 'ad', 'ae', 'aero', 'af'])
