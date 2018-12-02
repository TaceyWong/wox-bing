# coding:utf-8

from __future__ import absolute_import
import sys
import os
sys.path.insert(0,os.sep.join(os.path.abspath(__file__).split(os.sep)[:-1]))
from wox import Wox,WoxAPI
from baidu import transelate as baidu_transe

class Transelation(Wox):
    
    def query(self, *query):
        ori = " ".join(query)
        results = []
        WoxAPI.start_loadingbar()
        transe_result = baidu_transe(ori)
        for  item in transe_result:        
            results.append({
                "Title": item['dst'],
                "SubTitle": "Ori: {}".format(ori),
                "IcoPath":"Images{}bing.png".format(os.sep),
                "ContextData": "ctxData"
            })
        WoxAPI.stop_loadingbar()        
        return results

if __name__ == "__main__":
    Transelation()