from django.conf.urls import *
from django.contrib import admin
from views import *

urlpatterns = [
    # Examples:
    # url(r'^$', 'wordlife.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', HomeView.as_view(), name="home"),
    url(r'^list/(?P<list_id>\d+)/$', WordListView.as_view(), name="word_list"),
    url(r'^word/(?P<word>[^/]+)/$', WordListView.as_view(), name="word"),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
]
