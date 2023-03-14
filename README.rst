.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

=======================
collective.behavior.seo
=======================

This small behavior adds extra fields used for SEO optimisation.
Inspired by collective.seo, but the data store now uses dexterity/behavior practice.


Features
--------

Adds fields SEO Title, SEO Description, and Metatag Robots on an extra tab SEO on contenttypes where the behavior is activated.

When the fields contain values, the ``<title>`` and ``<meta name='description'>`` in the ``<head>`` section will be replaced.
Also a ``<meta name="robots">`` tag will be added.

In a control panel you can give a list of valid combinations of robot tags: ``follow/nofollow``, ``index/noindex``.


Translations
------------

This product has been translated into:

- Dutch


Installation
------------

Install collective.behavior.seo by adding it to your buildout::

    [buildout]

    ...

    eggs =
        collective.behavior.seo


and then running ``bin/buildout``.
Or install it with ``pip``.

Activate the add'on in the Plone Contron Panel. Then go to Dexterity Types in the Plone Control Panel
and activate this behavior on selected content types.


Contribute
----------

- Issue Tracker: https://github.com/collective/collective.behavior.seo/issues
- Source Code: https://github.com/collective/collective.behavior.seo


License
-------

The project is licensed under the GPLv2.
