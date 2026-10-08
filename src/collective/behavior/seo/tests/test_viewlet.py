from collective.behavior.seo.behaviors.seo_fields import SEOFields
from collective.behavior.seo.testing import COLLECTIVE_BEHAVIOR_SEO_FUNCTIONAL_TESTING
from collective.behavior.seo.testing import COLLECTIVE_BEHAVIOR_SEO_INTEGRATION_TESTING
from collective.behavior.seo.testing import (
    COLLECTIVE_BEHAVIOR_SEO_WITH_ADAPTER_INTEGRATION_TESTING,
)
from collective.behavior.seo.tests import TEST_SCHEMA_JSON_LD_LIST
from collective.behavior.seo.tests import TEST_SCHEMA_JSON_LD_OBJECT
from copy import deepcopy
from io import StringIO
from lxml import etree
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.testing.zope import Browser

import transaction
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

        self.portal.invokeFactory(
            "Folder",
            id="folder",
            title="Folder",
            description="a description",
        )

        self.page = self.portal.page

        self.news = self.portal.news

        self.folder = self.portal.folder

    def _invalidateRequestMemoizations(self):
        try:
            del self.app.REQUEST.__annotations__
        except AttributeError:
            pass


class BaseViewletWithAdapterIntegrationTest(unittest.TestCase):

    layer = COLLECTIVE_BEHAVIOR_SEO_WITH_ADAPTER_INTEGRATION_TESTING

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

        self.portal.invokeFactory(
            "Folder",
            id="folder",
            title="Folder",
            description="a description",
        )

        self.page = self.portal.page

        self.news = self.portal.news

        self.folder = self.portal.folder


class MetaFieldsViewletIntegrationTest(BaseViewletIntegrationTest):

    def test_viewlet_contenttype_with_seo_behavior(self):

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

    def test_viewlet_contenttype_without_seo_behavior(self):

        from collective.behavior.seo.browser.metafields import MetaFieldsViewlet

        self._invalidateRequestMemoizations()

        self.app.REQUEST["ACTUAL_URL"] = self.news.absolute_url()

        viewlet = MetaFieldsViewlet(self.news, self.app.REQUEST, None)
        viewlet.update()
        self.assertTrue(list(viewlet.metatags) == [("description", "a description")])


class MetaRobotsViewletIntegrationTest(BaseViewletIntegrationTest):

    def test_viewlet_contenttype_with_seo_behavior(self):

        from collective.behavior.seo.browser.metarobots import MetaRobotsViewlet

        self._invalidateRequestMemoizations()

        self.app.REQUEST["ACTUAL_URL"] = self.page.absolute_url()

        viewlet = MetaRobotsViewlet(self.page, self.app.REQUEST, None)
        viewlet.update()

        self.assertTrue(viewlet.behavior is not None)
        self.assertTrue(viewlet.available())
        self.assertTrue(viewlet.content() == "all")

        adapter = SEOFields(self.page)
        adapter.seo_robots = "index, follow"

        viewlet = MetaRobotsViewlet(self.page, self.app.REQUEST, None)
        viewlet.update()
        self.assertTrue(viewlet.content() == "index, follow")

    def test_viewlet_contenttype_without_seo_behavior(self):

        from collective.behavior.seo.browser.metarobots import MetaRobotsViewlet

        self._invalidateRequestMemoizations()

        self.app.REQUEST["ACTUAL_URL"] = self.news.absolute_url()

        viewlet = MetaRobotsViewlet(self.news, self.app.REQUEST, None)
        viewlet.update()

        self.assertTrue(viewlet.behavior is None)
        self.assertTrue(viewlet.available() is False)


