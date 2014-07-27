#!/usr/bin/python

import urllib
import json
from pprint import pprint
from datetime import datetime

api_key = ""
notification_day = 2

todoist_link = 'https://todoist.com/API'

def open_apilink(add_link):
	json_items = urllib.urlopen(todoist_link + add_link)
	result_items = json.load(json_items)
	return result_items

def get_projects():
	all_projects = open_apilink('/getProjects?token=' + api_key)
	return all_projects

def get_id_projects():
	all_id = []
	for one_id in get_projects():
		all_id.append(one_id['id'])

	return all_id

def get_uncompleted_items(id_projects):
	all_items = []
	for one_id in id_projects:
		projects_items = open_apilink('/getUncompletedItems?token=' + api_key + '&project_id=' + str(one_id))
		for one_item in projects_items:
			all_items.append(one_item)

	return all_items

date_format = "%a %d %b %Y %H:%M:%S" 
need_tasks = []	
for one_item in get_uncompleted_items(get_id_projects()):
	if one_item['due_date']:
		item_time = datetime.strptime(one_item['due_date'], date_format)
		delta = item_time - datetime.now()
		if (delta.days <= 2):
			need_tasks.append(one_item)

print len(need_tasks)
for one_task in need_tasks:
	print one_task['date_string'], one_task['content']