from collective.behavior.seo.testing import COLLECTIVE_BEHAVIOR_SEO_INTEGRATION_TESTING
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from zope.component import getUtility
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary

import unittest


class TestVocabulary(unittest.TestCase):

    layer = COLLECTIVE_BEHAVIOR_SEO_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        self.app = self.layer["app"]

        setRoles(self.portal, TEST_USER_ID, ["Manager"])

    def test_vocabulary(self):
        vocab = getUtility(IVocabularyFactory, "seofields.robots")(self.portal)
        self.assertIsNotNone(vocab)
        self.assertIsInstance(vocab, SimpleVocabulary)

        title = token = "index, nofollow"
        term = vocab.getTerm(token)
        self.assertTrue(term.title == title)

        title = token = "noindex, follow"
        term = vocab.getTerm(token)
        self.assertTrue(term.title == title)

        title = token = "index, follow"
        term = vocab.getTerm(token)
        self.assertTrue(term.title == title)

    def test_vocabulary_with_custom_registry_entries(self):
        from plone import api

        api.portal.set_registry_record(
            "collective.behavior.seo.interfaces.ICollectiveBehaviorSeoSettings.robot_tags",
            (
                "a,a",
                " ",
                " ",
                "b,b",
                "c,c",
                "d",
                "b,b",
            ),
        )

        vocab = getUtility(IVocabularyFactory, "seofields.robots")(self.portal)

        title = token = "a,a"
        term = vocab.getTerm(token)
        self.assertTrue(term.title == title)

        title = token = "b,b"
        term = vocab.getTerm(token)
        self.assertTrue(term.title == title)

        title = token = "c,c"
        term = vocab.getTerm(token)
        self.assertTrue(term.title == title)

        self.assertTrue(len(vocab._terms) == 3)
