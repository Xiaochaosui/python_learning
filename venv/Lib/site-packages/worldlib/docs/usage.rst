=============================================
 worldlib -- library for country code lookup
=============================================

To use the ``worldlib`` library, import the database which reads a canned,
pre-generated set of code mappings::

    >>> from worldlib.database import Database
    >>> db = Database()

You can look up a country code::

    >>> print(db.lookup_code('it'))
    Italy

Country codes are case-insensitive::

    >>> print(db.lookup_code('It'))
    Italy

You can find all matches for a particular string, which allows you for example
to implement a reverse look up.   The matches are returned sorted in
alphabetical order.  As with code look ups, the match string is case
insensitive::

    >>> for code, country in db.find_matches('United'):
    ...     print(code, 'is', country)
    ae is United Arab Emirates (the)
    gb is United Kingdom of Great Britain and Northern Ireland (the)
    tz is Tanzania, United Republic of
    uk is United Kingdom (common practice)
    um is United States Minor Outlying Islands (the)
    us is United States of America (the)

You can iterate through all the codes::

    >>> for code in db:
    ...     print(code)
    ac
    ...
    zw
