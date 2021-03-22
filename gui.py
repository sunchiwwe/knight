import json
import requests
import os
import pprint
from tkinter import *
from tkinter import messagebox

def get_url():
    path = 'D:/baidupt'
    header={
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }#构建头文件，防止反爬
    num=0
    ptnum=1
    word=enter.get()
    page=int(pages.get())
    page=page+1
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
                f.close()
            num += 1
            download_message(num)
        ptnum += 29 #ptnum为总的张数
       
        
def download_message(num):
    listbox.insert(END,'图片{}正在下载'.format(num))
    listbox.see(END)
    listbox.update()



root=Tk()
root.geometry('500x300+300+300')
root.title('爱琳图片下载器  开发者：孙驰')
label=Label(root,text='请输入你想下载的照片',font=10,bg='black',fg='purple').grid(row=0,column=0)
label1=Label(root,text='你想下载的页数',font=10,bg='black',fg='purple').grid(row=1,sticky=W)
pages=Entry(root,font=10,fg='blue')
pages.grid(row=1,column=1)
enter=Entry(root,font=10,fg='purple')
enter.grid(row=0,column=1,padx=30,pady=20)#调整位置
enter.insert(0,'银河')
listbox=Listbox(root,font=10,width=40,height=10)
listbox.grid(row=2,columnspan=2)
downloadBtn = Button(root,text='开始下载',bg='black',fg='blue',command=get_url)
downloadBtn.grid(row=3,column=0,pady=10)
exitBtn = Button(root,text='退出程序',bg='black',fg='blue',command=root.quit)
exitBtn.grid(row=3,column=1,padx=5)
root.mainloop()
