from django.shortcuts import render
from django.http import HttpResponse
from AracProje.mymodels.Arac import Arac

def index(request):
    if request.method == "POST":
        arac = Arac(request.POST)
        if arac.is_valid():            
            return render(request,'sonuc.html',{'depo' : arac.sur(),'menzil' : arac.menzil(), 'yol' : arac.gidilenYol()})
    
    else:
        arac = Arac()
        return render(request,'index.html',{'arac' : arac})
