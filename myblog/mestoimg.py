# -*- coding: utf-8 -*-
# 文字產生圖片

from PIL import Image, ImageDraw, ImageFont
import textwrap


def wordwrap(num, words):
    afterwrap = []
    words = words.split('\n')
    for i in range(len(words)):
        if len(words[i]) > 19:
            s = textwrap.wrap(words[i], width=20)
            afterwrap.extend(s)
        else:
            afterwrap.append(words[i])
    lines = len(afterwrap)+1
    afterwrap = '\n'.join(afterwrap)
    imgwords = num+'\n'+afterwrap
    return lines, imgwords


def picture(lines, words2):
    width = 40*20+5*2
    height = 44*lines+5*2
    if height < width:
        height = width
    image = Image.new(mode='RGB', size=(width, height), color=0)

    # drawable image
    ImDr = ImageDraw.Draw(image)

    # 使用中文字型，就能顯示中文
    # 同時決定字的大小

    font = ImageFont.truetype(
        # font='../static/fonts/msjhbd.ttc', size=40)
        font='/myblog/msjhbd.ttc', size=40)

    ImDr2 = ImageDraw.Draw(image)
    ImDr2.text(xy=(5, 0), text=words2, font=font,
               fill='green', spacing=0)
    return image


if __name__ == '__main__':
    pid = input()
    ptext = input()
    line, word = wordwrap(pid, ptext)
    img = picture(line, word)
    img.save('image.png', 'png')
