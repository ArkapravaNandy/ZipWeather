from django.shortcuts import render

# This is my views.py file
def home(request):
    import json
    import requests

    api_request=requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=5&API_KEY=DF8CE76E-D834-4728-9948-CB7B2AE0CB8E")
    
    try:
        api=json.loads(api_request.content)
    except Exception as e:
        api="Error 404...not found!"

    return render(request, 'Index.html', {'api' : api})    
