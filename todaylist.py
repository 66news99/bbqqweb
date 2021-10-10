import datetime

import requests
import json


def today_list():
    category = [""]
    today = datetime.datetime.now()
    yesterday = today - datetime.timedelta(1)
    yesterday = yesterday.strftime("%Y%m%d")

    yesterday = yesterday[:4] + '-' + yesterday[4:6] + '-' + yesterday[6:]
    date1 = str(int(yesterday[:4] + yesterday[5:7] + yesterday[8:]) + 1)
    today = date1[:4] + '-' + date1[4:6] + '-' + date1[6:]
    my_key = "a19a4199-9fe3-4dff-90ed-6512bb359f2b"
    result_url = 'http://tools.kinds.or.kr:8888/search/news'
    for i in range(len(category)):
        data = {
            "access_key": f"{my_key}",
            "argument": {
                "query":"",
                "published_at": {
                    "from": yesterday,
                    "until": today
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

        for sen in res_title :
            if '“' in sen :
                sen = sen.replace('“','"')
                if '”' in sen :
                    sen = sen.replace('”','"')
                sen_res.append(sen)
            elif '”' in sen :
                sen = sen.replace('”','"')
                sen_res.append(sen)
            elif '"' in sen :
                sen_res.append(sen)

    return sen_res

