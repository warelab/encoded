from locust import HttpLocust, TaskSet
import re

def login(l):
    l.client.post("/login", {"username":"test", "password":"testpass"})

def index(l):
	getFile = open('acess.log', 'r')
	for line in getFile:
		match = re.findall(r'\"(.+?)\"', line)
		if match and 'GET' in match[0]:
                if not any(term in match[0] for term in ['limit=all', 'icon', '.png', '.ico', '@download']):
                    arr.append(base_url + match[0].split()[1])
    	l.client.get("/files/ENCFF445ANP")

def profile(l):
    l.client.get("/profile")

class UserBehavior(TaskSet):
    tasks = {index:2, profile:1}

    def on_start(self):
        login(self)

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait=5000
    max_wait=9000