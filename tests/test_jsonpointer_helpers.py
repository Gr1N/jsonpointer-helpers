import pytest

import jsonpointer_helpers


def test_build_ok():
    assert jsonpointer_helpers.build({
        'foo': {
            'bar': 'foobar',
            'bar~bar': 'foo~foo',
        },
        'bar': 'foo',
        'foos': {
            0: {
                'foo_1': 'bar_1',
            },
            1: {
                'foo_2': 'bar_2',
            },
        },
        'foo/bar': {
            'bar/foo': {
                0: {
                    'bar_1': 'foo_1',
                },
                1: {
                    'bar_2': 'foo_2',
                },
            },
        },
    }) == {
        '/foo/bar': 'foobar',
        '/foo/bar~0bar': 'foo~foo',
        '/bar': 'foo',
        '/foos/0/foo_1': 'bar_1',
        '/foos/1/foo_2': 'bar_2',
        '/foo~1bar/bar~1foo/0/bar_1': 'foo_1',
        '/foo~1bar/bar~1foo/1/bar_2': 'foo_2',
    }


def test_build_with_initial_ref_tokens_ok():
    assert jsonpointer_helpers.build({
        'foo': {
            'bar': 'foobar',
            'bar~bar': 'foo~foo',
        },
        'bar': 'foo',
        'foos': {
            0: {
                'foo_1': 'bar_1',
            },
            1: {
                'foo_2': 'bar_2',
            },
        },
        'foo/bar': {
            'bar/foo': {
                0: {
                    'bar_1': 'foo_1',
                },
                1: {
                    'bar_2': 'foo_2',
                },
            },
        },
    }, initial_ref_tokens=[
        'initial',
        'ref',
        'tokens',
    ]) == {
        '/initial/ref/tokens/foo/bar': 'foobar',
        '/initial/ref/tokens/foo/bar~0bar': 'foo~foo',
        '/initial/ref/tokens/bar': 'foo',
        '/initial/ref/tokens/foos/0/foo_1': 'bar_1',
        '/initial/ref/tokens/foos/1/foo_2': 'bar_2',
        '/initial/ref/tokens/foo~1bar/bar~1foo/0/bar_1': 'foo_1',
        '/initial/ref/tokens/foo~1bar/bar~1foo/1/bar_2': 'foo_2',
    }


@pytest.mark.parametrize('in_, out', [
    ([], ''),
    ([1], '/1'),
    ([1, 2, 3], '/1/2/3'),
    (['a/b', 3, 'm~n', 'foo'], '/a~1b/3/m~0n/foo'),
])
def test_build_pointer_ok(in_, out):
    assert jsonpointer_helpers.build_pointer(in_) == out


@pytest.mark.parametrize('in_, out', [
    ('', []),
    ('/', ['']),
    ('/1', ['1']),
    ('/1/2/3', ['1', '2', '3']),
    ('/a~1b/3/m~0n/foo', ['a/b', '3', 'm~n', 'foo']),
])
def test_parse_pointer_ok(in_, out):
    assert jsonpointer_helpers.parse_pointer(in_) == out


def test_parse_pointer_invalid():
    with pytest.raises(jsonpointer_helpers.JSONPointerError):
        jsonpointer_helpers.parse_pointer('invalid')


@pytest.mark.parametrize('in_, out', [
    ('', ''),
    (' ', ' '),
    ('a/b', 'a~1b'),
    ('c%d', 'c%d'),
    ('e^f', 'e^f'),
    ('g|h', 'g|h'),
    ('i\\j', 'i\\j'),
    ('k\"l', 'k\"l'),
    ('m~n', 'm~0n'),
])
def test_escape_token_ok(in_, out):
    assert jsonpointer_helpers.escape_token(in_) == out


@pytest.mark.parametrize('in_, out', [
    ('', ''),
    (' ', ' '),
    ('a~1b', 'a/b'),
    ('c%d', 'c%d'),
    ('e^f', 'e^f'),
    ('g|h', 'g|h'),
    ('i\\j', 'i\\j'),
    ('k\"l', 'k\"l'),
    ('m~0n', 'm~n'),
])
def test_unescape_token_ok(in_, out):
    assert jsonpointer_helpers.unescape_token(in_) == out
