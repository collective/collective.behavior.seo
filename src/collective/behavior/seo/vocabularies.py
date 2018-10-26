from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IVocabularyFactory, IContextSourceBinder
from zope.component import getUtility
from zope.interface import implements
from z3c.formwidget.query.interfaces import IQuerySource

class BaseQueryVocabulary(object):
    implements(IVocabularyFactory, IQuerySource)

    vocab = None

    def update(self):
        raise NotImplementedError

    def __call__(self, context):
        self.vocab = self.update(context)
        return self

    def __contains__(self, term):
        return self.vocab.__contains__(term)

    def __iter__(self):
        return self.vocab.__iter__()

    def __nonzero__(self):
        return True

    def __len__(self):
        return self.vocab.__len__()

    def getTerm(self, value):
        return self.vocab.getTerm(value)

    def getTermByToken(self, value):
        return self.vocab.getTermByToken(value)

    def search(self, query_string):
        q = query_string.lower()
        return [x for x in self if x.title.lower().find(q) != -1]

ROBOTSVOCAB = SimpleVocabulary([
    SimpleTerm('noindex', 'noindex', u"noindex"),
    SimpleTerm('nofollow', 'nofollow', u"nofollow"),
    SimpleTerm('none', 'none', u"none"),
    SimpleTerm('noarchive', 'noarchive', u"noarchive"),
    SimpleTerm('nosnippet', 'nosnippet', u"nosnippet"),
    SimpleTerm('notranslate', 'notranslate', u"notranslate"),
    SimpleTerm('noimageindex', 'noimageindex', u"noimageindex"),
    SimpleTerm('unavailable_after', 'unavailable_after', u"unavailable after expiration"),
])


class RobotsVocabulary(BaseQueryVocabulary):

    def update(self, context):
        return ROBOTSVOCAB


RobotsVocabularyFactory = RobotsVocabulary()
