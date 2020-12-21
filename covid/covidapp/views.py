from django.shortcuts import render
import requests,json

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "4f83bb086emshbdea6a3d4b268eap1b604ajsn0f063ee697ae",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers).json()

# Create your views here.
def Dharma(request):
    a = int(response['results'])
    l=[]
    for i in range(a):
        l.append(response['response'][i]['country'])
    if request.method=='POST':
        b = request.POST['country']
        for i in range(0,a):
            if b == response['response'][i]['country']:
                new = response['response'][i]['cases']['new']
                active = response['response'][i]['cases']['active']
                critical = response['response'][i]['cases']['critical']
                recovered = response['response'][i]['cases']['recovered']
                total = response['response'][i]['cases']['total']
                deaths = int(total) - int(active) - int(recovered)
        context = {'list1':l,'country':b,'new':new,'active':active,'critical':critical,'recovered':recovered,'total':total,'deaths':deaths}
        return render(request,'helloworld.html',context)
        
    context = {'list1':l}
    return render(request,'helloworld.html',context)
    
   