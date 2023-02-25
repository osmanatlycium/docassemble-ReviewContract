def update_task(taskid, todo):
 import requests 

 if todo == 'complete':
  url = 'https://lrv.hrpilot.co.uk/api/v1/tasks/complete/' 
 elif todo == 'reject':
  url = 'https://lrv.hrpilot.co.uk/api/v1/tasks/reject/' 
 elif todo == 'sign':
  url = 'https://lrv.hrpilot.co.uk/api/v1/tasks/sign/' 
 else:
  url = 'https://lrv.hrpilot.co.uk/api/v1/tasks/' 

 data = {"Id": taskid}
 param = {'X-Authorization': '9FIittRmUQGJHLTZw0IQUdGB8bwePmhggV7y40UoJi1qRWbiYh9AaM6ABcKrBTzn'}
 response = requests.put(url, data, headers=param)

 return(url)


