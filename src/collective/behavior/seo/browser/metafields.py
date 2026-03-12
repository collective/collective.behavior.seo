from ..interfaces import ISEOFieldsMarker
from plone.app.layout.viewlets import common


class MetaFieldsViewlet(common.DublinCoreViewlet):
    """ """

    def update(self):
        super().update()

        if not ISEOFieldsMarker.providedBy(self.context):
            return

        self.metatags = list(self.metatags)

        if not self.context.seo_description:
            return

        for index, (key, value) in enumerate(self.metatags):
            if key == "description":
                self.metatags.pop(index)
                break

        self.metatags.append(("description", self.context.seo_description))
