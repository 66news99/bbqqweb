import random

from django.shortcuts import render
import numpy as np
# Create your views here.
from django.views.generic import TemplateView
from Builder import Build_X
import torch
from transformers import BertModel, BertTokenizer
import torch.nn.functional as F
from bbqqClassifer import bbqqClassifer
from saved_model import predict
from todaylist import today_list

bertmodel = BertModel.from_pretrained("monologg/kobert")
tokenizer = BertTokenizer.from_pretrained("monologg/kobert")

def pred():
    sen_res = today_list()
    pred_list = []
    label = []
    for sen in sen_res[:7]:
        pred_list.append(predict(sen))
        if np.argmax(predict(sen)[0]) == 0:
            label.append('<판단유보 유형>')
        elif np.argmax(predict(sen)[0]) == 1:
            label.append('<책임회피 유형>')
        elif np.argmax(predict(sen)[0]) == 2:
            label.append('<선정주의 유형>')
    return [sen_res,pred_list,label]

class BasicTemplateView(TemplateView):
    template_name = 'traceapp/base.html'
    def get(self, request, *args, **kwargs):

        kwargs['sen0'] = pred()[0][0]
        kwargs['sen1'] = pred()[0][1]
        kwargs['sen2'] = pred()[0][2]
        kwargs['sen3'] = pred()[0][3]
        kwargs['sen4'] = pred()[0][4]
        kwargs['sen5'] = pred()[0][5]
        kwargs['sen6'] = pred()[0][6]
        kwargs['label0'] = pred()[2][0]
        kwargs['label1'] = pred()[2][1]
        kwargs['label2'] = pred()[2][2]
        kwargs['label3'] = pred()[2][3]
        kwargs['label4'] = pred()[2][4]
        kwargs['label5'] = pred()[2][5]
        kwargs['label6'] = pred()[2][6]

        kwargs['pred000'] =pred()[1][0][0][0]*100
        kwargs['pred001'] =pred()[1][0][0][1]*100
        kwargs['pred002'] =pred()[1][0][0][2]*100
        kwargs['pred100'] =pred()[1][1][0][0]*100
        kwargs['pred101'] =pred()[1][1][0][1]*100
        kwargs['pred102'] =pred()[1][1][0][2]*100
        kwargs['pred200'] =pred()[1][2][0][0]*100
        kwargs['pred201'] =pred()[1][2][0][1]*100
        kwargs['pred202'] =pred()[1][2][0][2]*100
        kwargs['pred300'] =pred()[1][3][0][0]*100
        kwargs['pred301'] =pred()[1][3][0][1]*100
        kwargs['pred302'] =pred()[1][3][0][2]*100
        kwargs['pred400'] =pred()[1][4][0][0]*100
        kwargs['pred401'] =pred()[1][4][0][1]*100
        kwargs['pred402'] =pred()[1][4][0][2]*100
        kwargs['pred500'] =pred()[1][5][0][0]*100
        kwargs['pred501'] =pred()[1][5][0][1]*100
        kwargs['pred502'] =pred()[1][5][0][2]*100
        kwargs['pred600'] =pred()[1][6][0][0]*100
        kwargs['pred601'] =pred()[1][6][0][1]*100
        kwargs['pred602'] =pred()[1][6][0][2]*100

        return super().get(request, *args, **kwargs)


# print(pred()[0][0][0])