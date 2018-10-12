from cgi import escape
from zope import component
from plone.app.layout.viewlets import common
from plone.memoize.view import memoize

from Products.CMFPlone.utils import safe_unicode

from ..interfaces import ISEOFieldsMarker


class TitleViewlet(common.TitleViewlet):
    """Override the default Plone viewlet"""

    @property
    def page_title(self):

        if ISEOFieldsMarker.providedBy(self.context):

            if self.context.seo_title:
                return escape(safe_unicode(self.context.seo_title))

        return super(TitleViewlet,self).page_title
        
