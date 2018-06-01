# jsonpointer-helpers [![Build Status](https://travis-ci.org/Gr1N/jsonpointer-helpers.svg?branch=master)](https://travis-ci.org/Gr1N/jsonpointer-helpers) [![codecov](https://codecov.io/gh/Gr1N/jsonpointer-helpers/branch/master/graph/badge.svg)](https://codecov.io/gh/Gr1N/jsonpointer-helpers)

Helpers for JSON pointers described by [RFC 6901](https://tools.ietf.org/html/rfc6901).

## Installation

    $ pip install jsonpointer-helpers

## Usage

    >>> import jsonpointer_helpers as jp
    >>>
    >>> jp.build({'foo': {'bar': 42}})
    {'/foo/bar': 42}
    >>>
    >>> jp.build_pointer(['foo', 'bar'])
    '/foo/bar'
    >>>
    >>> jp.parse_pointer('/foo/bar')
    ['foo', 'bar']
    >>>
    >>> jp.escape_token('foo~bar')
    'foo~0bar'
    >>>
    >>> jp.unescape_token('foo~0bar')
    'foo~bar'
    >>>

## Testing and linting

For testing and linting install [tox](http://tox.readthedocs.io):

    $ pip install tox

...and run:

    $ tox

## License

`jsonpointer-helpers` is licensed under the MIT license. See the license file for details.
