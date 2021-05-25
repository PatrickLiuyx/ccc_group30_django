from ccc_backend.api.views.yangjing import *
from ccc_backend.api.views.jade import *
from ccc_backend.api.views.yilin import *
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, re_path


urlpatterns = []

# url: http://127.0.0.1:8000/api/{urlpatterns}
# e.g. http:localhost:8000/api/map/Map_bySuburb_March

urlpatterns = [path('main/emotion.html/', multi_chart_emotion),]

urlpatterns += [path('main/social_impact.html', multi_chart_social)]

# show static file
# urlpatterns += [
#     re_path(r'^wordcloud_current/$', WC_current, name='wc'),
# ]
# urlpatterns += static('/wordcloud_current/', document_root=settings.MEDIA_ROOT)
#
# urlpatterns += [
#     re_path(r'^wordcloud_previous/$', WC_previous, name='wc'),
# ]
# urlpatterns += static('/wordcloud_previous/', document_root=settings.MEDIA_ROOT)
#
# urlpatterns += [
#     re_path(r'^wordcloud_before_the_previous/$', WC_before_the_previous, name='wc'),
# ]
# urlpatterns += static('/wordcloud_before_the_previous/', document_root=settings.MEDIA_ROOT)

urlpatterns += [path('main/', main_page)]

urlpatterns += [path('main/emotion.html/', emotion)]

urlpatterns += [path('main/timeline.html', timeline)]

urlpatterns += [path('main/live_tweets.html', live_tweets)]

urlpatterns += [path('main/social_impact.html', social_impact)]


