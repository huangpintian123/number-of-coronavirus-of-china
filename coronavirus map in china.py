import  time,json,requests,jsonpath


def catch_map():
    timestamp = '%d'%int (time.time()*1000)
    url_area = ('https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5''&callback=&_=') + timestamp
    world_data = json.loads(requests.get(url=url_area).json()['data'])
    china_data = jsonpath.jsonpath(world_data, expr='$.areaTree[0].children[*]')
    ls_province_names = jsonpath.jsonpath(china_data, expr='$[*].name')
    ls_confirm_vals = jsonpath.jsonpath(china_data, expr='$[*].total.confirm')
    ls_province_confirm = list(zip(ls_province_names,ls_confirm_vals,))
    return ls_province_confirm

ls_province_cfm  = catch_map()
print(ls_province_cfm)

