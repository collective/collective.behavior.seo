import logging

from plone.app.layout.links.viewlets import CanonicalURL
from plone.memoize import view
from zope.component import getMultiAdapter

from ..interfaces import ISEOFieldsMarker

logger = logging.getLogger("collective.behavior.seo")


class CanonicalUrlViewlet(CanonicalURL):
    @view.memoize
    def render(self):
        if self.behavior and self.behavior.seo_canonical:
            canonical_url = self.behavior.seo_canonical
        else:
            context_state = getMultiAdapter(
                (self.context, self.request), name="plone_context_state"
            )
            canonical_url = context_state.canonical_object_url()
        return '    <link rel="canonical" href="%s" />' % canonical_url

    def update(self):
        super().update()
        try:
            self.behavior = ISEOFieldsMarker(self.context)
        except TypeError:
            self.behavior = None
