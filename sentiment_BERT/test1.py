import requests
import pandas as pd
import json
import time
import urllib

data = {
    "current_refinement_paths": ["/for_you"],
    "current_tab_id": "all_tab",
    "federated_search_id": "7922e000-c0c5-4f5d-8cd6-438d97811f5a",
    "federated_search_session_id": "707e36ca-a0c4-41dd-b0b5-62d8f8a50f0f",
    "gtm_experiments": [],
    "has_map": "false",
    "map_toggle": "true",
    "marquee_mode": "DEFAULT",
    "page_metadata": {"page_title": "度假屋、民宿、体验和攻略 - Airbnb爱彼迎", "render_type": "EXPLORE", "location_query": "true"},
    "parent_administrative_area": {},
    "price_display_strategy": "CONTROL",
    "query_text": "搜“墨尔本”试试",
    "recent_searches_responses": {},
    "request_uuid": "f8ee3ebb-7435-80be-b3f2-8a8e253c073c",
    "satori_config": {"market": "Beijing", "state_code": "", "country_code": "CN", "region_id": "-1", "version": "1.1.13"},
    "satori_version": "1.0.3",
    "saved_search_responses": [],
    "search_id": "f8ee3ebb-7435-80be-b3f2-8a8e253c073c",
    "show_as_hint": "true",
        }

url = 'https://www.airbnb.cn'
headers =  {
    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'accept-encoding':'gzip, deflate, sdch, br',
    'accept-language':'zh-CN,zh;q=0.8',
    'cache-control':'max-age=0',
    'cookie':'cdn_exp_8b0a302e9114b448a=control; cdn_exp_bbe2630836041e67f=control; bev=1564443985_EyKSjdp3WfXhaw9P; _csrf_token=V4%24.airbnb.cn%24PgZ_y9uHGMg%248VUPhxd-3rvk2E5xQNXVih0B9zcHIzkss-nGa15jVGk%3D; jitney_client_session_created_at=1564472786; _user_attributes=%7B%22curr%22%3A%22CNY%22%2C%22guest_exchange%22%3A6.89131%2C%22device_profiling_session_id%22%3A%221564472786--f09116f59075091358430c1d%22%2C%22giftcard_profiling_session_id%22%3A%221564472786--051093bfd8fc05563051be4e%22%2C%22reservation_profiling_session_id%22%3A%221564472786--dac1f8f2ff4993f00b4f23d6%22%7D; flags=0; sdid=; cbkp=3; __ag_cm_=1; __xsptplus840=840.1.1564443993.1564443993.1%234%7C%7C%7C%7C%7C%23%23zkQOLdRqstXHIEaoO9HAHErKfMKsGVG-%23; jitney_client_session_updated_at=1564443988; jitney_client_session_id=052df591-e425-4c41-aed5-3157ebc1a3b1; ag_fid=GIOhnmXALIfLqVHF',
    'if-none-match':'W/"6ba41-4dRPW/ksE1fi/1/vbUm1B9Sv/hg"',
    'upgrade-insecure-requests':'1',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0',
}
URL = url + '?' + urllib.parse.urlencode(data)
print(URL)
# response = requests.get(URL)
# r = requests.get('https://api.github.com/events')
# answer = r.json()
# print(answer)
# answer1=response.content()
# print(answer1)
# answer = response.json()
# print(response)
#print(response.json())
#list = response['explore_tabs'][0]['sections'][0]['listings']
import urllib.parse
print(urllib.parse.quote('ChIJb_KF3fiuLjQRECJYbKzJwjk'))