from ..interfaces import ISEOFieldsMarker
from plone.app.layout.viewlets import common


class MetaFieldsViewlet(common.DublinCoreViewlet):
    """ """

    def update(self):
        super().update()

        if ISEOFieldsMarker.providedBy(self.context):
            self.metatags = dict(
                self.metatags
            )  # Convert to a dictionary for faster lookups

            if self.context.seo_description:
                self.metatags["description"] = self.context.seo_description

            if self.context.seo_keywords:
                self.metatags["keywords"] = self.context.seo_keywords

            if self.context.seo_keywords:
                self.metatags["distribution"] = self.context.seo_distribution
                self.metatags[
                    "DC:distribution"
                ] = self.context.seo_distribution

            # if self.context.seo_custom_metatags:
            #     import pdb;pdb.set_trace()
            #     for item in self.context.seo_custom_metatags:
            #         self.metatags[item["name"]] = item["value"]

            self.metatags = list(
                self.metatags.items()
            )  # Convert back to a list of tuples
