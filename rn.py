import json

# with open('settings.json') as json_file:
# 	data = json.load(json_file)
# print(data)

req = urllib.request.Request(https://api.github.com/search/issues?q=repo:opensearch-project/documentation-website+is:pr+assignee:JeffH-AWS+is:open)
response = urllib.request.urlopen(req)
data = response.read()
values = json.loads(data)
print(response)