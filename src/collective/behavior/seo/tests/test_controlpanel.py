"""Setup tests for this package."""

from collective.behavior.seo.testing import COLLECTIVE_BEHAVIOR_SEO_INTEGRATION_TESTING
from zope.component import getMultiAdapter

import unittest


class TestControlpanelIntgration(unittest.TestCase):

    layer = COLLECTIVE_BEHAVIOR_SEO_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        self.app = self.layer["app"]
        self.request = self.app.REQUEST

    def test_controlpanel(self):
        view = getMultiAdapter(
            (self.portal, self.request),
            name="collective_behavior_seo_settings",
        )
        self.assertTrue(view.__name__ == "collective_behavior_seo_settings")

        # call the view, this added the interface to the request
        view()
        self.assertTrue("robot_tags" in view.form_instance.fields.keys())
