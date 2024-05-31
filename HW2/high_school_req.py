import requests
from bs4 import BeautifulSoup
import pandas as pd
if __name__ == '__main__':
    # 設定目標網址
    url = "https://zh.wikipedia.org/zh-tw/%E8%87%BA%E5%8C%97%E5%B8%82%E9%AB%98%E7%B4%9A%E4%B8%AD%E7%AD%89%E5%AD%B8%E6%A0%A1%E5%88%97%E8%A1%A8"

    # 發送 HTTP 請求
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'  # 確保正確的編碼

    # 解析網頁內容
    soup = BeautifulSoup(response.text, 'html.parser')

    # 找到所有 'table-td' class 的 div 標籤
    items = soup.find_all('table', class_="nowraplinks navbox-subgroup")
    index = 1
    data = []

    # 遍歷每個項目，爬取需要的資訊
    for item in items:
        try:
            title_tag = item.find('td',"navbox-list navbox-odd").find_all('a')
            for tag in title_tag:
                print(f"{tag.get('title')},{tag.get('href')}")
                data.append({'Name':tag.get('title'),'link':tag.get('href')})
            title_tag = item.find('td', "navbox-list navbox-even").find_all('a')
            for tag in title_tag:
                print(f"{tag.get('title')},{tag.get('href')}")
                data.append({'Name': tag.get('title'), 'link': tag.get('href')})
            index += 1
        except:
            continue
    df = pd.DataFrame(data)
    df.to_csv("high_school_request.csv", encoding='utf_8_sig', index=False)
