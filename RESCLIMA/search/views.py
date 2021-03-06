from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.db import connection
from django.core.paginator import Paginator
from search.models import Category
import json
import sys 
import os
import search.layer_searcher as layer_searcher
import search.series_searcher as series_searcher


def categories_json(request):
	categories = Category.objects.all()
	result = []
	for category in categories:
		result.append({"id":category.id,
			      "name":category.name,
			      "selected":False})

	result_json = json.dumps({"categories":result});
	return HttpResponse(result_json,content_type='application/json')
			


def search_layer(request):
	query_str = request.body
	query_dict = json.loads(query_str)
	#print "el query de busqueda ******",query_dict
	qs,params = layer_searcher.create_query(query_dict)
	layers = []
	full_count = 0;
	with connection.cursor() as cursor:
		cursor.execute(qs, params)
		rows = cursor.fetchall()
		for row in rows:
			layer = {}
			layer["id"] = row[0]
			layer["title"] = row[1]
			layer["abstract"] = row[2]
			layer["type"] = row[3]
			layer["selected"] = False
			full_count = row[5]
			layers.append(layer)
	return JsonResponse({"layers":layers,"full_count":full_count})

def search_series(request):
	query_str = request.body;
	query_dict = json.loads(query_str)
	qs,params = series_searcher.getTsTextQuery(query_dict)
	series = []
	full_count = 0;
	print(qs)
	print(params)
	with connection.cursor() as cursor:
		cursor.execute(qs, params)
		rows = cursor.fetchall()
		for row in rows:
			serie = {}
			serie["variable_id"]=row[0]
			serie["variable_name"]=row[1]
			serie["stations"] = row[2]
			serie["selected"] = False
			full_count=row[3]
			series.append(serie);
	return JsonResponse({"series":series,"full_count":full_count})

