from collective.behavior.seo.behaviors.seo_fields import SEOFields
from collective.behavior.seo.testing import COLLECTIVE_BEHAVIOR_SEO_INTEGRATION_TESTING
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

import unittest


class BaseViewletIntegrationTest(unittest.TestCase):

    layer = COLLECTIVE_BEHAVIOR_SEO_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        self.app = self.layer["app"]

        setRoles(self.portal, TEST_USER_ID, ["Manager"])

        self.portal.invokeFactory(
            "Document",
            id="page",
            title="Test default page",
            description="a description",
        )

        self.portal.invokeFactory(
            "News Item",
            id="news",
            title="News Item",
            description="a description",
        )

        self.page = self.portal.page

        self.news = self.portal.news

    def _invalidateRequestMemoizations(self):
        try:
            del self.app.REQUEST.__annotations__
        except AttributeError:
            pass


class MetaFieldsViewletIntegrationTest(BaseViewletIntegrationTest):

    def test_viewlet(self):

        from collective.behavior.seo.browser.metafields import MetaFieldsViewlet

        self._invalidateRequestMemoizations()

        self.app.REQUEST["ACTUAL_URL"] = self.page.absolute_url()

        viewlet = MetaFieldsViewlet(self.page, self.app.REQUEST, None)
        viewlet.update()
        self.assertTrue(viewlet.metatags == [("description", "a description")])

        # now we set the seo description

        adapter = SEOFields(self.page)
        self.assertTrue(adapter.seo_title is None)
        self.assertTrue(adapter.seo_description is None)
        self.assertTrue(adapter.seo_robots is None)

        # set properties via adapter
        adapter.seo_description = "Another seo description"

        self._invalidateRequestMemoizations()
        viewlet.update()
        self.assertTrue(
            viewlet.metatags == [("description", "Another seo description")]
        )


class MetaRobotsViewletIntegrationTest(BaseViewletIntegrationTest):

    def test_viewlet_contenttype_with_seo_behavior(self):

        from collective.behavior.seo.browser.metarobots import MetaRobotsViewlet

        self._invalidateRequestMemoizations()

        self.app.REQUEST["ACTUAL_URL"] = self.page.absolute_url()

        viewlet = MetaRobotsViewlet(self.page, self.app.REQUEST, None)
        viewlet.update()

        self.assertTrue(viewlet.behavior is not None)
        self.assertTrue(viewlet.available())

    def test_viewlet_contenttype_without_seo_behavior(self):

        from collective.behavior.seo.browser.metarobots import MetaRobotsViewlet

        self._invalidateRequestMemoizations()

        self.app.REQUEST["ACTUAL_URL"] = self.news.absolute_url()

        viewlet = MetaRobotsViewlet(self.news, self.app.REQUEST, None)
        viewlet.update()

        self.assertTrue(viewlet.behavior is None)
        self.assertTrue(viewlet.available() is False)
