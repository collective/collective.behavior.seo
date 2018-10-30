# -*- coding: utf-8 -*-
from plone.app.layout.viewlets import common
from ..interfaces import ISEOFieldsMarker
import logging


logger = logging.getLogger("collective.behavior.seo")

# Code mostly reused from https://github.com/simplesconsultoria/sc.seo


class MetaRobotsViewlet(common.ViewletBase):
    """Renders the  <meta name="robots"> tag if the IMetaRobots is applied
       to the context
    """

    def update(self):
        super(MetaRobotsViewlet, self).update()
        try:
            self.behavior = ISEOFieldsMarker(self.context)
        except TypeError:
            self.behavior = None

    def available(self):
        return True if self.behavior else False

    def content(self):
        content = self.behavior.seo_robots
        # If there is no restriction, we explicity allow indexing
        if not content:
            return 'all'
        return content
