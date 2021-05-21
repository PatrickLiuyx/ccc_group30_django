from os import walk
import json
from django.shortcuts import render
from django.http import HttpResponse
import plotly.io as pio
from plotly.offline import plot
from plotly.graph_objs import Scatter
import plotly
from django.shortcuts import render,HttpResponse


def WC_1(request):
    img = 'WC1621397367.png'
    return render(request, 'WC_1.html', {"WC_1": img})