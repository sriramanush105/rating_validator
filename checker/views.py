from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import re
#we define a function for checking whether a rating is given valid or not relating to positivity of review


def rating_check(sentence,rating):
    # Creating a SentimentIntensityAnalyzer object That can identify the sentiment of a
    sid_obj = SentimentIntensityAnalyzer()
    s= sid_obj.polarity_scores(sentence)
    #s is a dict containg pos ,neg, compund scores of sentence
    #s[compund] refers to overall sentiment of sentence which we use
    #when sentiment>0.05 its positive if <-0.05 its negative and between(-0.05,0.05) neutral
    # we compare it with our ratings and return true if ratings are valid else flase
    if s['compound'] >= 0.05 :
      if rating >=3:
        return True

    elif s['compound'] <0.05:
      if rating <3:
        return True

    return False
# Create your views here.
def index(request):
    s=''
    if request.method=='POST':
        f=request.FILES['myfile']
        if not f.name.endswith('.csv'):
            s='please upload csv file only'
            return render(request,'checker/index.html',{'s':s})

        file_data = f.read().decode("utf-8")
        lines=file_data.split("\n")
        reviews=[]
        for line in lines[1:2000]:
            r=re.split(',\d,\d,',line)
            review=r[0].split(',',2)
            l=line[::-1].split(",",7)
            print(l)
            try:
                if not rating_check(review[2],int(l[6])):
                    reviews.append({'rating':review[2],'review': l[6]})
            except:
                continue
        return render(request,'checker\invalid_reviews.html',{'reviews':reviews})


    return render(request,'checker/index.html',{'s':s})
