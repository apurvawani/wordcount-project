from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
 	return render(request , 'home.html')

def count(request):
	fulltext = request.GET['fulltext']
	wordList = fulltext.split()
	wordCount = {}
	for word in wordList:
		if word in wordCount:
			wordCount[word] += 1
		else:
			wordCount[word] = 1

	sortedWords = sorted(wordCount.items() , key = operator.itemgetter(1) , reverse = True)

	return render(request , 'count.html' , {'fulltext' : fulltext , 'count' : len(wordList) , 'sortedWords' : sortedWords}) 

def about(request):
	return render(request , 'about.html')	