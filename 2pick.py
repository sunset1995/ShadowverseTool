import os
import cv2
import time
import pyautogui
import numpy as np
import PIL.Image as Image

import util

# Create sceen reader (using another thread)
screenshotter = util.ScreenShotter()



''' Main program '''
def go_arena():
    arena_temp = util.read_template('templates', '2pick', 'arena.png')
    arena_in_temp = util.read_template('templates', '2pick', 'arena_in.png')
    while not util.check_existed(screenshotter, arena_in_temp):
        util.find_and_click(screenshotter, arena_temp)

def go_2pick():
    twopick_temp = util.read_template('templates', '2pick', '2pick.png')
    entrace_temp = util.read_template('templates', '2pick', 'entrance.png')
    while not util.check_existed(screenshotter, entrace_temp):
        util.find_and_click(screenshotter, twopick_temp)

def go_entrance():
    entrace_temp = util.read_template('templates', '2pick', 'entrance.png')
    useticket_temp = util.read_template('templates', '2pick', 'use_ticket.png')
    while not util.check_existed(screenshotter, useticket_temp):
        util.find_and_click(screenshotter, entrace_temp)

def go_useticket():
    useticket_temp = util.read_template('templates', '2pick', 'use_ticket.png')
    getin_temp = util.read_template('templates', '2pick', 'get_in.png')
    while not util.check_existed(screenshotter, getin_temp):
        util.find_and_click(screenshotter, useticket_temp)

def go_getin():
    getin_temp = util.read_template('templates', '2pick', 'get_in.png')
    character_temp = util.read_template('templates', '2pick', 'chose_character.png')
    while not util.check_existed(screenshotter, character_temp):
        util.find_and_click(screenshotter, getin_temp)

def go_character():
    character_temp = util.read_template('templates', '2pick', 'chose_character.png')
    chose_temp = util.read_template('templates', '2pick', 'chose.png')
    while not util.check_existed(screenshotter, chose_temp):
        util.find_and_click(screenshotter, character_temp, rel_h=1.5)
        time.sleep(1)

def go_chose():
    chose_temp = util.read_template('templates', '2pick', 'chose.png')
    pickcard_temp = util.read_template('templates', '2pick', 'pick_card.png')
    while not util.check_existed(screenshotter, pickcard_temp):
        util.find_and_click(screenshotter, chose_temp)

def go_pickcard():
    pickcard_temp = util.read_template('templates', '2pick', 'pick_card.png')
    giveup_temp =  util.read_template('templates', '2pick', 'giveup.png')
    while not util.check_existed(screenshotter, giveup_temp):
        util.find_and_click(screenshotter, pickcard_temp)

def go_giveup():
    giveup_temp =  util.read_template('templates', '2pick', 'giveup.png')
    giveup2_temp = util.read_template('templates', '2pick', 'giveup2.png')
    while not util.check_existed(screenshotter, giveup2_temp):
        util.find_and_click(screenshotter, giveup_temp)

def go_giveup2():
    giveup2_temp = util.read_template('templates', '2pick', 'giveup2.png')
    goback_temp =  util.read_template('templates', '2pick', 'goback.png')
    while not util.check_existed(screenshotter, goback_temp):
        util.find_and_click(screenshotter, giveup2_temp)

def go_goback():
    goback_temp =  util.read_template('templates', '2pick', 'goback.png')
    arena_temp = util.read_template('templates', '2pick', 'arena.png')
    while not util.check_existed(screenshotter, arena_temp):
        util.find_and_click(screenshotter, goback_temp)

for i in range(20):
    go_arena()
    go_2pick()
    go_entrance()
    go_useticket()
    go_getin()
    go_character()
    go_chose()
    go_pickcard()
    go_giveup()
    go_giveup2()
    go_goback()
