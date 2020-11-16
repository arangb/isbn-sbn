# -*- coding: utf-8 -*-
# flake8: noqa
# pylint: skip-file
"""nose tests for metadata."""

from nose.tools import assert_equals
from isbnlib import meta
from .._sbn import query


def test_query():
    """Test the query of metadata (opac.sbn.it) with 'low level' queries."""
    # does not exist:
    assert_equals(len(repr(query('9788889579060'))) <= 2, True)

    # ok:
    assert_equals(len(repr(query('9788491043508'))) > 100, True)
    assert_equals(len(repr(query('9788437604947'))) > 100, True)
    assert_equals(len(repr(query('9788474234046'))) > 100, True)

    # wrong data?
    assert_equals(len(repr(query('9780000000'))) <= 2, True)
