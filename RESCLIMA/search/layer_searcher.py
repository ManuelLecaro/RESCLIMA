# encoding: utf-8
from utils import parseUserTextInput;

def create_str_polygon_postgis(polygon_dict):
	minX = polygon_dict["minX"];
	maxX = polygon_dict["maxX"];
	minY = polygon_dict["minY"];
	maxY = polygon_dict["maxY"];
	if (minX=='0' and maxX=='0' and minY=='0' and maxY=='0'):
		return None
	else:
		polygon_str = "SRID=4326;POLYGON((%s %s,%s %s,%s %s,%s %s,%s %s))::geometry"%(float(minX),float(minY),float(minX),float(maxY),float(maxX),float(maxY),float(maxX),float(minY),float(minX),float(minY));
		return polygon_str


def appendQueryPart(query,query_part, separator):
	return query + separator + query_part

# Genera un query dinamico depenciendo
# de las opciones de query_object
def create_query(query_object):
	# opciones de busqueda
	text = query_object.get("text","")
	categories = query_object.get("categories", [])
	bbox = query_object.get("bbox", None)
	ini_date = query_object.get("ini_date",None)
	end_date = query_object.get("end_date",None)

	# sql statements
	select_stm = 'SELECT l.id, l.title, l.abstract, l.type, l.bbox';

	from_stm = 'FROM "layer_layer" AS l';
	where_stm = 'WHERE';
	where_filters = [];
	params = []

	if(text or len(categories)>0):
		ts_query_str = parseUserTextInput(text,categories);
		print ts_query_str
		filter_str = 'ts_index @@ to_tsquery(\'spanish\',%s)'
		where_filters.append(filter_str);
		params.append(ts_query_str);


	if(bbox):
		bbox_str = create_str_polygon_postgis(bbox);
		if bbox_str == None:
			return "Error";
		filter_str = 'ST_Intersects(bbox,%s)';
		where_filters.append(filter_str);
		params.append(bbox_str);

	if(ini_date and end_date):
		filter_str = 'data_date >= %s and data_date <= %s';
		where_filters.append(filter_str)
		params.append(ini_date);
		params.append(end_date);

	sql_query = select_stm;
	sql_query = appendQueryPart(sql_query,from_stm," ");
	sql_query = appendQueryPart(sql_query,where_stm," ");

	for i,f in enumerate(where_filters):
		if (i==0):
			sql_query = appendQueryPart(sql_query,f," ");
		else:
			sql_query = appendQueryPart(sql_query,f," and ");

	print sql_query, params
	return sql_query, params


