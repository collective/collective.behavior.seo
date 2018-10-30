from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IVocabularyFactory
from zope.interface import implements
from plone import api
from collective.behavior.seo.interfaces import ICollectiveBehaviorSeoSettings


class RobotsVocabulary(object):
    implements(IVocabularyFactory)

    def __call__(self, context):

        items = []
        tags = api.portal.get_registry_record(
            'robot_tags',
            interface=ICollectiveBehaviorSeoSettings,
            default=u'index, follow')
        for tag in tags:
            items.append(SimpleTerm(tag, tag, tag))

        return SimpleVocabulary(items)


RobotsVocabularyFactory = RobotsVocabulary()
