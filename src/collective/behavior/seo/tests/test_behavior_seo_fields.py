from collective.behavior.seo.interfaces import ISEOFieldsMarker
from collective.behavior.seo.testing import COLLECTIVE_BEHAVIOR_SEO_INTEGRATION_TESTING
from copy import deepcopy
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.behavior.interfaces import IBehavior
from zope.component import getUtility

import unittest


class SeoFieldsIntegrationTest(unittest.TestCase):

    layer = COLLECTIVE_BEHAVIOR_SEO_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])

    def test_behavior_seo_fields(self):
        behavior = getUtility(IBehavior, "collective.behavior.seo.seo_fields")
        self.assertEqual(
            behavior.marker,
            ISEOFieldsMarker,
        )
        behavior_name = "collective.behavior.seo.behaviors.seo_fields.ISEOFields"
        behavior = getUtility(IBehavior, behavior_name)
        self.assertEqual(
            behavior.marker,
            ISEOFieldsMarker,
        )

    def test_behavior_unset_seo_fields_on_contenttype(self):
        """Behavior is enabled on contenttype"""

        from collective.behavior.seo.behaviors.seo_fields import SEOFields

        DOCUMENT_PAYLOAD = [
            {
                "type": "Document",
                "id": "page1",
                "title": "Page 1",
                "description": "a simple page",
            },
        ]

        payload = deepcopy(DOCUMENT_PAYLOAD[0])
        self.page = api.content.create(container=self.portal, **payload)

        adapter = SEOFields(self.page)
        self.assertTrue(adapter.seo_title is None)
        self.assertTrue(adapter.seo_description is None)
        self.assertTrue(adapter.seo_robots is None)

        # set properties via adapter
        adapter.seo_title = "Another seo title"
        adapter.seo_description = "Another seo description"
        adapter.seo_robots = "another term value"

        self.assertTrue(self.page.seo_title == "Another seo title")
        self.assertTrue(self.page.seo_description == "Another seo description")
        self.assertTrue(self.page.seo_robots == "another term value")

    def test_behavior_set_seo_fields_on_contenttype(self):
        """Behavior is enabled on contenttype"""

        from collective.behavior.seo.behaviors.seo_fields import SEOFields

        SEO_TITLE = "Seo Title"
        SEO_DESCRIPTION = "Seo Description"
        SEO_ROBOTS = "index, follow"

        DOCUMENT_PAYLOAD = [
            {
                "type": "Document",
                "id": "page1",
                "title": "Page 1",
                "description": "a simple page",
                "seo_title": SEO_TITLE,
                "seo_description": SEO_DESCRIPTION,
                "seo_robots": SEO_ROBOTS,
            },
        ]

        payload = deepcopy(DOCUMENT_PAYLOAD[0])
        self.page = api.content.create(container=self.portal, **payload)

        adapter = SEOFields(self.page)
        self.assertTrue(adapter.seo_title == SEO_TITLE)
        self.assertTrue(adapter.seo_description == SEO_DESCRIPTION)
        self.assertTrue(adapter.seo_robots == SEO_ROBOTS)

    def test_behavior_unset_seo_fields_on_wrong_contenttype(self):
        """Behavior is not enabled on contenttype"""

        from collective.behavior.seo.behaviors.seo_fields import SEOFields

        NEWS_ITEM_PAYLOAD = [
            {
                "type": "News Item",
                "id": "news",
                "title": "News Item",
                "description": "a simple news item",
            },
        ]

        payload = deepcopy(NEWS_ITEM_PAYLOAD[0])
        self.news = api.content.create(container=self.portal, **payload)

        adapter = SEOFields(self.news)
        self.assertTrue(adapter.seo_title is None)
        self.assertTrue(adapter.seo_description is None)
        self.assertTrue(adapter.seo_robots is None)
