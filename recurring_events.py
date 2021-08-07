from datetime import datetime
from dateutil.relativedelta import *
from dateutil.parser import *
from secrets import NOTION_API_KEY
import requests

response = requests.get('https://api.notion.com/v1/databases', headers={'Authorization': 'Bearer {}'.format(NOTION_API_KEY), 'Notion-Version': '2021-07-27'})
databases = []
for i, database in enumerate(response.json()['results']):
    databases.append({
        'id': database['id'],
        'properties': database['properties']
    })
    print('{}: '.format(i), database['id'], database['title'][0]['text']['content'])

database = databases[int(input('Database index: '))]
properties = {}
date = ''
for key, property in database['properties'].items():
    if property['type'] == 'title':
        properties[key] = {
            'title': [{
                'text': {
                    'content': input('Enter title of entries: ')
                }
            }]
        }
    elif property['type'] == 'rich_text':
        properties[key] = {
            'rich_text': [{
                'text': {
                    'content': input('Enter {} of entries: '.format(key))
                }
            }]
        }
    elif property['type'] == 'select':
        options = []
        for i, option in enumerate(property['select']['options']):
            options.append(option['name'])
            print('{}: '.format(i), option['name'])
        properties[key] = {
            'select': {
                'name': options[int(input('Index of option: '))]
            }
        }
    elif property['type'] == 'number':
        properties[key] = {
            'number': float(input('Enter your {}: '.format(key)))
        }
    elif property['type'] == 'multi_select':
        options = []
        for i, option in enumerate(property['multi_select']['options']):
            options.append(option['name'])
            print('{}: '.format(i), option['name'])
        selection = [{ 'name': option[int(i)] } for i in input('Enter indices of options separated by commas: ').split(',')]
        properties[key] = {
            'multi_select': selection
        }
    elif property['type'] == 'date':
        date = key
        properties[key] = {
            'date': {
                'start': isoparse(input('Starting date (ISO 8601): ')).isoformat(),
                'end': input('Ending date (ISO 8601, optional): '),
            }
        }
        if properties[key]['date']['end'] == '':
            properties[key]['date']['end'] = None
        else:
            properties[key]['date']['end'] = isoparse(properties[key]['date']['end'])
    elif property['type'] == 'checkbox':
        properties[key] = {
            'checkbox': input('Checkbox value (true/false): ') == 'true'
        } 
    elif property['type'] == 'url':
        properties[key] = {
            'url': input('Url value: ')
        } 
    elif property['type'] == 'email':
        properties[key] = {
            'checkbox': input('Email value: ')
        } 
    elif property['type'] == 'phone_number':
        properties[key] = {
            'checkbox': input('Phone number: ')
        } 

years = int(input('Year gap: '))
months = int(input('Month gap: '))
weeks = int(input('Week gap: '))
days = int(input('Day gap: '))
hours = int(input('Hour gap: '))
minutes = int(input('Minute gap: '))
iterations = int(input('Number of iterations: '))
for i in range(iterations):
    pages = requests.post('https://api.notion.com/v1/pages', 
    headers={
        'Authorization': 'Bearer {}'.format(NOTION_API_KEY),
        'Notion-Version': '2021-07-27',
        'Content-Type': 'application/json'
    },
    json={
        'parent': { 'database_id': database['id'] },
        'properties': properties
    })
    print(pages.status_code)
    new_start = isoparse(properties[date]['date']['start'])+relativedelta(years=+years, months=+months, weeks=+weeks, days=+days, hours=+hours, minutes=+minutes)
    properties[date]['date']['start'] = new_start.isoformat()
    if properties[date]['date']['end']:
        new_end = isoparse(properties[date]['date']['end'])+relativedelta(years=+years, months=+months, weeks=+weeks, days=+days, hours=+hours, minutes=+minutes)
        properties[date]['date']['start'] = new_end.isoformat()