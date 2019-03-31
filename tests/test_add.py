import pytest

from pull_request_sandbox import add

@pytest.mark.parametrize('a, b, expected', [
    (1, 2, 3),
    ('a', 'b', 'ab'),
])
def test_add(a, b, expected):
    assert add(a, b) == expected
