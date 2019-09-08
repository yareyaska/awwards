from django.conf.urls import url 
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'^new/post$', views.new_post, name='new-post'),
    url(r'^profile/$',views.profile,name='profile'),
    url(r'^new/profile/(\d+)$', views.new_profile, name='new-profile'),
    url(r'ratings/(\d+)$', views.ratings,name='ratings')   , 
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)