# sandbox-django-urltag-regexnamespace

```{% url %}```テンプレートタグを使ってURLを描画するテストリポジトリ。 
urlはURLconf内でview関数とヒモ付がされている。例えばチュートリアルではこうなっている。 https://docs.djangoproject.com/ja/2.1/intro/tutorial03/#namespacing-url-names
```py
from django.urls
import path
from.import
views app_name = 'polls'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:question_id>/', views.detail, name = 'detail'),
    path('<int:question_id>/results/', views.results, name = 'results'),
    path('<int:question_id>/vote/', views.vote, name = 'vote'),
    ]

 ``` 

正規表現や変数を使ったurlpatternに対して、URLをテンプレート上で動的に生成できるかどうかを確認する。