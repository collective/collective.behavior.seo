from collective.behavior.seo.behaviors.seo_fields import SEOFields
from collective.behavior.seo.interfaces import ICollectiveSeoStructuredDataAdapter
from collective.behavior.seo.interfaces import ISEOFieldsMarker
from plone.app.layout.viewlets.common import ViewletBase
from plone.memoize.view import memoize
from zope.component import getAdapters

import json


class StructuredDataViewlet(ViewletBase):
    """Base viewlet to render content metadata as JSON-LD"""

    """ the use of this decorator is this a right approach?"""

    @property
    @memoize
    def structured_data(self):
        adapter = SEOFields(self.context)

        seo_structured_data = []

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

            extra_data = seo_adapter.get_data() or []

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

        return json.dumps(seo_structured_data)

    def update(self):
        super().update()
        try:
            self.behavior = ISEOFieldsMarker(self.context)
        except TypeError:
            self.behavior = None

    def available(self):
        return bool(self.behavior is not None and self.structured_data)
