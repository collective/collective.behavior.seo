from collective.behavior.seo.interfaces import ISEOFieldsMarker
from collective.behavior.seo.testing import (  # noqa
    COLLECTIVE_BEHAVIOR_SEO_INTEGRATION_TESTING,
)
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
