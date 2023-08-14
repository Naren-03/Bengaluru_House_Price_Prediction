from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.contrib import messages
from banglore_house_prediction import util
# Create your views here.

total_sqft = "0.0"
price = "0.0"
location = "Loction"
bhk = "0"
bath = "0"

def return_price(request):
    global price
    global total_sqft
    global location
    global bhk
    global bath
    util.extract_data()

    if request.method == 'POST':
        total_sqft = float(request.POST.get('Squareft'))
        location = request.POST.get('loc')
        bhk = int(request.POST.get('uiBHK'))
        bath = int(request.POST.get('uiBathrooms'))
        price = util.get_price(location,total_sqft,bhk,bath)
        print(total_sqft,location,bhk,bath,price)
    params={'Data':util.getloc(),'loc':location,'bhk':bhk,'bath':bath,'Price':price,'area_sqft':total_sqft}
    return render(request,'index.html',params)