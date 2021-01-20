import cv2
import numpy as np
from processing import proc_img
from PIL import Image
from CCCD_class import CCCD
from classify import  classify


def single_pic_proc(image_file):
    image = np.array(Image.open(image_file).convert('RGB')) #chuyển ảnh xám
    result, image_framed = proc_img(image) #nhận dạng, gọi hàm proc_img của module processing
    return result,image_framed #trả về
#Hàm xử lí ảnh trả về ảnh đã vẽ khung và kết quả nhận dạng


def show_img(image): 
    cv2.imshow('image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
#Hàm hiển thị ảnh


def print_list_text(list_img):
    for text in list_img:
        print('TEXT OUTPUT:' + text)
#Hàm in danh sách kết quả



def output_proc(results):#xử lí kết quả đầu ra
    id = ' '
    name = ' '
    birth = ' '
    nationality = ' '
    sex = ' '
    hometown = ' '
    address = ' '
    cccd = CCCD(id,name,birth,nationality,sex,hometown,address)
    cccd = classify(results) #phân loại
    cccd.print_cccd()
    



if __name__ == '__main__':
    import sys
    if len(sys.argv)>=2:
        filename = sys.argv[1]
        if filename.endswith('jpg') or filename.endswith('png'): #nhận đầu vào là đuôi jpg hoặc png
            results, image_framed = single_pic_proc(filename) #Hàm trả về là kết quả dạng array và img đã đóng khung
            show_img(image_framed) #hiển thị ảnh
            #print(results) #hiển thị kết quả
            output_proc(results)




