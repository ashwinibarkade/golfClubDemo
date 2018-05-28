# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.views.generic.base import TemplateView
from teeTimeSellerApp import views

urlpatterns = [
        url(r'^getListOfAlgorithms$', views.rest_getListOfAlgorithms, name='getListOfAlgorithms'),
        #url(r'^getListOfFilesImported$', views.rest_getListOfFilesImported, name='getListOfFilesImported'),
        #url(r'^getJobStatus$', views.rest_getJobStatus, name='getJobStatus'),
        #url(r'^startJob$', views.rest_startJob, name='startJob'),
        #url(r'^recommendationEngine$', views.rest_provideRecommendation, name='provideRecommendation'),
        #url(r'^getColumnNames', views.rest_getColumnNames, name='getColumnNames'),
        #url(r'^fileUpload', views.File_Upload, name='fileUpload'),
        #url(r'^trainRegressionVisualization', views.rest_regression_train_visualization, name='trainRegressionVisualization'),
        #url(r'^predictRegressionVisualization', views.rest_regression_predict_visualization, name='predictRegressionVisualization'),
]