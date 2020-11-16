# -*- coding: utf-8 -*-
# flake8: noqa
# pylint: skip-file
"""Simple checks with a few examples. Just to see if it works.
To run: python3 -m isbnlib_sbn.test.simpletest   # no .py at the end"""

from nose.tools import assert_equals
import isbnlib
from .._sbn import query

def test_sbn():
    """Simple tests to study different cases."""
    #print(query('9788832961010')) # two authors
    #print(query('9788854194793'))
    #print(query('9788811810230'))
    #print(query('9788854197152')) # 
    #print(query('9788889579060')) # does not exist?
    #print(query('9788804705307')) # accents in title
    #print(query('9788809808607')) # accents in title
    #print(query('9788806207694')) # accent in name
    #print(query('880605242X')) # fails as ISBN13, only exists in DB as ISBN10
    #print(query('9788817124706')) # this had a space after before the year
    #print(query('9788808621337')) # dictionary with no authors (finds the Publisher, which goob doesn't)
    print(query('9788814031922')) # Corrupted unimarc data: the lines for 200 and 700 are part of previous lines! 
    print(query('9788814034572')) # case of two main laguages: latin and italian, and part of many volumes
    
    #for i in ['9788854194793', '9788811687160', '9788838915741', '9788845901638', '9788817121323', '9788820350222','9788809869424','9788811810230','9788814034572']:
    #    print(query(i))

test_sbn()
