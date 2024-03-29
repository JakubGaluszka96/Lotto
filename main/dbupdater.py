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
from main.models import LottoDraw

class SeleniumDbUpdater():

    last_id = int

    def update(self):
        PATH = "/usr/bin/chromedriver"
        s=Service(PATH)
        driver=webdriver.Chrome(service=s)
        driver.get("https://www.lotto.pl/lotto/wyniki-i-wygrane")
        self.last_id = driver.find_element(By.CLASS_NAME,"result-item__number").get_attribute("innerHTML").replace(" ", "").strip()
        if len(LottoDraw.objects.all()) != 0:
            last_id_from_db = LottoDraw.objects.all().order_by("-id")[0].id
        else:
            last_id_from_db = 0
        if last_id_from_db == self.last_id:
            return print("DB up to date")
        if last_id_from_db == 0:
            url = "https://www.lotto.pl/api/lotteries/draw-results/by-number-per-game?gameType=Lotto&drawSystemId="+self.last_id+"&index=1&size="+self.last_id+"&sort=drawSystemId&order=DESC"
        else:
            size = str(int(self.last_id) - last_id_from_db)
            url = "https://www.lotto.pl/api/lotteries/draw-results/by-number-per-game?gameType=Lotto&drawSystemId="+self.last_id+"&index=1&size="+size+"&sort=drawSystemId&order=DESC"
        driver.get(url)
        result = driver.find_element(By.TAG_NAME,"pre").get_attribute("innerHTML")
        driver.close()
        draws_json = json.loads(result)
        for draw in draws_json["items"]:
            id = draw["drawSystemId"]
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
                        mod.typing_set.create(number=number, is_plus=False)
                if result["gameType"] == "LottoPlus":
                    plus_numbers = result["resultsJson"]
                    for number in plus_numbers:
                        mod.typing_set.create(number=number, is_plus=True)          
            mod.save()
        return  
       
    def __str__(self):
        return self

    

                 
            
                



    
