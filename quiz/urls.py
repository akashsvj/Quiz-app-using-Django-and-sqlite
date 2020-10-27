from django.urls import path
#from AJAX import views as a
from quiz import views as a
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', a.welcome,name='welcome'),
                  path('quiz/', a.index),
                  path('save_ans/', a.save_ans, name="saveans"),
                  path('result/', a.result, name="result"),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
