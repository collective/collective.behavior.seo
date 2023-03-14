from collective.behavior.seo.interfaces import ICollectiveBehaviorSeoSettings
from plone import api
from zope.interface import implementer
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


@implementer(IVocabularyFactory)
class RobotsVocabulary(object):
    def __call__(self, context):

        items = []
        tags = api.portal.get_registry_record(
            "robot_tags",
            interface=ICollectiveBehaviorSeoSettings,
            default=u"index, follow",
        )
        for tag in tags:
            items.append(SimpleTerm(tag, tag, tag))

        return SimpleVocabulary(items)


RobotsVocabularyFactory = RobotsVocabulary()
