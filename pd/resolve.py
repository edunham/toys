#!/usr/bin/env python3

# based on example from https://github.com/PagerDuty/API_Python_Examples/tree/master/EVENTS_API_v2

import json
import requests
import os
import sys

ROUTING_KEY = os.environ['PAGERDUTY_SERVICE_KEY']
INCIDENT_KEY = sys.argv[1] 

def resolve_incident():
    # Triggers a PagerDuty incident without a previously generated incident key
    # Uses Events V2 API - documentation: https://v2.developer.pagerduty.com/docs/send-an-event-events-api-v2

    header = {
        "Content-Type": "application/json"
    }

    payload = { # Payload is built with the least amount of fields required to trigger an incident
        "routing_key": ROUTING_KEY, 
        "event_action": "resolve",
        "dedup_key": INCIDENT_KEY
    }

    response = requests.post('https://events.pagerduty.com/v2/enqueue', 
                            data=json.dumps(payload),
                            headers=header)
	
    if response.json()["status"] == "success":
        print('Incident Resolved ')
    else:
        print(response.text) # print error message if not successful

if __name__ == '__main__':
    resolve_incident()

