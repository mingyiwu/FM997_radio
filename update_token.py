#!/usr/bin/env python3

# Author: Mingyi Wu (mingi.wu@gmail.com)
# Date: 2020/01/22
#
# Usage:
#     $ ./update_token.py
#    
#     執行後會的步驟:
#     1. fetch 愛樂電台官網資料
#     2. searh 網頁內的電台 URL
#     3. 根據 2. 的結果更新對應的三個 .xspf 播放檔
#
# Play .xspf example:
#    $ cvlc FM997_onAir.xspf
#    or
#    $ vlc FM997_onAir.xspf
#    or
#    Double click the icon of FM997_onAir.xspf
#

import os
import urllib.request
import re


FILESDICT = { 
        "ra000018": "FM997_onAir.xspf", 
        "ra000109": "FM997_Jazz.xspf",
        "ra000120": "FM997_OBG.xspf" }


def fetch(keeppage=False):
    page = urllib.request.urlopen("https://www.e-classical.com.tw/index.html")

    #print(page.read())

    content = page.read()
    content = content.decode()

    if keeppage:
        with open("rawpage.html", 'w') as f:
            f.writelines(content)

    return content


def loadarchive():
    with open("rawpage.html", 'r') as f:
         content = f.readlines()
    
    return "\n".join(content)


if __name__ == "__main__":
    pattern = re.compile("(https://.+token=\w+&expires=\d+)", flags = re.MULTILINE)


    ## for debug preparation
    #content = fetch(True)

    ## for test and debug
    #content = loadarchive()

    ## for normal usage
    content = fetch()

    ## Find all possible tokens and expires (for OnAir, Jazz, OBG)
    matchs = pattern.findall(content)
    matchs.sort()


    for i, url in enumerate(matchs):
        ## xspf 內的 & 符號要改成 &amp; , 但 content 的網址是用 & 
        url = url.replace("&", "&amp;")

        ## 根據抓到的 url 名稱找尋對應的 xspf 檔案
        ra_match = re.search("ra\d+",url)
        fn = os.path.join(os.path.dirname(__file__), FILESDICT.get(ra_match.group(0)) )

        ## 讀取 xspf 內容
        with open(fn, "r") as f:
            xml = f.readlines()
        
        ## search <location>...</location> and replace the URL
        new_xml = []
        MATCH=False
        pattern_in_xspf = re.compile("<location>(.+)</location>")
        for oneline in xml:
            # Search URL in the xspf file 
            match = pattern_in_xspf.search(oneline)
            
            if match:
                oneline = re.sub(pattern_in_xspf, "<location>"+ url +"</location>", oneline) 
                MATCH=True

            new_xml.append(oneline)

        if MATCH:
            with open(fn, "w") as f:
                f.writelines(new_xml)
            
                print("Updated {}".format(fn))
                print("--------")
