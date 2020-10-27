from django.urls import include

from django.contrib import admin
from django.urls import path
#from AJAX import views as a
import quiz
from quiz import views as a
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('',include('quiz.urls')),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
