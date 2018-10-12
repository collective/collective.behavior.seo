# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from zope.interface import Interface


class ISEOFieldsMarker(Interface):
    """ Marker interface that will be provided by instances using the
        ISeoFields behavior.
    """

class ICollectiveBehaviorSeoLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""
