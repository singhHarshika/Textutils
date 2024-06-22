

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):

    # for get the text
    djtext=request.POST.get('text','default')

    #check checkbox value on or off
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get("newlineremover",'off')
    extraspaceremover = request.POST.get("extraspaceremover", 'off')
    charcount=request.POST.get('charcount','off')

    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed= " "
        for char in djtext:
           if char not in punctuations:
              analyzed= analyzed + char
        params={'purpose':'Remove Punctuation','analyzed_text':analyzed}
        djtext=analyzed

    if(fullcaps=='on'):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'Changed To Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed

    if(newlineremover=="on"):
        analyzed=""
        for char in djtext:
          if char != "\n" and char !="\r":
            analyzed=analyzed+char
        params={'purpose':'Removed New lines','analyzed_text':analyzed}
        djtext = analyzed

    if(extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analyzed = analyzed + char
        params = {'purpose': 'Removed Extra Space', 'analyzed_text': analyzed}
        djtext = analyzed

    if(charcount=='on'):
        analyzed=" "
        djtext2 = djtext.replace(' ', '')
        char_count=len(djtext2)
        analyzed= "Number of characters in given text :"+ str(char_count)
        params={'purpose':'Count Characters','analyzed_text':analyzed}

    if(removepunc!="on" and fullcaps!="on" and newlineremover!="on" and extraspaceremover!="on" and charcount!="on") :
         return HttpResponse('please select any operation and try again!!!')

    return render(request, 'analyze.html', params)

