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

"""world script main entry point."""

import sys
import argparse

from public import public
from worldlib import __version__
from worldlib.database import Database, gTLDs


@public
def main(args=None):
    parser = argparse.ArgumentParser(
        prog='world',
        description='Top level domain name mapper.')
    parser.add_argument('--version',
                        action='version',
                        version='world {}'.format(__version__))
    parser.add_argument_group('Querying')
    parser.add_argument('-r', '--reverse', action='store_true',
                        help="""Do a reverse lookup.  In this mode, the
                        arguments can be any Python regular expression; these
                        are matched against all TLD descriptions (e.g. country
                        names) and a list of matches is printed.""")
    parser.add_argument('-a', '--all', action='store_true',
                        help='Print the mapping of all top-level domains.')
    parser.add_argument('domain', nargs='*')
    args = parser.parse_args(sys.argv[1:] if args is None else args)
    # Lookup.
    db = Database()
    if args.all:
        print('Country code top level domains:')
        for cc in sorted(db.ccTLDs):
            print('    {}: {}'.format(cc, db.ccTLDs[cc]))
        # Print the empty string instead of an empty print call for Python 2
        # compatibility with the test suite.  Otherwise we get a stupid
        # TypeError when io.StringIO gets a (Python 2) str instead of unicode.
        print('')
        print('Additional top level domains:')
        for tld in sorted(gTLDs):
            print('    {:6}: {}'.format(tld, gTLDs[tld]))
        return
    if len(args.domain) == 0:
        parser.print_help()
        return 0
    newline = False
    for domain in args.domain:
        if args.reverse:
            if newline:
                # Print the empty string instead of an empty print call for
                # Python 2 compatibility with the test suite.  Otherwise we get
                # a stupid TypeError when io.StringIO gets a (Python 2) str
                # instead of unicode.
                print('')
            matches = db.find_matches(domain)
            if len(matches) > 0:
                print('Matches for "{}":'.format(
                    domain, len(matches)))
                for code, country in matches:
                    print('  {}: {}'.format(code, country))
                newline = True
                continue
        else:
            country = db.lookup_code(domain)
            if country is not None:
                print('{} originates from {}'.format(domain, country))
                continue
        print('Where in the world is {}?'.format(domain))
        return 0


if __name__ == '__main__':                          # pragma: no cover
    sys.exit(main())
