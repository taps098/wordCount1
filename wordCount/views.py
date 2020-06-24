from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')

def count(request):
    return render(request, 'wordCounting.html')

def result(request):
    User_Input = request.GET['UserInput']
    words = User_Input.split()
    wordDictionary = {}
    for wrd in words:
        if wrd in wordDictionary:
            wordDictionary[wrd] += 1
        else:
            wordDictionary[wrd] = 1
    sortedList = sorted(wordDictionary.items(), key=operator.itemgetter(1), reverse = True)

    return render(request, 'result.html', {'input': User_Input, 'wordCount' : len(words), 'wordCountList': sortedList})

def about(request):
    return render(request, 'about.html')
