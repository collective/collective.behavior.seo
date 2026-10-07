from collective.behavior.seo.behaviors.seo_fields import ISEOFields
from collective.behavior.seo.interfaces import ICollectiveSeoStructuredDataAdapter
from plone.app.layout.viewlets.common import ViewletBase
from plone.memoize.instance import memoizedproperty
from zope.component import getAdapters

import json


class StructuredDataViewlet(ViewletBase):
    """Base viewlet to render content metadata as JSON-LD"""

    """ the use of this decorator is this a right approach?"""

    @memoizedproperty
    def structured_data(self):
        adapter = ISEOFields(self.context, None)

        seo_structured_data = []

        if adapter:

            adapter_data = adapter.seo_structured_data

            if isinstance(adapter_data, dict):
                seo_structured_data.append(adapter_data)

            elif isinstance(adapter_data, list):
                seo_structured_data = adapter_data.copy()

        # resolve adapters
        # add externally defined extra json/ld schema data
        seo_adapters = getAdapters(
            (self.context, self.request), ICollectiveSeoStructuredDataAdapter
        )

        for name, seo_adapter in seo_adapters:

            try:
                extra_data = seo_adapter.get_data() or []
            except (TypeError, KeyError, AttributeError):
                extra_data = []

            if not extra_data:
                # no data via adapter
                continue

            if isinstance(extra_data, dict):

                # data can be a dict
                seo_structured_data.append(extra_data)

            elif isinstance(extra_data, list):

                # data can be a list
                seo_structured_data.extend(extra_data)

        if not seo_structured_data:
            return ""

        escaped_json = (
            json.dumps(seo_structured_data)
            .replace("<", "\\u003c")
            .replace(">", "\\u003e")
            .replace("&", "\\u0026")
        )

        return escaped_json

    def available(self):
        return bool(self.structured_data)
