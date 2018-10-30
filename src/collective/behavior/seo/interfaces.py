# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from zope import schema

from collective.behavior.seo import _
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class ISEOFieldsMarker(Interface):
    """ Marker interface that will be provided by instances using the
        ISeoFields behavior.
    """


class ICollectiveBehaviorSeoLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class ICollectiveBehaviorSeoSettings(Interface):

    robot_tags = schema.Tuple(
        title=_(u"Robot Tags"),
        description=_(
            u'robot_tags_desc',
            default=(
                u"Enter combinations of robot tags, separated by comma's one "
                u"combination on every line. The idea here is that the "
                u"webmaster decides which combinations of multiple tags are "
                u"sane, so that content editors don't need to compose logical "
                u"combinations themselves from all individuall tags."

            )
        ),
        value_type=schema.TextLine(),
        default=(u"index, nofollow",
                 u"noindex, follow",
                 u"index, follow")
    )
