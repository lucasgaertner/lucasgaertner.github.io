from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext

from django.http import HttpRequest


# Create your views here.

#import necessary libs


#get url
from django.urls import resolve
import pandas as pd
import os




def timeline(request):
    
    return render(request, 'polls/timeline.html')


def home(request):
    
    return render(request, 'polls/home.html')


def location(request):
    # Get Fulltext

    collected_years = {}
    for doc in os.listdir():
        if doc.startswith('dok_types_'):
            print(doc)
            year = doc[-8:-4]
            
            df = pd.read_csv('dok_types_'+ year + '.csv', encoding="latin-1", delimiter=";", error_bad_lines=False)
            df.columns = ['doku_type', 'CC', 'counter']
            cleaned = df.dropna()
            cleaned['CC'] = cleaned['CC'].apply(int)

            cleaned_sorted = cleaned.groupby(['CC', 'doku_type', 'counter'])
            cleaned_sorted = cleaned_sorted.groups
            CC_dict = {}
            for clean in cleaned_sorted:
                if clean[0] in CC_dict:
                    CC_dict[clean[0]].append([clean[1], clean[2]])
                else:
                    tmp_list = []
                    tmp_list.append([clean[1], clean[2]])
                    CC_dict[clean[0]] = tmp_list
                    
            collected_years[year] = CC_dict

    current_url = HttpRequest.get_full_path(request)

    if current_url == "/Germany":
        # print(dic[3])
        master_dic = {"CC": collected_years['2015'][3]}
    elif current_url == "/Spain":
        master_dic = {"CC": dic[60]}
    elif current_url == "/United States":
        master_dic = {"CC": dic[77]}
    elif current_url == "/Mexico":
        master_dic = {"CC": dic[78]}
    elif current_url == "/Japan":
        master_dic = {"CC": dic[90]}
    elif current_url == "/Singapore":
        master_dic = {"CC": dic[92]}
    elif current_url == "/Thailand":
        master_dic = {"CC": dic[91]}
    else:
        master_dic = {"CC": dic}

    return render(request, 'polls/location.html' , master_dic)