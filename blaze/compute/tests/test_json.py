from __future__ import absolute_import, division, print_function

from blaze.utils import example
from into.backends.json import JSON, JSONLines
from into import Chunks
from blaze import symbol, discover, compute, into, resource


js = JSON(example('accounts.json'))
jss = JSONLines(example('accounts-streaming.json'))

s = symbol('s', discover(js))


def test_simple():
    assert compute(s.count(), js) == 5
    assert compute(s.count(), jss) == 5


def test_less_simple():
    assert compute(s.amount.sum(), js) == 100
    assert compute(s.amount.sum(), jss) == 100


def test_chunks_json():
    r = resource(example('accounts-streaming*.json'))
    assert isinstance(r, Chunks)
    assert compute(s.amount.sum(), r) == 200
