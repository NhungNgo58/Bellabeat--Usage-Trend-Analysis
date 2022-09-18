# Display the output
print('new Python file')
url = 'http://api.spacexdata.com/v4/launches/past'
response = request.get(url)
response.json()
