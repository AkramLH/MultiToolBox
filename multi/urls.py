from django.contrib import admin
from django.urls import path, include

from .views import *
from guess_number.views import *
from temp_convert.views import *
from weight_count.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('guess/', include('guess_number.urls')),
    path('temp/', include('temp_convert.urls')),
    path('weight/', include('weight_count.urls')),
]
