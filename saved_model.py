import torch
from transformers import BertModel, BertTokenizer
import torch.nn.functional as F
from Builder import Build_X
from bbqqClassifer import bbqqClassifer

# USE_CUDA = torch.cuda.is_available()
# print(USE_CUDA)

#device = torch.device('cuda:0' if USE_CUDA else 'cpu')
# device = torch.device('cpu')
# print('학습을 진행하는 기기:',device)
# model = torch.load(r'C:\Users\jeonguihyeong\PycharmProjects\bbqq\bbqq\epoch50.pth', map_location=device)

# print(model.parameters())


bertmodel = BertModel.from_pretrained("monologg/kobert")
tokenizer = BertTokenizer.from_pretrained("monologg/kobert")

# DATA =["靑 \"日총리 취임후 정상 통화 검토\"…정상회담 재추진 계기 주목"]
#
# print(DATA)
def predict(DATA):

    device = torch.device('cpu')
    model = torch.load(r'C:\Users\JH\PycharmProjects\bbqqweb\epoch50.pth', map_location=device)
    X = Build_X(DATA, tokenizer, device)
    y_hat = model.predict(X)
    y_hat = F.softmax(y_hat, dim=1)

    return y_hat.detach().numpy()
    #
    # test_eval = []
    # for i in y_hat:
    #
    #     logits = i
    #     logits = np.round(logits.detach().cpu().numpy(), 2)
    #
    #     print(logits)
    #     if np.argmax(logits) == 0:
    #         test_eval.append("판단유보")
    #     elif np.argmax(logits) == 1:
    #         test_eval.append("책임회피")
    #     elif np.argmax(logits) == 2:
    #         test_eval.append("선정주의")
    # print(">> 이타이틀은 판단유보 {:.2f}, 책임회피 {:.2f}, 선정주의 {:.2f} 으로 측정되어 {}유형의 따옴표입니다".format(logits[0], logits[1], logits[2], test_eval[0]))
