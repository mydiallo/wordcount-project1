from django.http import HttpResponse
# le render est utilisé lorsqu'on veut afficher quelque chose dans la page d'acceuil avec un fichier html
from django.shortcuts import render
import operator

def homepage(request):
    return render (request, 'home.html')

def cours(request):
    return render (request, 'cours.html')

# pour permettre à django d'utiliser une autre page on crée dans le fichier home.html une fontion forme et une fonction input ensuite on crée un autre fichier htlm('count.html')

def count(request):
    fulltext = request.GET['fulltext']
    worldlist = fulltext.split()
    
    worddictionnary = {}
    for word in worldlist:
        if word in worddictionnary:
            # Increase 
            worddictionnary[word] += 1
        else:
            #add to the dictionnary
             worddictionnary[word] = 1
# le fait de mettre un dictionnaire dans le return permet d'afficher ce qu'il renferme dans la page count.html
    
    sortedword = sorted(worddictionnary.items(), key=operator.itemgetter(1), reverse=True)
    return render (request, 'count.html', { 'fulltext':fulltext, 'count':len(worldlist), 'sortedword':sortedword})