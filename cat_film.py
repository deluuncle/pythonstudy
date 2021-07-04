import requests
def get_one_page(url):
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
    }
    responese = requests.get(url,headers=headers, verify=False)
    if responese.status_code == 200:
        return responese.text
    return None



def main():
    url = "http://maoyan.com/board/4"
    html = get_one_page(url)
    print(html)


main()
