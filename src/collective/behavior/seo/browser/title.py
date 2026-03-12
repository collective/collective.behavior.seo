from collective.behavior.seo.interfaces import ISEOFieldsMarker
from html import escape
from plone.app.layout.viewlets import common
from plone.base.utils import safe_text


class TitleViewlet(common.TitleViewlet):
    """Override the default Plone viewlet"""

    def update(self):
        super().update()

        if ISEOFieldsMarker.providedBy(self.context):
            if self.context.seo_title:
                self.site_title = escape(safe_text(self.context.seo_title))
