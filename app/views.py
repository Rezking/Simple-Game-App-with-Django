from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests

# Create your views here.
def index(request):
    #The list for the code
    code_params=[(1,'a'),(2,'b'),(3,'c'),(4,'d'),(5,'e'),(6,'f'),(7,'g'),(8,'h'),(9,'i')]
    #Defining the first request
    if request.method == 'GET':
        mydict = dict()
        mydict["code_params"]=code_params
        return render(request, 'index.html', context = mydict)
    else:
        mydict = dict()
        code = request.POST['mycode']
        for (x,y) in code_params: 
            dict2 = {1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i'}
            code_str = str(code)
            word = ''
            for number in code_str:
                if number == ' ':
                    space = str(' ')
                    word += ' '
                else:
                    word += dict2[int(number)]
        #Making the api request in json format
        definition_reqr = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/"+word).json()
        #extracting the data from json result
        if type(definition_reqr) is dict:
             definition = "There is no such word"
        elif type(definition_reqr) is list:
             definition=definition_reqr[0]['meanings'][0]["definitions"][0]['definition']
        mydict = {"word":word, "code_params":code_params,"definition":definition}
        
        return render(request, 'index.html', context=mydict)
