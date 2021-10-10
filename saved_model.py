import torch
from transformers import BertModel, BertTokenizer
import torch.nn.functional as F
from Builder import Build_X
from bbqqClassifer import bbqqClassifer




bertmodel = BertModel.from_pretrained("monologg/kobert")
tokenizer = BertTokenizer.from_pretrained("monologg/kobert")

def predict(DATA):

    device = torch.device('cpu')
    model = torch.load(r'C:\Users\JH\PycharmProjects\testtest\epoch50.pth', map_location=device)
    X = Build_X(DATA, tokenizer, device)
    y_hat = model.predict(X)
    y_hat = F.softmax(y_hat, dim=1)

    return y_hat.detach().numpy()
