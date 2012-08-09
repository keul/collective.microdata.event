# -*- coding: utf8 -*-

from zope.interface import implements

from collective.microdata.event.interfaces import ISchemaOrgEvent
from collective.microdata.core.adapter import ThingMicrodataProvider

class EventMicrodataProvider(ThingMicrodataProvider):
    implements(ISchemaOrgEvent)
    
    def __init__(self, content):
        super(EventMicrodataProvider, self).__init__(content)
        self.microdata_vocabulary = 'http://schema.org/Event'
        self.attendees = content.getAttendees()
        self.startDate = content.start().ISO8601()
        self.endDate = content.end().ISO8601()
        self.duration = '%s/%s' % (self.startDate, self.endDate) 
        self.location = content.location
