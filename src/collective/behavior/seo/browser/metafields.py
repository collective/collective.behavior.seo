from ..interfaces import ISEOFieldsMarker
from plone.app.layout.viewlets import common


class MetaFieldsViewlet(common.DublinCoreViewlet):
    """ """

    def update(self):
        super().update()

        if ISEOFieldsMarker.providedBy(self.context):
            # in python3 this is a dict_items instance
            self.metatags = list(self.metatags)
            if self.context.seo_description:
                for index, (key, value) in enumerate(self.metatags):
                    if key == "description":
                        self.metatags.pop(index)
                        break

                self.metatags.append(("description", self.context.seo_description))
