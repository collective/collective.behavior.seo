# -*- coding: utf-8 -*-

from collective.behavior.seo import _
from plone import schema
from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.supermodel import model
from zope.component import adapter
from zope.interface import implementer
from zope.interface import provider
from plone.autoform import directives

from ..interfaces import ISEOFieldsMarker

@provider(IFormFieldProvider)
class ISEOFields(model.Schema):
    """
    """
    model.fieldset(
            'seofields',
            label=_(u'SEO'),
            fields=(
                'seo_title',
                'seo_description'
            ),
        )

    seo_title=schema.TextLine(
        title=u"SEO Title",
        description=_(u"This field is used in the web page <head> section "
                      u"title instead of the title on the main tab."),
        required=False
        )

    seo_description=schema.Text(
        title=u"SEO Description",
        description=_(u"This field is used as meta description field in <head> section and browser "
                      u"tab instead of the description on the main tab."),
        required=False
        )

@implementer(ISEOFieldsMarker)
@adapter(IDexterityContent)
class SEOFields(object):
    def __init__(self, context):
        self.context = context

    @property
    def seo_title(self):
        if hasattr(self.context, 'seo_title'):
            return self.context.seo_title
        return None

    @seo_title.setter
    def seo_title(self, value):
        self.context.seo_title = value
    
    @property
    def seo_description(self):
        if hasattr(self.context, 'seo_description'):
            return self.context.seo_description
        return None

    @seo_description.setter
    def seo_description(self, value):
        self.context.seo_description = value
