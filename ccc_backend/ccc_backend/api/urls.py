from ccc_backend.api.views.yangjing import *
from ccc_backend.api.views.jade import *
from ccc_backend.api.views.yilin import *
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, re_path

"""
['Map_bySuburb_April',
 'Map_bySuburb_August',
 'Map_bySuburb_December',
 'Map_bySuburb_July',
 'Map_bySuburb_June',
 'Map_bySuburb_March',
 'Map_bySuburb_May',
 'Map_bySuburb_November',
 'Map_bySuburb_October',
 'Map_bySuburb_September',
 'age_pie_Barwon_South_West',
 'age_pie_Gippsland',
 'age_pie_Grampians',
 'age_pie_Greater_Melbourne',
 'age_pie_Hume',
 'age_pie_Loddon_Mallee',
 'covidCases_bar',
 'monthly_covidTweets_Bar',
 'monthly_dist_pie',
 'payroll_line_Barwon_South_West',
 'payroll_line_Gippsland',
 'payroll_line_Grampians',
 'payroll_line_Greater_Melbourne',
 'payroll_line_Loddon_Mallee',
 'stockMarket_line']
 """

urlpatterns = []

# url: http://127.0.0.1:8000/api/{urlpatterns}
# e.g. http:localhost:8000/api/map/Map_bySuburb_March

urlpatterns = [
    path('main/emotion.html/', multi_chart_emotion),
    path('bar/covidCases_bar', covidCases_bar),
    path('line/payroll_line_Barwon_South_West', payroll_line_Barwon_South_West),
    path('line/payroll_line_Loddon_Mallee', payroll_line_Loddon_Mallee),
    path('line/payroll_line_Gippsland', payroll_line_Gippsland),
    path('line/payroll_line_Grampians', payroll_line_Grampians),
    path('line/payroll_line_Greater_Melbourne', payroll_line_Greater_Melbourne),
    path('line/payroll_line_Hume', payroll_line_Hume),
    path('line/stockMarket_line', stockMarket_line),
    path('pie/age_pie_Barwon_South_West', age_pie_Barwon_South_West),
    path('pie/age_pie_Gippsland', age_pie_Gippsland),
    path('pie/age_pie_Grampians', age_pie_Grampians),
    path('pie/age_pie_Greater_Melbourne', age_pie_Greater_Melbourne),
    path('pie/age_pie_Hume', age_pie_Hume),
    path('pie/age_pie_Loddon_Mallee', age_pie_Loddon_Mallee),
]

# show static file
urlpatterns += [
    re_path(r'^wordcloud_current/$', WC_current, name='wc'),
]
urlpatterns += static('/wordcloud_current/', document_root=settings.MEDIA_ROOT)

urlpatterns += [
    re_path(r'^wordcloud_previous/$', WC_previous, name='wc'),
]
urlpatterns += static('/wordcloud_previous/', document_root=settings.MEDIA_ROOT)

urlpatterns += [
    re_path(r'^wordcloud_before_the_previous/$', WC_before_the_previous, name='wc'),
]
urlpatterns += static('/wordcloud_before_the_previous/', document_root=settings.MEDIA_ROOT)

urlpatterns += [path('main/', main_page)]

urlpatterns += [path('main/emotion.html/', emotion)]

urlpatterns += [path('main/emotion.html/main.html', main_page)]

urlpatterns += [path('main/emotion.html/emotion.html', emotion)]

urlpatterns += [path('main/timeline.html', timeline)]

urlpatterns += [path('main/live_tweets.html', live_tweets)]

urlpatterns += [path('main/social_impact.html', social_impact)]
