#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

from waveshare_1in8_LCD import LCD_1in8
from waveshare_1in8_LCD import LCD_Config

from PIL  import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageColor


def main():
    LCD = LCD_1in8.LCD()
    
    print ("**********Init LCD**********")
    Lcd_ScanDir = LCD_1in8.SCAN_DIR_DFT  #SCAN_DIR_DFT = D2U_L2R
    LCD.LCD_Init(Lcd_ScanDir)
    LCD.LCD_Clear(0xffff)
    image = Image.new("RGB", (LCD.LCD_Dis_Column, LCD.LCD_Dis_Page), "WHITE")
    draw = ImageDraw.Draw(image)

    # image = Image.open(picdir+'/logo.jpg')
    # LCD.LCD_ShowImage(image)
    draw.line([(0,5),(40,5)], fill = "YELLOW",width = 1)

    draw.line([(0,20),(40,20)], fill = "BLUE",width = 1)

    draw.line([(0,40),(40,40)], fill = "RED",width = 1)

    draw.line([(0,80),(40,80)], fill = "BLACK",width = 1)
    
    # draw.rectangle([(18,10),(110,20)],fill = "RED", outline='BLUE',width = 1)
    LCD.LCD_ShowImage(image)

if __name__ == '__main__':
    main()