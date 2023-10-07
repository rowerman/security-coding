import math
import numpy as np

class dtft():
#xvalues:输入序列
    def __init__(self,xvalues=[]):
        self.yvalues = []
        self.xvalues = xvalues
#fre:频率坐标
    def xjw(self,fre = []):
#（式1-1）实现yvalues为X（jw）频谱值
        for f in fre:
            p = 0
            for x in self.xvalues:
                p = math.e**(-1j*f*x) + p
            self.yvalues.append(p)
