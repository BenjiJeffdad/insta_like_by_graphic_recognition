"""
Author : Jeonghoon Lee
Last modification: 2022.1.11.
whitefang79@naver.com
https://github.com/Benjijeffdad/insta_like_by_graphic_recognition
"""

from selenium import webdriver
import pywinmacro as pw
import pyautogui as pg
import time

class LikeBoT:
    def __init__(self, like_button):
        self.like_button = like_button
        self.tag_url = "http://instagram.com/explore/tags"
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe")

    def login(self, id, ps):
        #로그인 페이지 이동
        self.driver.get("https://www.instagram.com/accounts/login")

        # 로그인
        time.sleep(5)
        pw.key_press_once("tab")
        pw.typing(id)
        pw.key_press_once("tab")
        pw.typing(ps)
        pw.key_press_once("enter")
        time.sleep(5)

    def kill(self):
        self.driver.quit()

    def refresh(self):
        pw.key_press_once("f5")

    def search_tag(self, tag):
        self.driver.get(self.tag_url + tag)
        time.sleep(5)

    def select_picture(self):
        # 탭 키를 20번 정도 누르기 -> 최근게시물로 넘어가기 위함
        for i in range(20):
            pw.key_press_once("tab")

        # 엔터키 누르기
        pw.key_press_once("enter")

    # 좋아요 누르는 함수
    def press_like(self):
        like_location = pg.locateCenterOnScreen(self.like_button)
        if like_location:
            pw.click(like_location)

    def insta_jungdok(self, tag, click_num):
        self.search_tag(tag)
        self.select_picture()

         # for 문 돌면서 좋아요 누르기
        for i in range(click_num):
            self.press_like()
            time.sleep(3)
            pw.key_press_once("right_arrow")
            time.sleep(3)