#coding:utf-8
#autor:伊恒
import requests,base64,logging,time,json
import argparse
import base64
import apikey
from requests.packages.urllib3 import disable_warnings
disable_warnings()

print('''
db    db .d8888.  .o88b.  .d8b.  d8b   db
`8b  d8' 88'  YP d8P  Y8 d8' `8b 888o  88
 `8bd8'  `8bo.   8P      88ooo88 88V8o 88
   88      `Y8b. 8b      88~~~88 88 V8o88
   88    db   8D Y8b  d8 88   88 88  V888 
   YP    `8888Y'  `Y88P' YP   YP VP   V8P ''')

def Args():

    parse=argparse.ArgumentParser()
    parse.add_argument('-a','--api',help='需要查询的内容')
    parse.add_argument('-f','--file',help='需要保存文件的位置')
    parse.add_argument('-s','--size',help='提取页数')

    args=parse.parse_args()

    if args.api is None and args.file is None:
        print(parse.print_help())
    else:
        return args
session=requests.session()
headers = {
    'Upgrade-Insecure-Requests': '1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}

def main():
    args = Args()
    try:
        print(args.api)
        size=args.size
        qbase = base64.b64encode(args.api.encode()).decode()
        # 查询的 API
        api_url = "https://fofa.info/api/v1/search/all?email={email}&key={key}&qbase64={qbase}&size={size}".format(email=apikey.email, key=apikey.key, qbase=qbase,size=size)
        print(api_url)
        rs = session.get(api_url, verify=False, headers=headers,timeout=20)
        rs_text = rs.text
        results = json.loads(rs_text)
        print(results)
        print('\n')

        with open(args.file + '_' + str(len(results["results"])) + '.txt', 'a') as fi:
            for i in results["results"]:
                # print i[0]
                fi.write('%s \n' % (i[0].encode('utf-8').decode()))
        print(len(results["results"]))
    except Exception as e:
        print("请配置正确的fofa api")
if __name__ == "__main__":
    main()
