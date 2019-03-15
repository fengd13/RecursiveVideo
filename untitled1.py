# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 20:40:03 2018

@author: fd
"""

import cv2
import moviepy.editor as mpy
import numpy as np
img=cv2.imread("1.png",-1)
#cv2.imshow("a",img[:,:,3])
time=0
start=[]
end=[]
def onmouse(event, x, y, flags, param):      #标准鼠标交互函数
    global time
    global start
    global end
    if event==1:           #当鼠标点击时
        print(img[y,x])                      #显示鼠标所在像素的数值，注意像素表示方法和坐标位置的不同
        if time==0:
            start=[y,x]
        if time==1:
            end=[y,x]
        time+=1
        
centerx=0
centery=0
now_zoom=1
def make_frame(t):
    global now_zoom
    """ Return the frame for time t """
    tempim=cv2.resize(bigimg,(int(now_zoom*y),int(now_zoom*x)))
    tempcx=int(centerx*now_zoom)
    tempcy=int(centery*now_zoom)
    immm=tempim[tempcx-centerx:tempcx+(x-centerx),tempcy-centery:tempcy+(y-centery),:]
    now_zoom=1+t*t/100*(zoom-1)
    a=t
        #cv2.imwrite("aa.png",immm)
        
    return  immm[:,:,0:3][...,::-1]   #bgr2rgb   gbr = rgb[...,[2,0,1]]


cv2.namedWindow("img")                   #构建窗口
cv2.setMouseCallback("img", onmouse)     #回调绑定窗口
#点两下鼠标显示预览图 点三下确认关闭 开始处理 按q退出重来

while True:                              #无限循环
    print(time)
    cv2.imshow("img",img)                #显示图像
    if cv2.waitKey() == ord('q'):break   #按下‘q’键，退出
cv2.destroyAllWindows()                  #关闭窗口
x,y,_=img.shape
zoom=x/(end[0]-start[0])

bigimg=cv2.resize(img,(int(zoom*y),int(zoom*x)),cv2.INTER_NEAREST)
bigx=int(zoom*x)
bigy=int(zoom*y)
#for iii in range(10):
#    start[1]=int(y/x*(start[0]-end[0])+end[1])
#    smallimg=cv2.resize(bigimg,(end[1]-start[1],end[0]-start[0]))
#    for i in range(end[0]-start[0]):
#        for j in range(end[1]-start[1]):
#            if smallimg[i,j,3]>0:
#                img[start[0]+i,start[1]+j,:]=smallimg[i,j,:]
start[1]=int((y/x*(start[0]-end[0])+end[1]))
for iii in range(10):
    
    smallimg=cv2.resize(bigimg,(y,x))
    for i in range(x):
        for j in range(y):
            if smallimg[i,j,3]>0:
                bigimg[int(start[0]*zoom+i),int(start[1]*zoom+j),:]=smallimg[i,j,:]
#cv2.imshow("img",bigimg)                #显示图像
cv2.imwrite("aa.png",bigimg)


centerx=int(start[0]*x/(x+start[0]-end[0]))
centery=int(start[1]*y/(y+start[1]-end[1]))
animation = mpy.VideoClip(make_frame, duration=10)
# 可以将结果写为视频或GIF（速度较慢）
#animation.write_gif(make_frame, fps=15)
animation.write_videofile('test.mp4', fps=20)
    
    
