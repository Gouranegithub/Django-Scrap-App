from django.shortcuts import render , redirect
from django.http import HttpResponse
from .forms import DateForm
from django.contrib import messages
from .yallakoora import main

# Create your views here.

def  scrap_form(request):
    if request.method == 'POST':
        
        form = DateForm(request.POST)
        if form.is_valid():
            form.save()
            day = form.cleaned_data.get('day')
            month = form.cleaned_data.get('month')
            year = form.cleaned_data.get('year')
            try :
                #if( month in [2,4,6,9,11] and day == 31 ) or (month ==2 and day == 30) :
                datee= str(f'{month}/{day}/{year}')
                request.session['matches']=main(datee)
                
                messages.success(request,f'Matches for {day}/{month}/{year}')
                return redirect('result')
            except:
                messages.warning(request,f'there is no {day} in this month, pleas try a valid date')
                return redirect('form')
    else:
        form= DateForm()
    context ={'form':form}
    return render(request, 'scraper/the_form.html', context)
    
    
    
    
def result(request):
    matches =request.session.get('matches')
    context ={'matches' :matches}
    return render(request, 'scraper/result.html', context)