import tensorflow as tf
from captcha.image import ImageCaptcha
import numpy as np  
import matplotlib.pyplot as plt  
from PIL import Image,ImageFont
import random
import os
   

number = ['0','1','2','3','4','5','6','7','8','9']  
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']  
ALPHABET = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']  
chinese = ['人','入','日','目','岁','步', '钩','询', '师','脂', '沉', '肌']
def random_captcha_text(char_set=chinese, captcha_size=4):
    captcha_text = []  
    for i in range(captcha_size):  
        c = random.choice(char_set)  
        captcha_text.append(c)  
    return captcha_text  
   

def gen_captcha_text_and_image():
    fonts = ['SourceHanSans-Normal.ttf']
    image = ImageCaptcha(fonts=fonts)
   
    captcha_text = random_captcha_text()  
    captcha_text = ''.join(captcha_text)  
   
    captcha = image.generate(captcha_text)  
    #image.write(captcha_text, captcha_text + '.jpg')   
   
    captcha_image = Image.open(captcha)  
    # captcha_image = np.array(captcha_image)
    return captcha_text, captcha_image  
if __name__ == '__main__':  
    text, image = gen_captcha_text_and_image()  
   
    # f = plt.figure()
    # ax = f.add_subplot(111)
    # ax.text(0.1, 0.9,text, ha='center', va='center', transform=ax.transAxes)
    # plt.imshow(image)
    #
    # plt.show()
    image.save("t1.png")
    print(text)