class TitleViewletIntegrationTest(BaseViewletIntegrationTest):

    def test_viewlet_contenttype_with_seo_behavior(self):

        from collective.behavior.seo.browser.title import TitleViewlet

        self._invalidateRequestMemoizations()

        self.app.REQUEST["ACTUAL_URL"] = self.page.absolute_url()

        viewlet = TitleViewlet(self.page, self.app.REQUEST, None)
        viewlet.update()
        self.assertTrue(viewlet.site_title == "Test default page &mdash; Plone site")

        # now we set the seo title
        adapter = SEOFields(self.page)
        adapter.seo_title = "Big & Bäng"

        self._invalidateRequestMemoizations()
        viewlet.update()
        self.assertTrue(viewlet.site_title == "Big &amp; Bäng")

    def test_viewlet_contenttype_without_seo_behavior(self):

        from collective.behavior.seo.browser.title import TitleViewlet

        self._invalidateRequestMemoizations()

        self.app.REQUEST["ACTUAL_URL"] = self.news.absolute_url()

        viewlet = TitleViewlet(self.news, self.app.REQUEST, None)
        viewlet.update()
        self.assertTrue(viewlet.site_title == "News Item &mdash; Plone site")


class StructuredDataViewletIntegrationTest(BaseViewletIntegrationTest):

    def test_viewlet_contenttype_with_seo_behavior(self):

        from collective.behavior.seo.browser.structured_data import (
            StructuredDataViewlet,
        )

        self.app.REQUEST["ACTUAL_URL"] = self.page.absolute_url()

        viewlet = StructuredDataViewlet(self.page, self.app.REQUEST, None)

        self.assertTrue(viewlet.structured_data == "")

        # now we set the seo structured data

        # first a json object
        adapter = SEOFields(self.page)
        adapter.seo_structured_data = TEST_SCHEMA_JSON_LD_OBJECT

        viewlet = StructuredDataViewlet(self.page, self.app.REQUEST, None)

        self.assertTrue("John Doe" in viewlet.structured_data)

        # second a json list of objects
        adapter = SEOFields(self.page)
        adapter.seo_structured_data = TEST_SCHEMA_JSON_LD_LIST

        viewlet = StructuredDataViewlet(self.page, self.app.REQUEST, None)

        self.assertTrue("Jane Doe" in viewlet.structured_data)

    def test_viewlet_contenttype_without_seo_behavior(self):

        from collective.behavior.seo.browser.structured_data import (
            StructuredDataViewlet,
        )

        self.app.REQUEST["ACTUAL_URL"] = self.news.absolute_url()

        viewlet = StructuredDataViewlet(self.news, self.app.REQUEST, None)

        self.assertFalse(viewlet.available())

    def test_viewlet_json_escape(self):

        from collective.behavior.seo.browser.structured_data import (
            StructuredDataViewlet,
        )

        self.app.REQUEST["ACTUAL_URL"] = self.page.absolute_url()

        viewlet = StructuredDataViewlet(self.page, self.app.REQUEST, None)

        self.assertTrue(viewlet.structured_data == "")

        # now we set the seo structured data

        # first a json object
        adapter = SEOFields(self.page)
        adapter.seo_structured_data = TEST_SCHEMA_JSON_LD_OBJECT

        viewlet = StructuredDataViewlet(self.page, self.app.REQUEST, None)
        self.assertTrue("\\u003c \\u0026 \\u003e" in viewlet.structured_data)


class StructuredDataViewletWithAdapterIntegrationTest(
    BaseViewletWithAdapterIntegrationTest
):

    def test_viewlet_adapter_resolution(self):

        from collective.behavior.seo.browser.structured_data import (
            StructuredDataViewlet,
        )

        # test injected structured data via adapter "json-ld-variant1"
        viewlet = StructuredDataViewlet(self.page, self.app.REQUEST, None)
        self.assertTrue("Plone Foundation" in viewlet.structured_data)

        # test inject structured data via adapter "json-ld-variant2"
        viewlet = StructuredDataViewlet(self.folder, self.app.REQUEST, None)
        self.assertTrue("Plone Team" in viewlet.structured_data)

    def test_viewlet_broken_adapter_resolution(self):

        from collective.behavior.seo.browser.structured_data import (
            StructuredDataViewlet,
        )
        from collective.behavior.seo.tests import IDummyContent
        from zope.interface import alsoProvides

        alsoProvides(self.page, IDummyContent)

        # test injected structured data via adapter "json-ld-variant1"

        # test injected structured data via adapter "json-ld-variant3"
        # the adapter is broken, but the viewlet should be rendered
        viewlet = StructuredDataViewlet(self.page, self.app.REQUEST, None)
        self.assertTrue("Plone Foundation" in viewlet.structured_data)

    def test_viewlet_adapter_resolution_and_behavior_field(self):

        from collective.behavior.seo.browser.structured_data import (
            StructuredDataViewlet,
        )

        # now we set the seo structured data
        adapter = SEOFields(self.page)
        adapter.seo_structured_data = TEST_SCHEMA_JSON_LD_LIST

        viewlet = StructuredDataViewlet(self.page, self.app.REQUEST, None)

        # data from seo field
        self.assertTrue("Jane Doe" in viewlet.structured_data)

        # data from adapter
        self.assertTrue("Plone Foundation" in viewlet.structured_data)


