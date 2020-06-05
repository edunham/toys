#!/usr/bin/env python3

# based on example from https://github.com/PagerDuty/API_Python_Examples/tree/master/EVENTS_API_v2

import json
import requests
import os
import platform
from datetime import datetime

ROUTING_KEY = os.environ['PAGERDUTY_SERVICE_KEY']


def trigger_incident():
    # Triggers a PagerDuty incident without a previously generated incident key
    # Uses Events V2 API - documentation:
    # https://v2.developer.pagerduty.com/docs/send-an-event-events-api-v2

    header = {
        "Content-Type": "application/json"
    }

    payload = {
        "routing_key": ROUTING_KEY,
        "event_action": "trigger",
        "payload": {
            "summary": "hello from " + os.getlogin() + " at " + datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            "source": platform.node(),
            "severity": "critical",
            "incident_key": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            "assignments": [{
                "assignee": {
                    "id": "PGPG5GB",  # had to dig that one out of the URL
                    "type": "user_reference"
                }
            }],
            "body": {
                "type": "incident_body",
                "details": "On the barren shore, and on the lofty ice barrier in the background, myriads of grotesque penguins squawked and flapped their fins; while many fat seals were visible on the water, swimming or sprawling across large cakes of slowly drifting ice."
            }
        }
    }

    response = requests.post('https://events.pagerduty.com/v2/enqueue',
                             data=json.dumps(payload),
                             headers=header)

    if response.json()["status"] == "success":
        print(
            'Incident created with with dedup key (also known as incident / alert key) of ' +
            '"' +
            response.json()['dedup_key'] +
            '"')
    else:
        print(response.text)  # print error message if not successful


if __name__ == '__main__':
    trigger_incident()
