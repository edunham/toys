#!/usr/bin/env python
#
# Copyright (c) 2016, PagerDuty, Inc. <info@pagerduty.com>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of PagerDuty Inc nor the
#       names of its contributors may be used to endorse or promote products
#       derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL PAGERDUTY INC BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import requests
import sys

# Update to match your API key
API_KEY = ''

QUERY = ''
TEAM_IDS = []
INCLUDE = []
HEADERS = {
        'Accept': 'application/vnd.pagerduty+json;version=2',
        'Authorization': 'Token token={token}'.format(token=API_KEY)
        }

USERS = {} 

def populate_list(offset):
    url = 'https://api.pagerduty.com/users'
    payload = {
        'query': QUERY,
        'team_ids[]': TEAM_IDS,
        'include[]': INCLUDE,
        'limit': 100,
        'offset': offset 
    }
    r = requests.get(url, headers=HEADERS, params=payload)
    for u in r.json()['users']:
        USERS[u['name']] = u['id']
    #print(r.json()['limit'])
    if r.json()['more']:
         populate_list(offset + r.json()['limit'])

def print_contact_method(url):
    r = requests.get(url, headers=HEADERS)
    #print('Status Code: {code}'.format(code=r.status_code))
    print(r.json()['contact_method']['address'])

def print_user_info(user_id):
    url = 'https://api.pagerduty.com/users/' + user_id
    payload = {
        'include[]': [] 
    }
    r = requests.get(url, headers=HEADERS, params=payload)
    #print('Status Code: {code}'.format(code=r.status_code))
    contact_methods = r.json()['user']['contact_methods']
    for c in contact_methods:
        print_contact_method(c['self'])

def lookup_user(identifier):
    if ' ' in identifier:
        print_user_info(identifier)
    else:
        print_user_info(USERS[identifier])

if __name__ == '__main__':
    populate_list(0)
    if len(sys.argv) > 1:
        # they want to look up a person
        lookup_user(sys.argv[1])
    else:
        print(USERS)
