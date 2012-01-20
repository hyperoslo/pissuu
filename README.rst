Pissuu
======

Python client for the Issuu API.

Usage
-----

::

    from pissuu import IssuuAPI

    issuu = IssuuAPI(
        key = 'qyy6ls1qv15uh9xwwlvk853u2uvpfka7',
        secret = '13e3an36eaxjy8nenuepab05yc7j7w5g'
    )

    upload = issuu.upload(
        file = open('brochure.pdf'),
        title = 'Brochure'
    )

Disclaimer
----------

Pissuu is under development, and does not implement functionality
besides listing and uploading documents.

Installation
------------

Pissuu is best installed with `pip <http://pypi.python.org/pypi/pip>`_::

    $ pip install git+git://github.com/hyperoslo/pissuu.git
