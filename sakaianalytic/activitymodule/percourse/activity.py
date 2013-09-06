import sys
import json

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

@event_handler()
def event_type_histogram(mongodb, events):
    collection = mongodb['event_types']
    for evt in events: 
        event_type = evt['event_type']
        if event_type.split('.')[0] == 'sakai': 
            collection.update(
                {'event_type': event_type}, 
                {'$inc':{'count': 1}}, 
                True, 
                False
            )

@query()
def plot_histogram(mongodb):
    histogram = list(mongodb['course_activity'].find())
    histogram = [{'count' : e['count'], 
                  'course' : e['course']} for e in histogram]
    histogram.sort(lambda x,y:cmp(y['count'], x['count']))
    return histogram

@query()
def event_type_query(mongodb):
    histogram = list(mongodb['event_types'].find())
    histogram = [{'count' : e['count'], 
                  'event_type' : e['event_type']} for e in histogram]
    histogram.sort(key=lambda x: x['count'], reverse=True)
    return histogram

@view()
def plot_histogram(query):
    from edinsights.core.render import render
    return render("courseviews.html", {'data':json.dumps(query.plot_histogram())})

@view()
def plot_event_type_histogram(query):
    from edinsights.core.render import render
    return render("event_types.html", {'data':json.dumps(query.event_type_query())})
