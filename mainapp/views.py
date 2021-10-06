from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
import requests
import json
import pandas as pd
import re
from openpyxl import Workbook
import numpy as np
def News_data():
    #자신의 api 키를 입력해서 사용해주세요!
    my_key = "a19a4199-9fe3-4dff-90ed-6512bb359f2b"

    # result_url에 따라 인용문이나 그날의 뉴스 순위등을 설정할수있으니 사용자 지침서를 꼭 보셔야해요!
    result_url = 'http://tools.kinds.or.kr:8888/search/news'
    data = {
        "access_key": f"{my_key}",
        "argument": {
            "query":"",
            "published_at": {
                "from": "2021-10-05", #이전에는 관련 기사 없음 확인
                "until": "2021-10-06"
            },
            "provider": [
                ""
            ],
            "category": [
                ""
            ],
            "category_incident": [
                 ""
            ],
            "byline": "",
            "provider_subject": [
                ""
            ],
            "subject_info": [
                ""
            ],
            "subject_info1": [
                ""
            ],
            "subject_info2": [
                ""
            ],
            "subject_info3": [
                ""
            ],
            "subject_info4": [
                ""
            ],
            "sort": {
                "date": "desc"
            },
            "hilight": 200,
            "return_from": 0,
            "return_size": 20000, #총 힛이 2133입니다
            "fields": [
                "hilight",
                "byline",
                "category",
                "category_incident",
                "images",
                "provider_subject",
                "subject_info",
                "provider_news_id",
                "publisher_code"
            ]
        }
    }

    dated = data['argument']['published_at']['from']

    response = requests.post(result_url, data=json.dumps(data))
    res_json = response.json()
    res_doc = res_json['return_object']['documents']
    res_title = [i['title'] for i in res_doc]
    my_ex = '"'
    sen_res = []
    for sen in res_title:
        if re.search(my_ex, sen):
            sen_res.append(sen)
    return((len(sen_res)/len(res_title))*100, dated)

def News_category():
    category = ["정치", "경제", "사회", "국제", "문화", "스포츠", "IT_과학"]
    per_res = {}
    date = str(20211005)
    today = date[:4] + '-' + date[4:6] + '-' + date[6:]
    date1 = str(int(date) + 1)
    tomorrow = date1[:4] + '-' + date1[4:6] + '-' + date1[6:]

    my_key = "a19a4199-9fe3-4dff-90ed-6512bb359f2b"

    result_url = 'http://tools.kinds.or.kr:8888/search/news'
    for i in range(len(category)):
        data = {
            "access_key": f"{my_key}",
            "argument": {
                "query": "",
                "published_at": {
                    "from": today,
                    "until": tomorrow
                },
                "provider": [
                    ""
                ],
                "category": [
                    category[i]
                ],
                "provider_subject": [
                    ""
                ],
                "subject_info": [
                    ""
                ],
                "sort": {
                    "date": "desc"
                },
                "hilight": 200,
                "return_from": 0,
                "return_size": 20000,
                "fields": [
                    "hilight",
                    "byline",
                    "category",
                    "category_incident",
                    "images",
                    "provider_subject",
                    "subject_info",
                    "provider_news_id",
                    "publisher_code"
                ]
            }
        }

        response = requests.post(result_url, data=json.dumps(data))
        res_json = response.json()
        res_doc = res_json['return_object']['documents']
        res_title = [x['title'] for x in res_doc]

        sen_res = []

        for sen in res_title:
            if '“' in sen:
                sen = sen.replace('“', '"')
                if '”' in sen:
                    sen = sen.replace('”', '"')
                sen_res.append(sen)
            elif '”' in sen:
                sen = sen.replace('”', '"')
                sen_res.append(sen)
            elif '"' in sen:
                sen_res.append(sen)
        per = len(sen_res) / len(res_title)

        per_res[category[i]]=str(np.round((per*100),1))+'%'
        print("{} {} 뉴스에 {}%의 비율로 따옴표가 쓰였습니다.".format(today, category[i], np.round(per * 100, 2)))

    politics = per_res['정치']
    economy = per_res['경제']
    social = per_res['사회']
    world = per_res['국제']
    culture = per_res['문화']
    sports = per_res['스포츠']
    science = per_res['IT_과학']
    return [politics,economy,social,world,culture,sports,science]

class BasicTemplateView(TemplateView):
    template_name = 'mainapp/base.html'

    def get(self, request, *args, **kwargs):
        kwargs['test'] = News_data()[0]
        kwargs['date'] = News_data()[1]
        kwargs['politics'] = News_category()[0]
        kwargs['economy'] = News_category()[1]
        kwargs['social'] = News_category()[2]
        kwargs['world'] = News_category()[3]
        kwargs['culture'] = News_category()[4]
        kwargs['sports'] = News_category()[5]
        kwargs['science'] = News_category()[6]

        return super().get(request, *args, **kwargs)

