# import json
# import plotly
# import couchdb
# from django.shortcuts import render
# from config.couchdb_acc import *
#
# plots_data = {
#     'age_pie_Barwon_South_West': '27429f577b9a5b580223a0867d009125',
#     'age_pie_Gippsland': '27429f577b9a5b580223a0867d00b8e5',
#     'age_pie_Grampians': '27429f577b9a5b580223a0867d00beca',
#     'age_pie_Greater_Melbourne': '27429f577b9a5b580223a0867d00c556',
#     'age_pie_Hume': '27429f577b9a5b580223a0867d00d284',
#     'age_pie_Loddon_Mallee': '27429f577b9a5b580223a0867d00e18e',
#     'monthly_covidTweets_Bar': '27429f577b9a5b580223a0867d00ea80',
#     'monthly_dist_pie': '27429f577b9a5b580223a0867d00f41d',
#     'payroll_line_Barwon_South_West': '27429f577b9a5b580223a0867d00fbdb',
#     'payroll_line_Gisppsland': '27429f577b9a5b580223a0867d00fcfe',
#     'payroll_line_Grampians': '27429f577b9a5b580223a0867d010a9c',
#     'payroll_line_Greater_Melbourne': '27429f577b9a5b580223a0867d0111aa',
#     'payroll_line_Hume': '27429f577b9a5b580223a0867d011527',
#     'payroll_line_Londdon_Mallee': '27429f577b9a5b580223a0867d0117b2',
#     'stockMarket_line': '27429f577b9a5b580223a0867d0123a4',
#     'covidCases_bar': '27429f577b9a5b580223a0867d012fdb'
# }
#
# filename_list = [
#     'Map_bySuburb_April',
#     'Map_bySuburb_August',
#     'Map_bySuburb_December',
#     'Map_bySuburb_July',
#     'Map_bySuburb_June',
#     'Map_bySuburb_March',
#     'Map_bySuburb_May',
#     'Map_bySuburb_November',
#     'Map_bySuburb_October',
#     'Map_bySuburb_September',
#     'age_pie_Barwon_South_West',
#     'age_pie_Gippsland',
#     'age_pie_Grampians',
#     'age_pie_Greater_Melbourne',
#     'age_pie_Hume',
#     'age_pie_Loddon_Mallee',
#     'covidCases_bar',
#     'monthly_covidTweets_Bar',
#     'monthly_dist_pie',
#     'payroll_line_Barwon_South_West',
#     'payroll_line_Gippsland',
#     'payroll_line_Grampians',
#     'payroll_line_Greater_Melbourne',
#     'payroll_line_Hume',
#     'payroll_line_Loddon_Mallee',
#     'stockMarket_line']
#
# couchdb_connection_status = False
# try:
#     couch = couchdb.Server('http://' + instance_3_acc_name + ':' + instance_3_pass + \
#                            '@' + instance_3_ip + ':5984')
#     db1 = couch['img']
#     rows1 = db1.view('_all_docs', include_docs=True)
#     img_data = [row['doc'] for row in rows1]
#     plot_id = {}
#     for i in range(len(img_data)):
#         plot = img_data[i]
#         id_ = plot['_id']
#         del plot['_id']
#         del plot['_rev']
#         plot_id[id_] = plot
#     couchdb_connection_status = True
# except:
#     print("Failed to connect CouchDB")
#
# # the local path of Graph data
# file_url = '/Users/yuxuanliu/Desktop/Desktop - Yuxuan’s MacBook Pro/graph_json/'
#
# data_dict = {}
# if couchdb_connection_status:
#     for name_ in filename_list:
#         if name_ not in plots_data:
#             tmp_dirpath = file_url + name_ + '.json'
#             with open(tmp_dirpath, 'r') as file:
#                 for each_ in file:
#                     data_ = each_
#                     data_2 = json.loads(each_)
#                     data_dict[name_] = data_2
#         else:
#             data_dict[name_] = plot_id[plots_data[name_]]
# else:
#     for name_ in filename_list:
#         tmp_dirpath = file_url + name_ + '.json'
#         with open(tmp_dirpath, 'r') as f:
#             for each_ in f:
#                 data_ = each_
#                 data_ = json.loads(each_)
#                 data_dict[name_] = data_
#
#
# def Map_bySuburb_March(request):
#     tmp_plot = plotly.offline.plot(data_dict['Map_bySuburb_March'], output_type='div')
#     return render(request, 'Map_bySuburb_March.html', context={'Map_bySuburb_March': tmp_plot})
#
#
# def Map_bySuburb_April(request):
#     tmp_plot = plotly.offline.plot(data_dict['Map_bySuburb_April'], output_type='div')
#     return render(request, 'Map_bySuburb_April.html', context={'Map_bySuburb_April': tmp_plot})
#
#
# def Map_bySuburb_May(request):
#     tmp_plot = plotly.offline.plot(data_dict['Map_bySuburb_May'], output_type='div')
#     return render(request, 'Map_bySuburb_May.html', context={'Map_bySuburb_May': tmp_plot})
#
#
# def Map_bySuburb_June(request):
#     tmp_plot = plotly.offline.plot(data_dict['Map_bySuburb_June'], output_type='div')
#     return render(request, 'Map_bySuburb_June.html', context={'Map_bySuburb_June': tmp_plot})
#
#
# def Map_bySuburb_July(request):
#     tmp_plot = plotly.offline.plot(data_dict['Map_bySuburb_July'], output_type='div')
#     return render(request, 'Map_bySuburb_July.html', context={'Map_bySuburb_July': tmp_plot})
#
#
# def Map_bySuburb_August(request):
#     tmp_plot = plotly.offline.plot(data_dict['Map_bySuburb_August'], output_type='div')
#     return render(request, 'Map_bySuburb_August.html', context={'Map_bySuburb_August': tmp_plot})
#
#
# def Map_bySuburb_September(request):
#     tmp_plot = plotly.offline.plot(data_dict['Map_bySuburb_September'], output_type='div')
#     return render(request, 'Map_bySuburb_September.html', context={'Map_bySuburb_September': tmp_plot})
#
#
# def Map_bySuburb_October(request):
#     tmp_plot = plotly.offline.plot(data_dict['Map_bySuburb_October'], output_type='div')
#     return render(request, 'Map_bySuburb_October.html', context={'Map_bySuburb_October': tmp_plot})
#
#
# def Map_bySuburb_November(request):
#     tmp_plot = plotly.offline.plot(data_dict['Map_bySuburb_November'], output_type='div')
#     return render(request, 'Map_bySuburb_November.html', context={'Map_bySuburb_November': tmp_plot})
#
#
# def Map_bySuburb_December(request):
#     tmp_plot = plotly.offline.plot(data_dict['Map_bySuburb_December'], output_type='div')
#     return render(request, 'Map_bySuburb_December.html', context={'Map_bySuburb_December': tmp_plot})
#
#
# def payroll_line_Barwon_South_West(request):
#     tmp_plot = plotly.offline.plot(data_dict['payroll_line_Barwon_South_West'], output_type='div')
#     return render(request, 'payroll_line_Barwon_South_West.html', context={'payroll_line_Barwon_South_West': tmp_plot})
#
#
# def payroll_line_Loddon_Mallee(request):
#     tmp_plot = plotly.offline.plot(data_dict['payroll_line_Loddon_Mallee'], output_type='div')
#     return render(request, 'payroll_line_Loddon_Mallee.html', context={'payroll_line_Loddon_Mallee': tmp_plot})
#
#
# def payroll_line_Gippsland(request):
#     tmp_plot = plotly.offline.plot(data_dict['payroll_line_Gippsland'], output_type='div')
#     return render(request, 'payroll_line_Gippsland.html', context={'payroll_line_Gippsland': tmp_plot})
#
#
# def payroll_line_Grampians(request):
#     tmp_plot = plotly.offline.plot(data_dict['payroll_line_Grampians'], output_type='div')
#     return render(request, 'payroll_line_Grampians.html', context={'payroll_line_Grampians': tmp_plot})
#
#
# def payroll_line_Greater_Melbourne(request):
#     tmp_plot = plotly.offline.plot(data_dict['payroll_line_Greater_Melbourne'], output_type='div')
#     return render(request, 'payroll_line_Greater_Melbourne.html', context={'payroll_line_Greater_Melbourne': tmp_plot})
#
#
# def payroll_line_Hume(request):
#     tmp_plot = plotly.offline.plot(data_dict['payroll_line_Hume'], output_type='div')
#     return render(request, 'payroll_line_Hume.html', context={'payroll_line_Hume': tmp_plot})
#
#
# def stockMarket_line(request):
#     tmp_plot = plotly.offline.plot(data_dict['stockMarket_line'], output_type='div')
#     return render(request, 'stockMarket_line.html', context={'stockMarket_line': tmp_plot})
#
#
# def age_pie_Barwon_South_West(request):
#     tmp_plot = plotly.offline.plot(data_dict['age_pie_Barwon_South_West'], output_type='div')
#     return render(request, 'age_pie_Barwon_South_West.html', context={'age_pie_Barwon_South_West': tmp_plot})
#
#
# def age_pie_Gippsland(request):
#     tmp_plot = plotly.offline.plot(data_dict['age_pie_Gippsland'], output_type='div')
#     return render(request, 'age_pie_Gippsland.html', context={'age_pie_Gippsland': tmp_plot})
#
#
# def age_pie_Grampians(request):
#     tmp_plot = plotly.offline.plot(data_dict['age_pie_Grampians'], output_type='div')
#     return render(request, 'age_pie_Grampians.html', context={'age_pie_Grampians': tmp_plot})
#
#
# def age_pie_Greater_Melbourne(request):
#     tmp_plot = plotly.offline.plot(data_dict['age_pie_Greater_Melbourne'], output_type='div')
#     return render(request, 'age_pie_Greater_Melbourne.html', context={'age_pie_Greater_Melbourne': tmp_plot})
#
#
# def age_pie_Hume(request):
#     tmp_plot = plotly.offline.plot(data_dict['age_pie_Hume'], output_type='div')
#     return render(request, 'age_pie_Hume.html', context={'age_pie_Hume': tmp_plot})
#
#
# def age_pie_Loddon_Mallee(request):
#     tmp_plot = plotly.offline.plot(data_dict['age_pie_Loddon_Mallee'], output_type='div')
#     return render(request, 'age_pie_Loddon_Mallee.html', context={'age_pie_Loddon_Mallee': tmp_plot})
#
#
# def monthly_dist_pie(request):
#     tmp_plot = plotly.offline.plot(data_dict['monthly_dist_pie'], output_type='div')
#     return render(request, 'monthly_dist_pie.html', context={'monthly_dist_pie': tmp_plot})
#
#
# def covidCases_bar(request):
#     tmp_plot = plotly.offline.plot(data_dict['covidCases_bar'], output_type='div')
#     return render(request, 'covidCases_bar.html', context={'covidCases_bar': tmp_plot})
#
#
# def monthly_covidTweets_Bar(request):
#     tmp_plot = plotly.offline.plot(data_dict['monthly_covidTweets_Bar'], output_type='div')
#     return render(request, 'monthly_covidTweets_Bar.html', context={'monthly_covidTweets_Bar': tmp_plot})
