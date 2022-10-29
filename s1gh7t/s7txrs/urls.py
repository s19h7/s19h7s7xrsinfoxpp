from django.urls import include, path, re_path
from django.views.decorators.cache import cache_page

from .views import *

urlpatterns = [
    path('', S1gh7ts7txrHome.as_view(), name='home'),
    path('info/', info, name='info'),
    path('addpage/', AddPage.as_view(), name='addpage'),
    path('feedback/', ContactFormView.as_view(), name='feedback'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('signup/', SignupUser.as_view(), name='signup'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', S1gh7ts7txrCategory.as_view(), name='category'),
]
