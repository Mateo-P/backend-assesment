from __future__ import absolute_import, unicode_literals
from celery.utils.log import get_task_logger
#from models import Agent, Leg, Itinerary
from celery import shared_task
from utils.dataload import load_json


logger = get_task_logger(__name__)

# Create your tasks here

@shared_task(bind=True, track_started=True)
def data_load_info(self):
    data = load_json()
    legs = data['legs']
    intineraries = ['itineraries']
    print(legs)
    
    return "Celery has imported {0} tweets from Twitter.".format(len(data))
