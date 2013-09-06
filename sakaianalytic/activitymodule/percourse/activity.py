import sys

from edinsights.core.decorators import event_handler, view, query

@event_handler()
def dump_to_db(mongodb, events):
    ## TODO: Error handling
    print "Got a message"
    collection = mongodb['event_log']
    collection.insert([e.event for e in events])

@event_handler()
def histogram(mongodb, events):
    collection = mongodb['course_activity']
    for evt in events: 
        event_type = evt['event_type']
        if event_type.split('.')[0] == 'sakai': 
            course = evt['course']
            collection.update({'course':course}, 
                              {'$inc':{'count':1}}, 
                              True, 
                              False)
            print "Got a message", evt
            
@view()
def plot_histogram(mongodb):
    histogram = list(mongodb['course_activity'].find())
    return str(histogram)
