from collective.z3cform.datagridfield.row import DictRow
from plone.autoform.directives import widget
from collective.behavior.seo import _
from plone import schema
from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.supermodel import model
from zope.component import adapter
from zope.interface import implementer
from zope.interface import provider, Interface
from collective.z3cform.datagridfield.datagridfield import DataGridFieldFactory


class ICustomMetatagsSchema(Interface):
    name = schema.TextLine(title=_("Name"))
    value = schema.TextLine(title=_("Value"))


@provider(IFormFieldProvider)
class ISEOFields(model.Schema):
    """ """

    model.fieldset(
        "seofields",
        label=_("SEO"),
        fields=(
            "seo_title",
            "seo_description",
            "seo_robots",
            "seo_keywords",
            "seo_distribution",
            "seo_canonical",
            "seo_custom_metatags",
        ),
    )

    seo_title = schema.TextLine(
        title=_("SEO Title"),
        description=_(
            "seo_title_help",
            default=(
                "Used in the web page 'head' section title and "
                "browser tab instead of the default title."
            ),
        ),
        required=False,
    )

    seo_description = schema.Text(
        title=_("SEO Description"),
        description=_(
            "seo_description_help",
            default=(
                "Used as meta description field in the 'head' section "
                "of a page instead of the default description."
            ),
        ),
        required=False,
    )

    seo_robots = schema.Choice(
        title=_("Metatag Robots"),
        description=_(
            "seo_robots_help",
            default=(
                "Select options that hint search engines how "
                "to treat this content. Typically listings are to "
                "navigate the site, but add little to no value in its "
                "own and should be set to 'noindex, follow'. In some "
                "cases you want a listing to be indexed. E.g. when "
                "publishing a Top 10 recipes list with extra content "
                "above and below the list, in which case you would use "
                "'index,follow'."
            ),
        ),
        vocabulary="seofields.robots",
        required=False,
    )

    seo_keywords = schema.TextLine(
        title=_("SEO Keywords"),
        description=_("Keywords separated by a comma."),
        required=False,
    )

    seo_distribution = schema.TextLine(
        title=_("SEO Distribution"),
        description=_("distribution and CD.distribution"),
        default="Global",
        required=False,
    )
    seo_canonical = schema.TextLine(
        title=_("SEO Canonical"),
        description=_("custom canonical link"),
        required=False,
    )

    seo_custom_metatags = schema.List(
        title=_("Custom metatags"),
        value_type=DictRow(title="metatag", schema=ICustomMetatagsSchema),
    )
    widget(seo_custom_metatags=DataGridFieldFactory)


@implementer(ISEOFields)
@adapter(IDexterityContent)
class SEOFields:
    def __init__(self, context):
        self.context = context

    @property
    def seo_title(self):
        if hasattr(self.context, "seo_title"):
            return self.context.seo_title
        return None

    @seo_title.setter
    def seo_title(self, value):
        self.context.seo_title = value

    @property
    def seo_description(self):
        if hasattr(self.context, "seo_description"):
            return self.context.seo_description
        return None

    @seo_description.setter
    def seo_description(self, value):
        self.context.seo_description = value

    @property
    def seo_robots(self):
        if hasattr(self.context, "seo_robots"):
            return self.context.seo_robots
        return None

    @seo_robots.setter
    def seo_robots(self, value):
        self.context.seo_robots = value

    @property
    def seo_keywords(self):
        if hasattr(self.context, "seo_keywords"):
            return self.context.seo_keywords
        return None

    @seo_keywords.setter
    def seo_keywords(self, value):
        self.context.seo_keywords = value

    @property
    def seo_distribution(self):
        if hasattr(self.context, "seo_distribution"):
            return self.context.seo_distribution
        return None

    @seo_distribution.setter
    def seo_distribution(self, value):
        self.context.seo_distribution = value

    @property
    def seo_canonical(self):
        if hasattr(self.context, "seo_canonical"):
            return self.context.seo_canonical
        return None

    @seo_canonical.setter
    def seo_canonical(self, value):
        self.context.seo_canonical = value

    @property
    def seo_custom_metatags(self):
        if hasattr(self.context, "seo_custom_metatags"):
            return self.context.seo_custom_metatags
        return None

    @seo_custom_metatags.setter
    def seo_custom_metatags(self, value):
        self.context.seo_custom_metatags = value
