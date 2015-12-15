import requests

def generateTilelayer(service_url, geo_user, geo_pwd, workspace_name, task_id, threadCount, zoomStart, zoomStop):
	s = requests.Session()
	data = {
		'username': geo_user,
		'password': geo_pwd
	}
	s.post(service_url+'/j_spring_security_check', data=data,allow_redirects=False)
	surl = service_url + '/gwc/rest/layers/' + workspace_name + ':' + task_id + '.json'
	print surl
	t = s.get(surl,allow_redirects=False)
	x = t.json()
	coords = x['GeoServerLayer']['gridSubsets'][1]['extent']['coords']
	payload = {
		'threadCount': threadCount,
		'type':'seed',
		'gridSetId': 'EPSG:4326',
		'format': 'image/png',
		'zoomStart': zoomStart,
		'zoomStop': zoomStop,
		'minX': coords[0],
		'minY': coords[1],
		'maxX': coords[2],
		'maxY': coords[3],
		'parameter_STYLES':'raster'
	}
	# testUrl = 'http://localhost:8080/geoserver/gwc/rest/seed/cde:series2_183_pix_gcp'
	xurl = service_url + '/gwc/rest/seed/' + workspace_name + ':' + task_id
	print xurl
	r = s.post(xurl, data=payload, allow_redirects=False)
	if r.status_code== 200:
		return 'Http Code=', r.status_code, '.Success.'
	else:
		return 'Http Code=', r.status_code, '.Failed'
# http://54.223.55.134:8080/gwc/rest/layers/user_liuzhusina:300.json
service_url = 'http://54.223.55.134:8080'
print generateTilelayer(service_url, 'admin', 'geoserver', 'user_liuzhusina', '170', 3, 0, 13)