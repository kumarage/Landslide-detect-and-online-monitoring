#!/usr/bin/env python
#image save:https://stackoverflow.com/questions/15018372/how-to-take-partial-screenshot-with-selenium-webdriver-in-python 
from selenium import webdriver
from PIL import Image
from pytesseract import image_to_string
import time
import os


try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
    from io import BytesIO

if __name__ == "__main__":

    wdriver = webdriver.PhantomJS(executable_path=r"phantomjs.exe")
    #wdriver = webdriver.Chrome(executable_path=r"chromedriver.exe")
    wdriver.set_window_size(1400,1000)
    wdriver.get("http://www.afreesms.com/intl/sri-lanka")

    to_num = 'xxxxxxxxx'
    mobile = wdriver.find_element_by_xpath("//input[@type='text']")
    mobile.send_keys(to_num)
    text1 = wdriver.get_screenshot_as_png()
    im1 = Image.open(BytesIO(text1))
    im1.save('text1.png')

    message = 'A Possible Landslide in your area. Please evacuate and reach a safe place !!!'
    mess_body = wdriver.find_element_by_xpath("//textarea")
    mess_body.send_keys(message)
    text2 = wdriver.get_screenshot_as_png()
    im2 = Image.open(BytesIO(text2))
    im2.save('text2.png')

    #element = wdriver.find_element_by_xpath('//*[@title="Reload the image"]').click()
    captcha = wdriver.find_element_by_id('captcha')
    location = captcha.location
    size = captcha.size
    print(location)
    print(size)

    png = wdriver.get_screenshot_as_png()
    im = Image.open(BytesIO(png)) # uses PIL library to open image in memory
    left = location['x']
    top = location['y']
    right = location['x'] + size['width']
    bottom = location['y'] + size['height']-10
    im = im.crop((left, top, right, bottom)) # defines crop points
    im.save('screenshot.png') # saves new cropped image
    
    im = Image.open('screenshot.png')
    text = image_to_string(im)
    
    verification_code = wdriver.find_element_by_xpath("//input[@type='text'][@style='width:80px']")
    verification_code.send_keys(text)
    text3 = wdriver.get_screenshot_as_png()
    im3 = Image.open(BytesIO(text3))
    im3.save('text3.png')
    print(text)

    send_button = wdriver.find_element_by_id("submit")
    send_button.click()

    time.sleep(6)
    text4 = wdriver.get_screenshot_as_png()
    im4 = Image.open(BytesIO(text4))
    im4.save('text4.png')

    wdriver.quit()

