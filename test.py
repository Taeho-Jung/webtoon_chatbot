# -*- coding: utf-8 -*-
import json
import os
import re
import urllib.request
import pandas as pd
from bs4 import BeautifulSoup
from slackclient import SlackClient
from flask import Flask, request, make_response, render_template

app = Flask(__name__)

slack_token = "xoxb-508930171334-506934298177-RZBRghnMOtynJEJf9xqagibm"
slack_client_id = "508930171334.508938367910"
slack_client_secret = "7ab8bbde5098d5648070cfb373389734"
slack_verification = "4D6ePtQU9iBwlM0VViBIQU0Q"
sc = SlackClient(slack_token)


# 크롤링 함수 구현하기
def _crawl_naver_keywords(text):
    #url = re.search(r'(https?://music.bugs.co.kr)', text.split('|')[0]).group(0)
    print(text)
    input = text.split(" ")
    text = input[1]
    input_word_list = []
    if text == "추천":
        input_word_list.append(input[2])
        input_word_list.append(input[3])
        input_word_list.append(input[4])
        input_word_list.append(input[5])
        input_word_list.append(input[6])


    keywords = []
    tmp = []
    url = ""
    if text == "추천":
        word_list = [["전투", "싸움", "폭탄", "무술", "총", "추격전", "성룡", "스턴트", "자동차", "오토바이", "싸움", "전쟁", "군인", "장비", "폭탄", "총", "칼", "운동", "피", "배신", "싸움", "맞짱", "조폭", "주인공", "찐따", "정의", "돈", "영화", "보수", "게임"],
                ["사랑", "로맨스", "고등학생", "학창시절", "크리스마스", "발렌타인데이", "약속", "마음", "짝사랑", "달달", "사랑", "친구", "연인", "연애", "관심", "애정", "썸", "데이트", "벚꽃", "사랑", "믿음", "이별", "양다리", "술", "돈", "꽃", "우정", "연락", "결혼", "마음"],
                ["시트콤", "웃음", "마음의소리", "조석", "하이킥", "가벼움", "짧음", "스토리", "병맛", "오덕", "우정", "싸움", "생각", "병맛", "취향", "덕후", "덕후", "스토리", "생각", "반전", "이야기", "스토리", "취지"],
                ["길", "나무", "학교", "회사", "공부", "음식", "학교", "친구", "학원", "연애", "공부", "놀이", "여행", "일상생활", "돈", "우정", "태양", "밤", "일기", "커피", "핸드폰", "일기"],
                ["웃음", "즐거움", "심심함", "미소", "병맛", "코미디", "웃찾사", "개그콘서트", "장동민", "박명수", "웃음", "개그콘서트", "개그콘서트", "분장", "캐릭터", "스마일", "기분전환", "개그", "개그맨", "웃음", "웃김", "코드", "병맛", "개그", "코믹", "일상", "부담"],
                ["마법", "드래곤", "오크", "전사", "레벨", "엘프", "지팡이", "검", "망토", "로브", "마법사", "조선", "역사", "시간여행", "타임슬립", "사극", "마법사", "마법", "지상세계", "천상세계", "천사", "악마", "마법", "해리포터", "반지", "지팡이", "뱀파이어", "늑대", "허구", "허구", "이야기"],
                ["칼", "추격", "번개", "밤", "공포", "긴장", "살인", "살인범", "범죄", "폭탄", "정치", "사시미", "귀신", "유령", "공포", "비평", "가위", "소리", "어두움", "음침함", "악마", "음모", "죽음", "공포영화", "공포", "링", "스크림", "비명", "좀비", "새벽", "손톱", "귀신", "범죄", "마약", "싸움", "공포", "유령", "살인", "잔인"]]

        act_num = len(word_list[0])
        sj_num = len(word_list[1])
        ep_num= len(word_list[2])
        day_num = len(word_list[3])
        gag_num = len(word_list[4])
        fantasy_num = len(word_list[5])
        thiller_num = len(word_list[6])


        all_num = act_num + sj_num + ep_num + day_num + gag_num + fantasy_num + thiller_num



        p = []
        p1 = 1
        for i in range(7):
           for j in range(5):
               p1 *= (word_list[i].count(input_word_list[j]) + 1 / (len(word_list[i]) + all_num))

           p.append(p1)
           p1 = 1

        max = -1
        index = -1
        for i in range(7):
           if p[i] > max:
               max = p[i]
               index = i

        if index == 0:
           print("액션")
           text ="액션"
           url ="https://comic.naver.com/webtoon/genre.nhn?genre=action"
        elif index == 1:
           print("순정")
           text ="순정"
           url ="https://comic.naver.com/webtoon/genre.nhn?genre=pure"
        elif index == 2:
           print("에피소드")
           text ="에피소드"
           url ="https://comic.naver.com/webtoon/genre.nhn?genre=episode"
        elif index == 3:
           print("일상")
           text ="일상"
           url ="https://comic.naver.com/webtoon/genre.nhn?genre=daily"
        elif index == 4:
           print("개그")
           text ="개그"
           url ="https://comic.naver.com/webtoon/genre.nhn?genre=comic"
        elif index == 5:
           print("판타지")
           text ="판타지"
           url ="https://comic.naver.com/webtoon/genre.nhn?genre=fantasy"
        elif index == 6:
           print("스릴러")
           text ="스릴러"
           url ="https://comic.naver.com/webtoon/genre.nhn?genre=thrill"

    # 여기에 함수를 구현해봅시다.
    # url = re.search(r'(https?://\S+)', text.split('|')[0]).group(0)
    elif text == '에피소드':
        url ="https://comic.naver.com/webtoon/genre.nhn?genre=episode"
    elif text == '스릴러':
        url ="https://comic.naver.com/webtoon/genre.nhn?genre=thrill"
    elif text == '일상':
        url ="https://comic.naver.com/webtoon/genre.nhn?genre=daily"
    elif text == '개그':
        url ="https://comic.naver.com/webtoon/genre.nhn?genre=comic"
    elif text == '순정':
        url ="https://comic.naver.com/webtoon/genre.nhn?genre=pure"
    elif text == '판타지':
        url ="https://comic.naver.com/webtoon/genre.nhn?genre=fantasy"
    elif text == '액션':
        url ="https://comic.naver.com/webtoon/genre.nhn?genre=action"
    elif text == '옴니버스':
        url ="https://comic.naver.com/webtoon/genre.nhn?genre=omnibus"

    elif (text == '월요일' or text == '화요일' or text == '수요일' or text == '목요일' or text == '금요일' or text == '토요일' or text == '일요일'):
        url = "https://comic.naver.com/webtoon/weekday.nhn"


    if (text == '에피소드' or text == '스릴러' or text == '일상' or text == '개그' or text == '순정' or text == '판타지' or text == '액션' or text == '옴니버스'):
        keywords = []
        # url ="https://comic.naver.com/webtoon/genre.nhn?genre=episode"
        req = urllib.request.Request(url)
        sourcecode = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(sourcecode, "html.parser")
        catoon_list = soup.find("div", class_="list_area")
        keywords.append("\t★" + text + " 웹툰목록★ \n")
        for i, keyword in enumerate(catoon_list.find_all("dl")):
            if i < 50:
                ct_name = keyword.find("dt").get_text()
                ct_auth = keyword.find("dd", class_="desc").find("a").get_text()
                ct_star = keyword.find("div", class_="rating_type").find("strong").get_text()
                keywords.append(str(i+1) + ". " +  ct_name + " (" + ct_star + ") "+ "- " + ct_auth +"\n")

        return u'\n'.join(keywords)
    elif (text == '월요일' or text == '화요일' or text == '수요일' or text == '목요일' or text == '금요일' or text == '토요일' or text == '일요일'):
        url = "https://comic.naver.com/webtoon/weekday.nhn"
        req = urllib.request.Request(url)
        sourcecode = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(sourcecode, "html.parser")
        tmp2 = []
        for i, keyword in enumerate(soup.find_all("a", class_="title")):
            if text == '월요일':
                if i < 32:
                    tmp2.append(keyword.get_text().strip())
            elif text == '화요일':
                if (32 <= i and i < 64):
                    tmp2.append(keyword.get_text().strip())
            elif text == '수요일':
                if (64 <= i and i < 97):
                    tmp2.append(keyword.get_text().strip())
            elif text == '목요일':
                if (97 <= i and i < 133):
                    tmp2.append(keyword.get_text().strip())
            elif text == '금요일':
                if (133 <= i and i < 163):
                    tmp2.append(keyword.get_text().strip())
            elif text == '토요일':
                if (163 <= i and i < 193):
                    tmp2.append(keyword.get_text().strip())
            elif text == '일요일':
                if (193 <= i and i < 225):
                    tmp2.append(keyword.get_text().strip())
        keywords.append(text + '웹툰 조회순 Ranking')
        for i in range(len(tmp2)):
            keywords.append(str(i+1)+'위 : '+tmp2[i]+"\n" )
        return u'\n'.join(keywords)


