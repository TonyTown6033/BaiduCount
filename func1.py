import requests
from bs4 import BeautifulSoup 
from baiduspider import BaiduSpider
from pprint import pprint



def getCouples(filename:str):
    
    """
    str is a path 
        which is one of the strings 
    """
    key1 = []
    
    with open(filename,'r') as file:
        for line in file:
            key1.append(line.split("\n")[0])    

    return key1


def getResponse(key1:str,key2:str):
    url = "https://www.baidu.com/s?wd="+key1+"%20"+key2
    response = requests.get(url) 
    return response

def analysis(responese):
    pass



if __name__ == "__main__":
    #pprint(BaiduSpider().search_web(input('搜索词：')).plain)
    result = BaiduSpider.search_web(query='篮球 科比')

    print(result)
    print("\n")
    pprint(result)
    