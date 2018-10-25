# -*- coding: utf-8 -*-

from collective.behavior.seo import _
from plone import schema
from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.supermodel import model
from zope.component import adapter
from zope.interface import implementer
from zope.interface import provider
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary
from plone.autoform import directives as form
from plone.app.z3cform.widget import AjaxSelectFieldWidget


@provider(IFormFieldProvider)
class ISEOFields(model.Schema):
    """
    """
    model.fieldset(
            'seofields',
            label=_(u'SEO'),
            fields=(
                'seo_title',
                'seo_description',
                'seo_robots'
            ),
        )

    seo_title=schema.TextLine(
        title=_(u"SEO Title"),
        description=_(u"Used in the web page <head> section title and "
                      u"browser tab instead of the default title."),
        required=False
        )

    seo_description=schema.Text(
        title=_(u"SEO Description"),
        description=_(u"Used as meta description field in the <head> "
                      u"section of a page instead of the default description."),
        required=False
        )

    form.widget('seo_robots',
                AjaxSelectFieldWidget,
                vocabulary = "seofields.robots")
    seo_robots = schema.Tuple(
        title=_(u'Metatag Robots'),
        description=_(u'Select options that hint search engines how '
                      u'to treat this content.'),
        value_type=schema.Choice(
            title=_(u'Available options'),
            vocabulary="seofields.robots"
        ),
        required=False
    )

@implementer(ISEOFields)
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

    @property
    def seo_robots(self):
        if hasattr(self.context, 'seo_robots'):
            return self.context.seo_robots
        return None

    @seo_robots.setter
    def seo_robots(self, value):
        self.context.seo_robots = value
