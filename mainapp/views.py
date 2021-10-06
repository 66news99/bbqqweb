from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
import requests
import json
import pandas as pd
import re
from openpyxl import Workbook

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
                "from": "2021-10-04", #이전에는 관련 기사 없음 확인
                "until": "2021-10-05"
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


class BasicTemplateView(TemplateView):
    template_name = 'mainapp/base.html'

    def get(self, request, *args, **kwargs):
        kwargs['test'] = News_data()[0]
        kwargs['date'] = News_data()[1]
        return super().get(request, *args, **kwargs)
