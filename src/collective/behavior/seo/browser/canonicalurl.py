from ..interfaces import ISEOFieldsMarker
from plone.app.layout.viewlets import common
from zope.component import getMultiAdapter

import logging


logger = logging.getLogger("collective.behavior.seo")

# Code mostly reused from https://github.com/simplesconsultoria/sc.seo


class CanonicalUrlViewlet(common.ViewletBase):
    """Renders the  <link rel="canonical"> tag if the ICanonicalUrl is applied
    to the context
    """

    def update(self):
        super().update()
        try:
            self.behavior = ISEOFieldsMarker(self.context)
        except TypeError:
            self.behavior = None

    def available(self):
        return True if self.behavior else False

    def content(self):
        context_state = getMultiAdapter(
            (self.context, self.request), name="plone_context_state"
        )
        content = self.behavior.seo_canonical
        # If there is no restriction, we explicity allow indexing
        if not content:
            return self.context.absolute_url()
        return content
