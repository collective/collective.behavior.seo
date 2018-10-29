from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IVocabularyFactory, IContextSourceBinder
from zope.component import getUtility
from zope.interface import implements
from plone import api
from collective.behavior.seo.interfaces import ICollectiveBehaviorSeoSettings
from plone.registry.interfaces import IRegistry


class RobotsVocabulary(object):
    implements(IVocabularyFactory)

    def __call__(self, context):

        registry = getUtility(IRegistry)
        items = []
        tags = api.portal.get_registry_record(
            'robot_tags',
            interface=ICollectiveBehaviorSeoSettings,
            default=u'index, follow')
        for tag in tags:
            items.append(SimpleTerm(tag, tag, tag))

        return SimpleVocabulary(items)

RobotsVocabularyFactory = RobotsVocabulary()
