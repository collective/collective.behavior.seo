Using the development buildout
------------------------------

Create a virtualenv in the package::

    $ python3 -mvenv .

Install requirements with pip::

    $ ./bin/pip install -r requirements.txt

Run buildout for Plone 6.0::

    $ ./bin/buildout -c test-6.0.x.cfg

Or run buildout for Plone 5.2::

    $ ./bin/buildout -c test-5.2.x.cfg

Start Plone in foreground:

    $ ./bin/instance fg

Run the tests:

    $ bin/test

Run the tests with tox in all supported Plone and Python combinations, optionally parallel:

    $ tox -p auto
