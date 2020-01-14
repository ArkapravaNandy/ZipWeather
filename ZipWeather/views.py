from django.shortcuts import render

# This is my views.py file
def home(request):
    import json
    import requests
    if(request.method=='POST'):
        zip=request.POST['zip']   
        api_request=requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode="+zip+"&distance=25&API_KEY=DF8CE76E-D834-4728-9948-CB7B2AE0CB8E")
        try:
            api=json.loads(api_request.content)
            
        except Exception as e:
            api="Error 404...not found!"
            
        if api[0]["Category"]["Name"]=="Good" :
            description="AQI: Good (0 - 50) Air quality is considered satisfactory, and air pollution poses little or no risk"
            jumbo_color="good"
        elif api[0]['Category']['Name']=="Moderate" :
            description="AQI: Moderate (51 - 100) Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution."
            jumbo_color="moderate"
        elif api[0]['Category']['Name']=="Unhealthy for Sensitive Groups" :
            description="AQI: Unhealthy for Sensitive Groups (101 - 150) Although general public is not likely to be affected at this AQI range, people with lung disease, older adults and children are at a greater risk from exposure to ozone, whereas persons with heart and lung disease, older adults and children are at greater risk from the presence of particles in the air."
            jumbo_color="usg"
        elif api[0]['Category']['Name']=="Unhealthy" :
            description="AQI: Unhealthy (151 - 200)Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects."
            jumbo_color="unhealty"
        elif api[0]['Category']['Name']=="Very Unhelthy" :
            description="AQI: Very Unhealthy (201 - 300) Health alert: everyone may experience more serious health effects."
            jumbo_color="veryunhealthy"
        elif api[0]['Category']['Name']=="Hazardous" :
            description="AQI: Hazardous (301 - 500) Health warnings of emergency conditions. The entire population is more likely to be affected."
            jumbo_color="hazardous"
            
        
        return render(request, 'Index.html', {'api' : api, 'description': description,'jumbo_color': jumbo_color})    
    else:
            api_request=requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=5&API_KEY=DF8CE76E-D834-4728-9948-CB7B2AE0CB8E")
            try:
                api=json.loads(api_request.content)
                
            except Exception as e:
                api="Error 404...not found!"
                
            if api[0]['Category']['Name']=="Good" :
                description="AQI: Good (0 - 50) Air quality is considered satisfactory, and air pollution poses little or no risk"
                jumbo_color="good"
            elif api[0]['Category']['Name']=="Moderate" :
                description="AQI: Moderate (51 - 100) Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution."
                jumbo_color="moderate"
            elif api[0]['Category']['Name']=="Unhealthy for Sensitive Groups" :
                description="AQI: Unhealthy for Sensitive Groups (101 - 150) Although general public is not likely to be affected at this AQI range, people with lung disease, older adults and children are at a greater risk from exposure to ozone, whereas persons with heart and lung disease, older adults and children are at greater risk from the presence of particles in the air."
                jumbo_color="usg"
            elif api[0]['Category']['Name']=="Unhealthy" :
                description="AQI: Unhealthy (151 - 200)Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects."
                jumbo_color="unhealty"
            elif api[0]['Category']['Name']=="Very Unhelthy" :
                description="AQI: Very Unhealthy (201 - 300) Health alert: everyone may experience more serious health effects."
                jumbo_color="veryunhealthy"
            elif api[0]['Category']['Name']=="Hazardous" :
                description="AQI: Hazardous (301 - 500) Health warnings of emergency conditions. The entire population is more likely to be affected."
                jumbo_color="hazardous"
                
            
            return render(request, 'Index.html', {'api' : api, 'description': description})    
