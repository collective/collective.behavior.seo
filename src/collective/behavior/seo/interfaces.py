"""Module where all interfaces, events and exceptions live."""

from collective.behavior.seo import _
from zope import schema
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class ISEOFieldsMarker(Interface):
    """Marker interface that will be provided by instances using the
    ISeoFields behavior.
    """


class ICollectiveBehaviorSeoLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class ICollectiveBehaviorSeoSettings(Interface):

    robot_tags = schema.Tuple(
        title=_("Robot Tags"),
        description=_(
            "robot_tags_desc",
            default=(
                "Enter combinations of robot tags, separated by comma's one "
                "combination on every line. The idea here is that the "
                "webmaster decides which combinations of multiple tags are "
                "sane, so that content editors don't need to compose logical "
                "combinations themselves from all individual tags."
            ),
        ),
        value_type=schema.TextLine(),
        default=("index, nofollow", "noindex, follow", "index, follow"),
    )