# 이벤트 핸들하는 함수
def _event_handler(event_type, slack_event):
    print(slack_event["event"])

    if event_type == "app_mention":
        channel = slack_event["event"]["channel"]
        text = slack_event["event"]["text"]

        keywords = _crawl_naver_keywords(text)
        sc.api_call(
            "chat.postMessage",
            channel=channel,
            text=keywords
        )

        return make_response("App mention message has been sent", 200,)

    # ============= Event Type Not Found! ============= #
    # If the event_type does not have a handler
    message = "You have not added an event handler for the %s" % event_type
    # Return a helpful error message
    return make_response(message, 200, {"X-Slack-No-Retry": 1})

@app.route("/listening", methods=["GET", "POST"])
def hears():
    slack_event = json.loads(request.data)

    if "challenge" in slack_event:
        return make_response(slack_event["challenge"], 200, {"content_type":
                                                             "application/json"
                                                            })

    if slack_verification != slack_event.get("token"):
        message = "Invalid Slack verification token: %s" % (slack_event["token"])
        make_response(message, 403, {"X-Slack-No-Retry": 1})

    if "event" in slack_event:
        event_type = slack_event["event"]["type"]
        return _event_handler(event_type, slack_event)

    # If our bot hears things that are not events we've subscribed to,
    # send a quirky but helpful error response
    return make_response("[NO EVENT IN SLACK REQUEST] These are not the droids\
                         you're looking for.", 404, {"X-Slack-No-Retry": 1})

@app.route("/", methods=["GET"])
def index():
    return "<h1>Server is ready.</h1>"

if __name__ == '__main__':
    app.run('127.0.0.1', port=5000)
