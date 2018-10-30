from plone.app.layout.viewlets import common
from ..interfaces import ISEOFieldsMarker


class MetaFieldsViewlet(common.DublinCoreViewlet):
    """
    """

    def update(self):
        super(MetaFieldsViewlet, self).update()

        if ISEOFieldsMarker.providedBy(self.context):

            if self.context.seo_description:
                for index, (key, value) in enumerate(self.metatags):
                    if key == 'description':
                        self.metatags.pop(index)
                        break
                self.metatags.append(
                    ('description', self.context.seo_description))
