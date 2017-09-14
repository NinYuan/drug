from random import randint
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView
from django.http import HttpResponse
from django.shortcuts import render

class LineChartJSONView(BaseLineChartView):
    def  __init__(self,feature):
        self.feature=feature
        
    def get_labels(self):
        print "eachart888888888888"
        print self.feature
        """Return 7 labels for the x-axis."""
        return ["January", "February", "March", "April", "May", "June", "July"]

    def get_providers(self):
        """Return names of datasets."""
        return ["Central", "Eastside", "Westside"]

    def get_data(self):
        """Return 3 datasets to plot."""

        return [[75, 44, 92, 11, 44, 95, 35],
                [41, 92, 18, 3, 73, 87, 92],
                [87, 21, 94, 3, 90, 13, 65]]



line_chart = TemplateView.as_view(template_name='line_chart.html')

# feature=request.GET['feature']
# featureNum=request.GET['featureNum']
# drugs=request.GET['drugs']
# subfeaturesstr=request.GET['subfeatures']

# lc=LineChartJSONView(feature)
# line_chart_json = lc.as_view()

line_chart_json = LineChartJSONView.as_view()
