# collective.behavior.seo

This small behavior adds extra fields used for SEO optimisation.
Inspired by collective.seo, but the data store now uses dexterity/behavior practice.

## Features

Adds fields SEO Title, SEO Description, Metatag Robots and Structured Data on an extra tab SEO on contenttypes where the behavior is activated.

When the fields contain values, the `<title>` and `<meta name='description'>` in the `<head>` section will be replaced.
Also a `<meta name="robots">` tag will be added.

In a control panel you can give a list of valid combinations of robot tags: `follow/nofollow`, `index/noindex`.

A Viewlet for `Structured Data` called `collective.behavior.seo.structured_data` register in the HTML Header Area by the `plone.app.layout.viewlets.interfaces.IHtmlHead` Viewlet Manager

An Interface for Adapter Registration and Resolution `ICollectiveSeoStructuredDataAdapter`

### Use Structured Data

read more: https://schema.org

Two Options to provide `Structured Data` in the Website.

**You can use both options together, the result in the Viewlet will then be concatenated.**

1. use the field in the seo tab

2. register an adapter


``` zcml
  <!-- Adapter for a Document - inject JSON LD-->
  <adapter
      factory="collective.behavior.seo.tests.CustomStructuredDataVariant1"
      for="plone.app.contenttypes.interfaces.IDocument
           collective.behavior.seo.interfaces.ICollectiveBehaviorSeoLayer"
      name="json-ld-variant1"
      />
```

``` python
@implementer(ICollectiveSeoStructuredDataAdapter)
class CustomStructuredDataVariant1:
    """Additional structured data adapter."""

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def get_data(self):
        """ Return a list or dict with data """
        """ see https://schema.org for all possible schema data """
        return {
            "@context": "https://schema.org/",
            "@type": "Organization",
            "name": "Plone Team",
            "url": "https://plone.org",
        }
```



## Translations

This product has been translated into:

- Dutch
- German

translate content, please run

```
uvx i18ndude rebuild-pot --pot ./src/collective/behavior/seo/locales/collective.behavior.seo.pot --create collective.behavior.seo ./src/collective/behavior/seo
uvx i18ndude sync --pot ./src/collective/behavior/seo/locales/collective.behavior.seo.pot ./src/collective/behavior/seo/locales/*/LC_MESSAGES/collective.behavior.seo.po
```

## Installation

Install collective.behavior.seo by adding it to your buildout:

```
[buildout]
...
eggs =
    collective.behavior.seo
```

and then running `bin/buildout`.

Or install it with `pip`.

Activate the add'on in the Plone Contron Panel. Then go to Dexterity Types in the Plone Control Panel
and activate this behavior on selected content types.

## Contribute

- Issue Tracker: https://github.com/collective/collective.behavior.seo/issues
- Source Code: https://github.com/collective/collective.behavior.seo


## License

The project is licensed under the GPLv2.
