Adding and updating locales
---------------------------


.. code-block:: console

    $ uvx i18ndude rebuild-pot --pot ./src/collective/behavior/seo/locales/collective.behavior.seo.pot --create collective.behavior.seo ./src/collective/behavior/seo
    $ uvx i18ndude sync --pot ./src/collective/behavior/seo/locales/collective.behavior.seo.pot ./src/collective/behavior/seo/locales/*/LC_MESSAGES/collective.behavior.seo.po


Note
----

The script uses gettext package for internationalization.

Install it before running the script.

On macOS
--------

.. code-block:: console

    $ brew install gettext

On Windows
----------

see https://mlocati.github.io/articles/gettext-iconv-windows.html
