from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing.zope import WSGI_SERVER_FIXTURE

import collective.behavior.seo


class CollectiveBehaviorSeoLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=collective.behavior.seo)

    def setUpPloneSite(self, portal):
        applyProfile(portal, "collective.behavior.seo:default")


COLLECTIVE_BEHAVIOR_SEO_FIXTURE = CollectiveBehaviorSeoLayer()


COLLECTIVE_BEHAVIOR_SEO_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_BEHAVIOR_SEO_FIXTURE,),
    name="CollectiveBehaviorSeoLayer:IntegrationTesting",
)


COLLECTIVE_BEHAVIOR_SEO_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_BEHAVIOR_SEO_FIXTURE, WSGI_SERVER_FIXTURE),
    name="CollectiveBehaviorSeoLayer:FunctionalTesting",
)
