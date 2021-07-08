from plone.app.layout.viewlets.common import ViewletBase
from plone.event.interfaces import IEventAccessor
from plone.app.uuid.utils import uuidToObject
from plone import api
import json
import pkg_resources


try:
    pkg_resources.get_distribution('collective.address')
except pkg_resources.DistributionNotFound:
    HAS_VENUE = False
else:
    from collective.venue.interfaces import IVenueEnabled
    from collective.address.vocabulary import get_pycountry_name
    HAS_VENUE = True


class StructuredDataBaseViewlet(ViewletBase):
    """Base viewlet to render content metadata as JSON-LD
    """

    def data(self):
        metadata = {}
        metadata["@context"] = "https://schema.org",
        return metadata


    def render(self):
        """Render content metadata as JSON-LD
        """

        return u"<script>{metadata}</script>".format(
            metadata=json.dumps(self.data())
        )


class StructuredDataArticleViewlet(StructuredDataBaseViewlet):
    """Viewlet to render article-like content metadata as JSON-LD
    """

    def data(self):
        metadata = {}
        metadata["@context"] = "https://schema.org",
        metadata["@type"] = "NewsArticle",

        metadata["headline"] = self.context.title
        metadata["description"] = self.context.description

        if getattr(self.context, "image", None):
            scale_util = api.content.get_view("images", self.context, self.request)
            scale = scale_util.scale("image", scale="large")
            metadata["image"] = scale.url

        if self.context.modification_date:
            metadata["dateModified"] = self.context.ModificationDate()

        if self.context.effective_date:
            metadata["datePublished"] = self.context.EffectiveDate()

        return metadata


class StructuredDataEventViewlet(StructuredDataBaseViewlet):
    """Viewlet to render event-like content metadata as JSON-LD
    """

    def data(self):
        metadata = {}
        metadata["@context"] = "https://schema.org",
        metadata["@type"] = "Event",

        metadata["name"] = self.context.title
        metadata["description"] = self.context.description

        if getattr(self.context, "image", None):
            scale_util = api.content.get_view("images", self.context, self.request)
            scale = scale_util.scale("image", scale="large")
            metadata["image"] = scale.url

        if self.context.start:
            metadata["startDate"] = IEventAccessor(self.context).start.isoformat()
        if self.context.end:
            metadata["endDate"] = IEventAccessor(self.context).end.isoformat()

        if getattr(self.context, "location", None):
            metadata["location"] = {
                "@type": "Place",
                "name": self.context.location,
            }

        if HAS_VENUE and IVenueEnabled.providedBy(self.context) and getattr(self.context, "location_uid", None):
            venue = uuidToObject(self.context.location_uid)
            if venue:
                metadata["location"] = {
                    "@type": "Place",
                    "name": venue.title,
                }

                address = {}
                if getattr(venue, "street", None):
                    address["street"] = venue.street
                if getattr(venue, "zip_code", None):
                    address["postalCode"] = venue.zip_code
                if getattr(venue, "city", None):
                    address["addressLocality"] = venue.city
                if getattr(venue, "country", None):
                    address["addressCountry"] = get_pycountry_name(venue.country)

                if "address":
                    address["@type"] = "PostalAddress"
                    metadata["location"]["address"] = address

        return metadata
