=====
world
=====

-------------------------
Where in the world is...?
-------------------------

:Author: Barry Warsaw <barry@python.org>
:Date: 2019-11-05
:Copyright: 2013-2019 Barry A. Warsaw
:Version: 4.1
:Manual section: 1


SYNOPSYS
========

world [options] [tld, [tld, ...]]


DESCRIPTION
===========

This script takes a list of Internet top-level domain names and prints out
where in the world those domains originate from.  Reverse look ups are also
supported.


EXAMPLES
========

Look up top-level domains::

    $ world tz us
    tz originates from Tanzania, United Republic of
    us originates from United States of America (the)

Reverse lookups::

    $ world -r united
    Matches for "united":
      ae: United Arab Emirates (the)
      gb: United Kingdom of Great Britain and Northern Ireland (the)
      tz: Tanzania, United Republic of
      uk: United Kingdom (common practice)
      um: United States Minor Outlying Islands (the)
      us: United States of America (the)

Only two-letter country codes are supported, since these are the only ones
that were freely available from the ISO 3166 standard.  As of 2015-01-09, even
these are no longer available in machine readable form.

This script also knows about non-geographic, generic, USA-centric, historical,
common usage, and reserved top-level domains.


OPTIONS
=======

Querying
--------

  -r, --reverse    Do a reverse lookup. In this mode, the arguments can be
                   any Python regular expression; these are matched against
                   all TLD descriptions (e.g. country names) and a list of
                   matches is printed.
  -a, --all        Print the mapping of all top-level domains.


Other
-----

  -h, --help       show this help message and exit
  --version        show program's version number and exit


With no top-level domains given, help is printed.
