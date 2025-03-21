from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'index.html',  context)

def create(request):
    # new/ 빈 종이를 보여주기
    # create/ 사용자가 입력한 데이터를 저장
    # =========================
    # GET create/ 빈 종이를 보여주기
    # POST create/ 사용자가 입력한 데이터를 저장

    # 모든 경우의 수
    # GET: form을 만들어서 html 문서를 사용자에게 리턴
    # POST: invaild 검증 실패
    # POST: valid 겅증 성공
    
    # POST 요청
    if request.method == 'POST':
        # POST 사용자가 입력한 데이터를 담은 폼을 만든다.
        form = ArticleForm(request.POST)
        # POST 검증 성공.
        if form.is_valid():
            # POST 폼을 저장.
            form.save()
            # POST index로 리다이렉트.
            return redirect('articles:index')
        # POST 검증 실패.
        # else:
        #     context = {
        #         'form': form,
        #     }
        #     return render(request, 'create.html', context)
        # 밑에 있는 else 문과 같기 때문에 지운다.
    
    # GET 요청
    else:
        # GET 비어있는 폼을 만든다.
        form = ArticleForm()
    # GET context에 비어있는 폼을 만든다.
    # POST 검증 실패한다면 context에 입력한 데이터를 담은 폼을 만든다.
    context = {
        'form': form,
    }
    return render(request, 'create.html', context)