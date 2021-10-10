from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class BasicTemplateView(TemplateView):
    template_name = 'analysisapp/base.html'

def let_write(request):
    if request.method == "POST":
        if request.POST.get("input_text1"):
            temp_text = " 흔히 직접인용부호를 사용한 인용문을 중심으로 기사를 작성하는 것을 일러 '따옴표 저널리즘'이라 부른다."
            temp_text2 = " 한국의 신문이 특정 정보원의 발언 내용을 독립적으로 검증하지 않고 무분별하게 인용 보도하는 행위를 비판하려는 목적에서 차용된 용어다."
            temp_text3 = " (이준웅, 양승목, 김규찬, 송현주, 「기사 제목에 포함된 직접 인용부호 사용의 문제점과 원인」, 2007)"
            return render(request, 'analysisapp/base.html', context={'text': temp_text,'text2':temp_text2,'text3':temp_text3})
        elif request.POST.get("input_text2"):
            temp_text = " 서구의 권위 있는 언론은 기사 속에서뿐만이 아니라 제목에서는 더더욱 따옴표를 통한 직접 인용을 꺼린다. (중략) "
            temp_text2 = " 언제부턴가 한국의 저널리즘 속엔 너무나 많은 발화자들이 등장한다. 기사를 쓰는 주체는 기자이지 취재 대상이 아니다. 게다가 발화자의 발언은 기자에 의한 사실 확인이 필요한 주장에 불과하다. "
            temp_text3 = " 혹여 ‘누군가가 그러한 주장을 했다는 사실’이 필요하다고 하더라도 그 발언에 따옴표를 붙여 보도해주기 위해서는 기자와 데스크에 의한 고민과 판단이 요구된다."
            temp_text4 = " (정준희, 『방송기자』, 2019.03, p.13-14.)"
            return render(request, 'analysisapp/base.html', context={'text': temp_text,'text2': temp_text2, 'text3': temp_text3,'text4': temp_text4})
        elif request.POST.get("input_text3"):
            temp_text = " [1] 첫 번 째는 '판단유보' 유형이다. 제목에 달린 따옴표는 독자로 하여금 기사에 의구심을 갖게 한다. 따옴표 안의 내용은 기자가 판단을 유보한 내용이라고 읽게 된다. 독자는 기자가 제목으로 전하기는 하지만, 따옴표 안의 내용이 의미하는 바를 철저히 확인하지 못했다고 이해한다는 뜻이다."
            temp_text2 =" [2] 두 번 째는 '책임회피'유형이다. 기자는 자신이 전하는 기사에 담긴 내용이 진실임을 취재를 통해 입증해야하는 기본적 책임이 있는 사람이다. 그러나 많은 한국 기자는 따옴표 뒤에 숨어 그러한 의무를 수행하지 않는다. 기자의 임무는 ‘누가 어떠한 말을 했는지’만 전달하는 선에서 그쳐도 된다는 직업관이 이러한 관행에 녹아있다는 뜻으로 볼 수도 있다. 따옴표로 전하는 말이 진실을 담고 있지 않았다면 거기에 대해서는 기자나 언론사가 책임지지 않겠다는 선언, 즉 따옴표의 지극히 부정적인 기능 역시 내포하고 있는 것이다."
            temp_text3 =" [3] 세 번 째는 '선정주의'유형이다. 제목에 따옴표를 달면 독자는 아무 것도 없는 제목에 비해 시각적 자극을 강하게 느끼게 된다. 블라우 교수는 이러한 장치를 통해 기자는 자신의 주관적 관점을 독자에게 강요할 수 있다고 주장한다."
            temp_text4 =" (이재경, 『신문과 방송』, 2019.06, p.102-103.)"
            return render(request, 'analysisapp/base.html', context={'text': temp_text,'text2': temp_text2, 'text3': temp_text3,'text4': temp_text4})

    else:
        return render(request, 'analysisapp/base.html', context={'text1': ""})