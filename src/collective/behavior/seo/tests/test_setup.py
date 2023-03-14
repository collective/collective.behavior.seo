"""Setup tests for this package."""
from collective.behavior.seo.testing import (  # noqa
    COLLECTIVE_BEHAVIOR_SEO_INTEGRATION_TESTING,
)
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

import unittest


try:
    from plone.base.utils import get_installer
except ImportError:
    from Products.CMFPlone.utils import get_installer


class TestSetup(unittest.TestCase):
    """Test that collective.behavior.seo is properly installed."""

    layer = COLLECTIVE_BEHAVIOR_SEO_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        self.installer = get_installer(self.portal)

    def test_product_installed(self):
        """Test if collective.behavior.seo is installed."""
        self.assertTrue(self.installer.is_product_installed("collective.behavior.seo"))

    def test_browserlayer(self):
        """Test that ICollectiveBehaviorSeoLayer is registered."""
        from collective.behavior.seo.interfaces import ICollectiveBehaviorSeoLayer
        from plone.browserlayer import utils

        self.assertIn(ICollectiveBehaviorSeoLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = COLLECTIVE_BEHAVIOR_SEO_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        self.installer = get_installer(self.portal)
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        self.installer.uninstall_product("collective.behavior.seo")
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if collective.behavior.seo is cleanly uninstalled."""
        self.assertFalse(self.installer.is_product_installed("collective.behavior.seo"))

    def test_browserlayer_removed(self):
        """Test that ICollectiveBehaviorSeoLayer is removed."""
        from collective.behavior.seo.interfaces import ICollectiveBehaviorSeoLayer
        from plone.browserlayer import utils

        self.assertNotIn(ICollectiveBehaviorSeoLayer, utils.registered_layers())
