from collective.behavior.seo.interfaces import ICollectiveSeoStructuredDataAdapter
from zope.interface import implementer

TEST_SCHEMA_JSON_LD_LIST = [
    {
        "@context": "https://schema.org/",
        "@type": "Person",
        "name": "Jane Doe",
        "sponsor": {
            "@type": "Organization",
            "name": "Plone",
            "url": "http://plone.org",
        },
    }
]

TEST_SCHEMA_JSON_LD_OBJECT = {
    "@context": "https://schema.org/",
    "@type": "Person",
    "name": "John Doe",
    "sponsor": {
        "@type": "Organization",
        "name": "Plone",
        "url": "http://plone.org",
    },
}


TEST_ADAPTER_SCHEMA_JSON_LD_VARIANT1 = [
    {
        "@context": "https://schema.org/",
        "@type": "Organization",
        "name": "Plone Foundation",
        "url": "https://plone.org",
        "sponsor": {
            "@type": "Organization",
            "name": "W3C",
            "url": "https://www.w3.org/",
        },
    }
]


TEST_ADAPTER_SCHEMA_JSON_LD_VARIANT2 = {
    "@context": "https://schema.org/",
    "@type": "Organization",
    "name": "Plone Team",
    "url": "https://plone.org",
}


@implementer(ICollectiveSeoStructuredDataAdapter)
class CustomStructuredDataVariant1:
    """Additional structured data adapter."""

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def get_data(self):
        return TEST_ADAPTER_SCHEMA_JSON_LD_VARIANT1


@implementer(ICollectiveSeoStructuredDataAdapter)
class CustomStructuredDataVariant2:
    """Additional structured data adapter."""

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def get_data(self):
        return TEST_ADAPTER_SCHEMA_JSON_LD_VARIANT2
