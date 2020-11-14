=================
NEWS of the world
=================

4.1 (2019-11-26)
================
* Use ``importlib.resources`` instead of ``pkg_resources``
* Add support for Python 3.6, 3.7, and 3.8.
* Drop support for Python 3.4.
* Modernize the packaging.


4.0 (2016-08-24)
================
* Add support for Python 3.5.
* Drop support for Python 2.
* With no arguments `world` prints help and exits.
* ISO 3166 database updated.


3.1.1 (2015-03-25)
==================
* Fix missing ``install_requires`` in ``setup.py``.


3.1 (2015-01-08)
================
* Convert repository to git and modernize the code.
* Remove the use of `distribute`.
* Python 2.7 and 3.4 is supported.
* ISO has pulled the free XML version of the two letter country codes.  Thus
  ``--refresh`` now prints a minor rant and is effectively deprecated.
  ``--source`` and ``--cache`` are no-ops and will be removed in a future
  version.


3.0 (2013-07-01)
================
* Initial standalone release.
