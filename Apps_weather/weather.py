import requests
from bs4 import BeautifulSoup
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QMainWindow, QVBoxLayout, QGroupBox
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from selenium import webdriver
import random
import datetime

from selenium.webdriver.common.by import By


def weather(params):
    user_agents_list = ["weather-pogoda", "russian-pogoda", "test_weater", "whygrad"]

    options = webdriver.ChromeOptions()
    options.add_argument(f"user-agent={random.choice(user_agents_list)}")
    driver = webdriver.Chrome(executable_path="/Apps_weather/chromedriver.exe", options=options)#Подкл. веб-драйвера.

    url = "https://yandex.ru/pogoda/"
    try:
        driver.get(url)
        with open("read_soup.html") as f1:
            f1.write(driver.page_source)
    except Exception:
        weather_now(params)
        weather_tomorrow(params)
        print(Exception)
    finally:
        driver.close()

def weather_now(params):
    with open("read_soup.html", encoding="UTF-8") as f2:
        text = ""
        for line in f2:
            text += line
    soup = BeautifulSoup(text, "lxml")
    grad_now = soup.find("span", class_="temp__value temp__value_with-unit").get_text() #Градусы.
    grad_north = soup.find("div", class_="fact__hour-temp").get_text() #Градусы ночью
    type_weather = soup.find("div", class_="link__condition day-anchor i-bem").get_text() #Тип погоды.
    time_now = soup.find("time", class_="time fact__time").get_text() #Текущее время.

    #Смена Текста в приложении.
    params.linedit_1.setText(f"{grad_now}")
    params.linedit_2.setText(f"{type_weather}")
    params.linedit_3.setText(f"{time_now}")
    params.linedit_4.setText(f"{grad_north}")

def weather_tomorrow(params):
    with open("read_soup.html", encoding="UTF-8") as f4:
        text = ""
        for line in f4:
            text += line
    soup = BeautifulSoup(text, "lxml")
    month = {"1": "января",
             "2": "февраля",
             "3": "марта",
             "4": "апреля",
             "5": "мая",
             "6": "июня",
             "7": "июля",
             "8": "августа",
             "9": "сентября",
             "10": "октября",
             "11": "ноября",
             "12": "декабря"}

    grad_dop_inf = soup.find("div", class_="forecast-briefly__days swiper-container swiper-container-horizontal")
    time = str(datetime.datetime.now()).split("-")
    time_number = int(time[1])

    for forecast in grad_dop_inf.find_all("li"):
        if f"{int(time[1])} {month[str(time_number)]}" in forecast.get_text():
            tomorrow = forecast
            break

    grad_day = tomorrow.find("span", class_="temp__value temp__value_with-unit").get_text()
    grad_north = tomorrow.find("div", class_="temp forecast-briefly__temp forecast-briefly__temp_night").get_text()
    type_weather = tomorrow.find("div", class_="forecast-briefly__condition").get_text()

    ###Добавление данных в приложение.
    params.linedit_5.setText(f"{grad_day}")
    params.linedit_6.setText(f"{type_weather}")
    params.linedit_7.setText(f"unknow")
    params.linedit_8.setText(f"{grad_north}")

