from os import name
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
from selenium.webdriver.common.action_chains import ActionChains
import json
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from main.models import LottoDraw, Typing

class SeleniumDbUpdater():

    lastId = int

    def Update(self):
        PATH = "/usr/bin/chromedriver"
        s=Service(PATH)
        driver=webdriver.Chrome(service=s)
        driver.get("https://www.lotto.pl/lotto/wyniki-i-wygrane")
        self.lastId = driver.find_element(By.CLASS_NAME,"result-item__number").get_attribute("innerHTML").replace(" ", "").strip()
        LastIDfromDB = LottoDraw.objects.all().order_by("-id")[0].id
        if LastIDfromDB == self.lastId:
            return print("DB up to date")
        url = "https://www.lotto.pl/api/lotteries/draw-results/by-number-per-game?gameType=Lotto&drawSystemId="+self.lastId+"&index=1&size="+self.lastId+"&sort=drawSystemId&order=DESC"
        driver.get(url)
        result = driver.find_element(By.TAG_NAME,"pre").get_attribute("innerHTML")
        driver.close()
        drawsJson = json.loads(result)
        for draw in drawsJson["items"]:
            id = draw["drawSystemId"]
            print(id)
            drawdate = draw["drawDate"].split("T")[0].split("-")
            year = int(drawdate[0])
            month = int(drawdate[1])
            day = int(drawdate[2])
            date = datetime.date(year=year, month=month, day=day)
            mod = LottoDraw(id=id, date=date)
            for result in draw["results"]:
                if result["gameType"] == "Lotto":
                    numbers=result["resultsJson"]
                    for number in numbers:
                        mod.typing_set.create(number=number, isplus=False)
                else:
                    plusnumbers = result["resultsJson"]
                    for number in plusnumbers:
                        mod.typing_set.create(number=number, isplus=True)            
            mod.save()

        return     
    def __str__(self):
        return self

    

                 
            
                



    
