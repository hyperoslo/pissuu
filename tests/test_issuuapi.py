"""Tests for pissuu.IssuuAPI."""

import os

from pissuu import IssuuAPI

FIXTURES_PATH = os.path.dirname(__file__) + '/fixtures'

API_KEY = 'eg6rrqqvabzzkkxfdqqz52tzi7m2fsbv'
API_SECRET = 'ektdvd0zzoj74nk837vfvqbur3jylvlz'

def test_sign():
    """Verify that ``_sign`` creates a valid signature."""

    issuu = IssuuAPI(
        key = API_KEY,
        secret = API_SECRET,
    )

    signature = issuu._sign({
        'foo': 'foo',
        'bar': 'bar',
        'baz': 'baz'
    })

    assert signature == 'fe90fc7886706c3e628ccb7a2f8c2ce7'

def test_list_documents():
    """Verify that ``list_documents`` lists documents."""

    issuu = IssuuAPI(
        key = API_KEY,
        secret = API_SECRET,
    )

    assert issuu.list_documents()

def test_upload_document():
    """Verify that ``upload_document`` uploads a document."""

    issuu = IssuuAPI(
        key = API_KEY,
        secret = API_SECRET
    )

    assert issuu.upload_document(
        file = open('%s/parrot.pdf' % FIXTURES_PATH),
        title = 'Parrot'
    )
