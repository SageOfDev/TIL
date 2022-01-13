from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render  # render는 파이썬 데이터를 템플릿에 적용하여 HTML로 반환하는 함수
from ..models import Question


def index(request):
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지, '1' 은 디폴트 값을 준 것

    # 조회
    question_list = Question.objects.order_by('-create_date')

    # 페이징처리
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj}
    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)
