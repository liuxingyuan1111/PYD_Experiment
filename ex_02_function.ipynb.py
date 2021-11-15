# -*- coding: utf-8 -*-

#小组：puffer
#实验二：小组第一次作业
#代码文件统一命名为ex_02_function.ipynb，并由组长上传至组长的GitHub账户，单独建立代码仓库repository，各组统一命名为:｀PYD_Experiment｀。
#文件中，需说明函数的意图，输入参数，和返回值等信息。并应用该函数实际运算演示。


#目的：计算楼梯间休息平台的宽度



#已知进深（depth）=6000mm，净高(net_height)=3000mm，踢面高度(road_height)=175mm
#且踏面宽度（width）=600-2*踢面高度（road_height)
#且楼梯级数（degree）=净高(net_height)/踢面高度（road_height)
#通过计算求解楼梯间休息平台宽度



#设定计算公式
import math

def calcRestPlatform(depth, net_height, road_height):
    degree = math.ceil(net_height / road_height)
    width = 600.0 - 2.0 * road_height;
    rp = (depth - width * (degree - 1))/2.0
    return rp;


#输入参数，求得结果
if __name__ == '__main__':
    print(calcRestPlatform(6000.0, 3000.0, 175.0))
    
    
    
#计算结束
    