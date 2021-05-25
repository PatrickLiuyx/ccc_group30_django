import plotly
import os
import sys
import couchdb

root_dir_name = "ccc_backend"
dir_path = os.path.abspath(sys.argv[0])
root_dir = dir_path[:dir_path.lower().find(root_dir_name) + len(root_dir_name)]
sys.path.insert(0, root_dir)

import config.couchdb_acc as conf
from django.shortcuts import render

plots_data = {
    'age_pie_Barwon_South_West': '27429f577b9a5b580223a0867d009125',
    'age_pie_Gippsland': '27429f577b9a5b580223a0867d00b8e5',
    'age_pie_Grampians': '27429f577b9a5b580223a0867d00beca',
    'age_pie_Greater_Melbourne': '27429f577b9a5b580223a0867d00c556',
    'age_pie_Hume': '27429f577b9a5b580223a0867d00d284',
    'age_pie_Loddon_Mallee': '27429f577b9a5b580223a0867d00e18e',
    'monthly_covidTweets_Bar': '27429f577b9a5b580223a0867d00ea80',
    'monthly_dist_pie': '27429f577b9a5b580223a0867d00f41d',
    'payroll_line_Barwon_South_West': '27429f577b9a5b580223a0867d02466d',
    'payroll_line_Gippsland': '27429f577b9a5b580223a0867d024e2b',
    'payroll_line_Grampians': '27429f577b9a5b580223a0867d025482',
    'payroll_line_Greater_Melbourne': '27429f577b9a5b580223a0867d02565f',
    'payroll_line_Hume': '27429f577b9a5b580223a0867d0264e8',
    'payroll_line_Loddon_Mallee': '27429f577b9a5b580223a0867d0273a3',
    'stockMarket_line': '27429f577b9a5b580223a0867d0123a4',
    'covidCases_bar': '27429f577b9a5b580223a0867d012fdb',
    'line15_17': '27429f577b9a5b580223a0867d030837',
    'bar15_17': '27429f577b9a5b580223a0867d0315e4'
}

filename_list = [
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
    'payroll_line_Hume',
    'payroll_line_Loddon_Mallee',
    'stockMarket_line',
    'line15_17',
    'bar15_17']

couch = couchdb.Server(
    'http://' + conf.instance_3_acc_name() + ':' + conf.instance_3_pass() + '@' + conf.instance_3_ip() + ':5984')
db1 = couch['img']
rows1 = db1.view('_all_docs', include_docs=True)
img_data = [row['doc'] for row in rows1]
plot_id = {}
for i in range(len(img_data)):
    plot = img_data[i]
    id_ = plot['_id']
    del plot['_id']
    del plot['_rev']
    plot_id[id_] = plot

data_dict = {}

for name_ in filename_list:
    try:
        data_dict[name_] = plot_id[plots_data[name_]]
    except:
        print(name_)


def line15_17(request):
    tmp_plot = plotly.offline.plot(data_dict['line15_17'], output_type='div')
    return render(request, 'emotion.html',
                  context={'line15_17': tmp_plot})


def payroll_line_Barwon_South_West(request):
    tmp_plot = plotly.offline.plot(data_dict['payroll_line_Barwon_South_West'], output_type='div')
    return render(request, './test_tmp/payroll_line_Barwon_South_West.html',
                  context={'payroll_line_Barwon_South_West': tmp_plot})


def payroll_line_Loddon_Mallee(request):
    tmp_plot = plotly.offline.plot(data_dict['payroll_line_Loddon_Mallee'], output_type='div')
    return render(request, './test_tmp/payroll_line_Loddon_Mallee.html',
                  context={'payroll_line_Loddon_Mallee': tmp_plot})


def payroll_line_Gippsland(request):
    tmp_plot = plotly.offline.plot(data_dict['payroll_line_Gippsland'], output_type='div')
    return render(request, './test_tmp/payroll_line_Gippsland.html', context={'payroll_line_Gippsland': tmp_plot})


def payroll_line_Grampians(request):
    tmp_plot = plotly.offline.plot(data_dict['payroll_line_Grampians'], output_type='div')
    return render(request, './test_tmp/payroll_line_Grampians.html', context={'payroll_line_Grampians': tmp_plot})


def payroll_line_Greater_Melbourne(request):
    tmp_plot = plotly.offline.plot(data_dict['payroll_line_Greater_Melbourne'], output_type='div')
    return render(request, './test_tmp/payroll_line_Greater_Melbourne.html',
                  context={'payroll_line_Greater_Melbourne': tmp_plot})


def payroll_line_Hume(request):
    tmp_plot = plotly.offline.plot(data_dict['payroll_line_Hume'], output_type='div')
    return render(request, './test_tmp/payroll_line_Hume.html', context={'payroll_line_Hume': tmp_plot})


def stockMarket_line(request):
    tmp_plot = plotly.offline.plot(data_dict['stockMarket_line'], output_type='div')
    return render(request, './test_tmp/stockMarket_line.html', context={'stockMarket_line': tmp_plot})


def age_pie_Barwon_South_West(request):
    tmp_plot = plotly.offline.plot(data_dict['age_pie_Barwon_South_West'], output_type='div')
    return render(request, './test_tmp/age_pie_Barwon_South_West.html', context={'age_pie_Barwon_South_West': tmp_plot})


def age_pie_Gippsland(request):
    tmp_plot = plotly.offline.plot(data_dict['age_pie_Gippsland'], output_type='div')
    return render(request, './test_tmp/age_pie_Gippsland.html', context={'age_pie_Gippsland': tmp_plot})


def age_pie_Grampians(request):
    tmp_plot = plotly.offline.plot(data_dict['age_pie_Grampians'], output_type='div')
    return render(request, './test_tmp/age_pie_Grampians.html', context={'age_pie_Grampians': tmp_plot})


def age_pie_Greater_Melbourne(request):
    tmp_plot = plotly.offline.plot(data_dict['age_pie_Greater_Melbourne'], output_type='div')
    return render(request, './test_tmp/age_pie_Greater_Melbourne.html', context={'age_pie_Greater_Melbourne': tmp_plot})


def age_pie_Hume(request):
    tmp_plot = plotly.offline.plot(data_dict['age_pie_Hume'], output_type='div')
    return render(request, './test_tmp/age_pie_Hume.html', context={'age_pie_Hume': tmp_plot})


def age_pie_Loddon_Mallee(request):
    tmp_plot = plotly.offline.plot(data_dict['age_pie_Loddon_Mallee'], output_type='div')
    return render(request, './test_tmp/age_pie_Loddon_Mallee.html', context={'age_pie_Loddon_Mallee': tmp_plot})


def monthly_dist_pie(request):
    tmp_plot = plotly.offline.plot(data_dict['monthly_dist_pie'], output_type='div')
    return render(request, ['emotion.html', './test_tmp/monthly_covidTweets_Bar.html'],
                  context={'monthly_dist_pie': tmp_plot})


def bar15_17(request):
    tmp_plot = plotly.offline.plot(data_dict['bar15_17'], output_type='div')
    return render(request, 'emotion.html', context={'bar15_17': tmp_plot})


def covidCases_bar(request):
    tmp_plot = plotly.offline.plot(data_dict['covidCases_bar'], output_type='div')
    return render(request, './test_tmp/covidCases_bar.html', context={'covidCases_bar': tmp_plot})


def monthly_covidTweets_Bar(request):
    tmp_plot = plotly.offline.plot(data_dict['monthly_covidTweets_Bar'], output_type='div')
    return render(request, 'emotion.html',
                  context={'monthly_covidTweets_Bar': tmp_plot})
