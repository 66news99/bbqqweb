from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import TemplateView
import requests
import json
import pandas as pd
import os
import numpy as np
from selenium import webdriver
from bs4 import BeautifulSoup as soup
import time
import datetime

from saved_model import predict
from todaylist import today_list

cwd = os.getcwd()

def News_category(**temp):
    today = datetime.datetime.now()
    yesterday = today - datetime.timedelta(1)
    yesterday = yesterday.strftime("%Y%m%d")

    yesterday = yesterday[:4] + '-' + yesterday[4:6] + '-' + yesterday[6:]
    date1 = str(int(yesterday[:4] + yesterday[5:7] + yesterday[8:]) + 1)
    today = date1[:4] + '-' + date1[4:6] + '-' + date1[6:]

    category = ["정치", "경제", "사회", "국제", "문화", "스포츠", "IT_과학",""]
    per_res = {}

    my_key = "a19a4199-9fe3-4dff-90ed-6512bb359f2b"

    result_url = 'http://tools.kinds.or.kr:8888/search/news'
    for i in range(len(category)):
        data = {
            "access_key": f"{my_key}",
            "argument": {
                "query": "",
                "published_at": {
                    "from": yesterday,
                    "until": today
                },
                "provider": [""],
                "category": [category[i]],
                "provider_subject": [""],
                "subject_info": [""],
                "sort": {
                    "date": "desc"
                },
                "hilight": 200, "return_from": 0, "return_size": 20000,
                "fields": [
                    "hilight","category","category_incident","images","provider_subject","subject_info",
                    "provider_news_id","publisher_code"
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

    politics = per_res['정치']
    economy = per_res['경제']
    social = per_res['사회']
    world = per_res['국제']
    culture = per_res['문화']
    sports = per_res['스포츠']
    science = per_res['IT_과학']
    total = per_res['']
    return [politics,economy,social,world,culture,sports,science,total,yesterday]

def search_selenium(search_name):
    search_url = "https://www.google.com/search?q=" + str(search_name) + "&hl=ko&tbm=isch"
    options = webdriver.ChromeOptions()
    # 창 숨기는 옵션 추가
    options.add_argument("headless")
    browser = webdriver.Chrome("C:\\Users\\JH\\Downloads\\chromedriver_win32\\chromedriver.exe",options=options)
    # soup = BeautifulSoup(text, 'html.parser')
    browser.get(search_url)
    # img = soup.find("img")
    # img_src = img.get("src")

    browser.implicitly_wait(2)
    image = browser.find_elements_by_tag_name("img")[41]
    image.screenshot(cwd + '\\static\\img\\top.jpg')
    image_loc = (cwd + '\\static\\img\\top.jpg')
    browser.quit()
    return image_loc

def weekly_keyword(**temp):
    today = datetime.datetime.now()
    yesterday = today - datetime.timedelta(1)
    yesterday = yesterday.strftime("%Y%m%d")

    yesterday = yesterday[:4] + '-' + yesterday[4:6] + '-' + yesterday[6:]
    date1 = str(int(yesterday[:4] + yesterday[5:7] + yesterday[8:]) - 7)
    lastday = date1[:4] + '-' + date1[4:6] + '-' + date1[6:]

    date = yesterday[:4]+'년'+yesterday[5:7]+'월'+yesterday[8:]+'일'

    my_key = "a19a4199-9fe3-4dff-90ed-6512bb359f2b"

    result_url = 'http://tools.kinds.or.kr:8888/search/news'

    data = {
        "access_key": f"{my_key}",
        "argument": {
            "query": "",
            "published_at": {
                "from": lastday,
                "until": yesterday
            },
            "provider": [""],
            "category": [""],
            "category_incident": [""],
            "provider_subject": [""],
            "subject_info": [""],
            "sort": {"date": "desc"},
            "hilight": 200,
            "return_from": 0,
            "return_size": 20000,
            "fields": ["hilight", "category", "category_incident", "images", "provider_subject",
                       "subject_info", "provider_news_id", "publisher_code"]}
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

    res_fin = []
    for i in range(len(sen_res)):
        if sen_res[i].count('"') == 1:
            sen_fin = sen_res[i].replace('"', ' ')
            res_fin.append(sen_fin)
        else:
            begin = sen_res[i].index('"')
            if '"' in sen_res[i][begin + 1:]:
                end = sen_res[i][begin + 1:].index('"')
            else:
                end = begin

            sen = sen_res[i].replace(sen_res[i][begin:begin + end + 2], ' ')
            if '"' in sen:
                second = sen.index('"')
                if '"' in sen[second + 1:]:
                    second_end = sen[second + 1:].index('"')
                else:
                    second_end = second
                sen_fin = sen.replace(sen[second:second + second_end + 2], ' ')
                res_fin.append(sen_fin)
            else:
                res_fin.append(sen)

    words = []
    props = [',', '.', '"', '?', '…', '+', '[', ']', 'vs', '‘', '’', '  ', '   ', '    ', '     ']
    for sen in res_fin:
        for prop in props:
            sen = sen.replace(prop, " ")
        sen = sen.split(" ")
        for word in sen:
            words.append(word)

    word_cnt = []
    for word in words:
        cnt = words.count(word)
        word_cnt.append((cnt, word))

    se = set(word_cnt)
    fin = list(se)

    word_list = []
    num_list = []
    for i in range(len(fin)):
        word_list.append(fin[i][1])
        num_list.append(fin[i][0])

    for j in range(1, len(word_list)):
        for i in range(j + 1, len(word_list)):
            if word_list[j] in word_list[i]:
                num_list[j] += 1
    final = []
    for i in range(len(word_list)):
        if len(word_list[i]) > 1:
            final.append([num_list[i], word_list[i]])
    final.sort(reverse=True)
    top = final[0][1]
    im_loc = search_selenium(top)

    return [top,im_loc,date]
def pred():
    list_a = []
    list_b = []
    list_c = []
    sen_res = today_list()

    for sen in sen_res:
        if np.argmax(predict(sen)[0]) == 0:
            list_a.append(sen)
        elif np.argmax(predict(sen)[0]) == 1:
            list_b.append(sen)
        elif np.argmax(predict(sen)[0]) == 2:
            list_c.append(sen)

        if min(len(list_a) , len(list_b), len(list_c) ) ==3 :
            break
    return [list_a,list_b,list_c]

class BasicTemplateView(TemplateView):
    template_name = 'mainapp/base.html'



    def get(self, request, *args, **kwargs):

        kwargs['politics'] = News_category()[0]
        kwargs['economy'] = News_category()[1]
        kwargs['social'] = News_category()[2]
        kwargs['world'] = News_category()[3]
        kwargs['culture'] = News_category()[4]
        kwargs['sports'] = News_category()[5]
        kwargs['science'] = News_category()[6]
        kwargs['total'] = News_category()[7]
        kwargs['top'] = weekly_keyword()[0]
        kwargs['image_loc'] = weekly_keyword()[1]
        kwargs['yesterday'] = weekly_keyword()[2]
        kwargs['a0'] = pred()[0][0]
        kwargs['a1'] = pred()[0][1]
        kwargs['a2'] = pred()[0][2]
        kwargs['b0'] = pred()[1][0]
        kwargs['b1'] = pred()[1][1]
        kwargs['b2'] = pred()[1][2]
        kwargs['c0'] = pred()[2][0]
        kwargs['c1'] = pred()[2][1]
        kwargs['c2'] = pred()[2][2]
        return super().get(request, *args, **kwargs)

