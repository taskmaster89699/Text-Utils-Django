#file created manually
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # params= {"name": "Kittu", "age":"1.5"}
    return render(request, 'index.html')
    # return HttpResponse('''<a href="https://www.google.com">Google</a>''')

def about(request):
    return HttpResponse("this is about")

def analyze(request):
    djtext= request.POST.get('text', 'default')
    removepunc= request.POST.get('removepunc', 'off')
    fullcaps= request.POST.get('fullcaps', 'off')
    newlineremover= request.POST.get('newlineremover', 'off')
    spaceremover= request.POST.get('spaceremover', 'off')
    charactercounter= request.POST.get('charactercounter', 'off')
    # print(removepunc)
    # print(djtext)
    if removepunc == 'on':
        analyzed= ""
        punctuations='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params= {'purpose': 'Remove Punctuations', 'analyzed_text': analyzed}
        # return HttpResponse("Removing Punctuations...")
        djtext= analyzed
        # return render(request, 'analyze.html', params)
    if fullcaps == 'on':
        analyzed= djtext.upper()
        params= {'purpose': 'Changed to Upper Case', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)
    if newlineremover=='on':
        analyzed= ""
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed= analyzed + char
        params= {'purpose': 'Removed New Lines', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)
    if spaceremover == 'on':
        analyzed= ""
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1] == " ":
                pass
            else:
                analyzed= analyzed + char
        params= {'purpose': 'Remove Extra Spaces', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)
    if charactercounter == 'on':
        analyzed= len(djtext)
        params= {'purpose': 'Count Characters', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)
    
    if (removepunc!='on' and newlineremover!='on' and spaceremover!= 'on' and fullcaps!= 'on' and charactercounter!= 'on'):
        return HttpResponse("Click on the required checkbox!")
    return render(request, 'analyze.html', params) 