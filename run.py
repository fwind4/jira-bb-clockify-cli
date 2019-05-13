

import requests
import subprocess
import json
import sys

with open('config.local.json') as json_file:  
    conf = json.load(json_file)

if len(sys.argv) == 1 or sys.argv[1] == '-h' :
    print('\
        Usage: \n\
        python run.py [OPTIONS] <issue number> | <issue prefix>-<issue number>\n\
            ex: python run.py 721\n \
                python run.py BER-721\n \
                \n\
            -p <issue prefix> - Prepends issue prefix. \n\
                                ex: python run.py -p BER 721\n\
            -c                - Don\'t start Clockify\n')
    exit()

argc = 1
isClockify = True
issue = ''
branchPre = None
while argc < (len(sys.argv)-1) :
    if sys.argv[argc] == '-p' :
        argc += 1
        issue += sys.argv[argc].upper()
    elif sys.argv[argc] == '-b' :
        argc += 1
        branchPre = sys.argv[argc]
    elif sys.argv[argc] == '-c' :
    
        noClockify = False
    elif '-' in sys.argv[argc] :
        issue += sys.argv[argc] 
    elif argc == 1:
        issue += conf['jiraIssuePrefix']
    argc += 1

issue += '-' + sys.argv[argc]

url = 'https://'+conf['jiraId']+'.atlassian.net/rest/api/latest/issue/' + issue
r = requests.get(url, auth=(conf['jiraEmail'], conf['jiraToken']))

if r.status_code == 200 :
    summary = r.json()['fields']['summary']
    print(issue + ': ' + summary)
else :
    print('No such issue or bad auth.')
    exit()

if branchPre is None :
    branchPre = conf['branchPrefix']

summary = summary.lower().replace(' ', '-')
summary = summary.encode('ascii',errors='ignore').decode()
branch = branchPre + '/' + issue + '-' + summary
branch = branch[:47]
#print(branch)

res = subprocess.run(['git', 'checkout', '-b', branch])
if res.returncode != 0 :
    res = subprocess.run(['git', 'checkout', branch])

print(res.returncode)