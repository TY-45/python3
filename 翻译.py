import json
from urllib import request,parse


print("输入 BBB 退出")
while True:
    content = input("请输入要翻译的单词：")
    if content == "BBB":
        break;
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'}
    req = request.Request('http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule')
    response = request.urlopen(req)

    Form_Data={ #提交数据
            "i":content,
            "from":"AUTO",
            "to":"AUTO",
            "smartresult":"dict",
            "client":"fanyideskweb",
            "salt":"1543202782988",
            "sign":"a7beafbc293ab82a029ee987adc97fc8",
            "doctype":"json",
            "version":"2.1",
            "keyfrom":"fanyi.web",
            "action":"FY_BY_REALTIME",
            "typoResult":"false"
        }
    data = parse.urlencode(Form_Data).encode('utf-8')
    response = request.urlopen(url=req,data=data)
    html = response.read().decode('utf-8')
    result_url = json.loads(html)

    result = result_url['translateResult'][0][0]['tgt']
    print("翻译结果为：", result)

