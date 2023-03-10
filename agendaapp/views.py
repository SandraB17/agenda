from django.shortcuts import render

# Create your views here.
def base(resquest):
    return render(resquest,'agenda/base.html')
