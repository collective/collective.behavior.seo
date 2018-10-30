from cgi import escape
from plone.app.layout.viewlets import common

from Products.CMFPlone.utils import safe_unicode

from ..interfaces import ISEOFieldsMarker


class TitleViewlet(common.TitleViewlet):
    """Override the default Plone viewlet"""

    def update(self):
        super(TitleViewlet, self).update()

        if ISEOFieldsMarker.providedBy(self.context):
            if self.context.seo_title:
                self.site_title = escape(safe_unicode(self.context.seo_title))
