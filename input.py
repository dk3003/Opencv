# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 17:30:58 2018

@author: karth
"""

import cv2
def main():
    path="D:\\cv\\misc\\4.1.08.tiff"
    img=cv2.imread(path,-1)
    outputpath="D:\\cv\\output\\4.1.08.jpg"
    cv2.namedWindow('damishdishu',cv2.WINDOW_AUTOSIZE)
    cv2.imshow("damishdishu",img)
    print(img.shape)
    cv2.imwrite(outputpath,img)
    cv2.waitKey(0)
    cv2.destroyWindow('damishdishu')
if __name__ == "__main__":
    main()