class StructuredDataViewletFunctionalTest(unittest.TestCase):

    layer = COLLECTIVE_BEHAVIOR_SEO_FUNCTIONAL_TESTING

    def setUp(self):
        self.app = self.layer["app"]
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        self.setUpContent()

    def setUpContent(self):

        PAYLOAD = [
            {
                "type": "Document",
                "id": "page",
                "title": "Default Page",
                "description": "a page with data in structured data field",
            },
            {
                "type": "Document",
                "id": "another_page",
                "title": "Default Page",
                "description": "a page without data in structured data field",
            },
            {
                "type": "Folder",
                "id": "folder",
                "title": "Default Page",
                "description": "a page without data in structured data field",
            },
            {
                "type": "News Item",
                "id": "news",
                "title": "A News Item",
                "description": "a description",
            },
        ]

        payload = deepcopy(PAYLOAD[0])
        self.page = api.content.create(container=self.portal, **payload)

        payload = deepcopy(PAYLOAD[1])
        self.another_page = api.content.create(container=self.portal, **payload)

        payload = deepcopy(PAYLOAD[2])
        self.news = api.content.create(container=self.portal, **payload)

        adapter = SEOFields(self.page)
        adapter.seo_structured_data = TEST_SCHEMA_JSON_LD_LIST

        transaction.commit()

    def test_viewlet_contenttype_with_seo_behavior(self):

        browser = Browser(self.layer["app"])
        browser.handleErrors = False
        browser.open(self.page.absolute_url())

        tree = etree.parse(StringIO(browser.contents), etree.HTMLParser())
        result = tree.xpath("//*[@type='application/ld+json']")
        self.assertTrue(
            len(result) == 1, "Structured Data Viewlet should be available!"
        )

    def test_viewlet_contenttype_without_seo_behavior(self):

        browser = Browser(self.layer["app"])
        browser.handleErrors = False
        browser.open(self.news.absolute_url())

        tree = etree.parse(StringIO(browser.contents), etree.HTMLParser())
        result = tree.xpath("//*[@type='application/ld+json']")
        self.assertTrue(
            len(result) == 0, "Structured Data Viewlet should be available!"
        )

    def test_viewlet_with_data(self):
        import json

        browser = Browser(self.layer["app"])
        browser.handleErrors = False
        browser.open(self.page.absolute_url())

        tree = etree.parse(StringIO(browser.contents), etree.HTMLParser())
        result = tree.xpath("//*[@type='application/ld+json']")
        self.assertTrue(
            len(result) == 1, "Structured Data Viewlet should be available!"
        )

        elem = result[0]
        data = json.loads(elem.text)
        self.assertListEqual(data, TEST_SCHEMA_JSON_LD_LIST)

    def test_viewlet_without_data(self):
        browser = Browser(self.layer["app"])
        browser.handleErrors = False
        browser.open(self.another_page.absolute_url())

        tree = etree.parse(StringIO(browser.contents), etree.HTMLParser())
        result = tree.xpath("//*[@type='application/ld+json']")
        self.assertTrue(
            len(result) == 0, "Structured Data Viewlet should not be available!"
        )
