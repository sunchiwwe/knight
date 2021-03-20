import json
import requests
import os
import pprint
path = 'D:/baidupt'
header={
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}#构建头文件，防止反爬
word=input('你想搜索的图片')
page=input('想下载的页数')
page=int(page)+1
num=0
ptnum=1
for m in range(1, page):
    url = 'https://image.baidu.com/search/acjson?'
    param = {
        'tn': 'resultjson_com',
        'logid': ' 5895221162371302533',
        'ipn': 'rj',
        'ct': '201326592',
        'is': '',
        'fp': 'result',
        'queryWord': word,
        'cl': '2',
        'lm': '-1',
        'ie': 'utf-8',
        'oe': 'utf-8',
        'adpicid': '',
        'st': '',
        'z': '',
        'ic': '',
        'hd': '',
        'latest': '',
        'copyright': '',
        'word': word,
        's': '',
        'se': '',
        'tab': '',
        'width': '',
        'height': '',
        'face': '',
        'istype': '',
        'qc': '',
        'nc': '1',
        'fr': '',
        'expermode': '',
        'force': '',
        'cg': 'star',
        'pn': ptnum,
        'rn': '30',
        'gsm': '1e',
    }
    image_url=list()
    response=requests.get(url=url,headers=header,params=param)
    response.encoding = 'utf-8'
    response = response.text
    data_s = json.loads(response)
    a = data_s["data"]  # 提取data里的数据
    for i in range(len(a)-1):  # 这是是要去掉最后一个空数据
        data = a[i].get("thumbURL") 
        image_url.append(data)
    for image_src in image_url:
        image_data = requests.get(url=image_src, headers=header).content  # 提取图片内容数据
        image_name = '{}'.format(num+1) + '.jpg'  # 图片名
        image_path = path + '/' + word +image_name  # 图片保存路径
        with open(image_path, 'wb') as f:  # 保存数据
            f.write(image_data)
            print(image_name, '下载成功啦！！！')
            f.close()
        num += 1
    ptnum += 29 #ptnum为总的张数
