import requests
from bs4 import BeautifulSoup
import re
from Objects import *
from datetime import datetime
import pandas as pd
import numpy as np

def scrape_current_community_bets(link):
    link = link
    Spieltag = list(range(1,35))

    Dic_Spieltag_Datum = {1: '18.09.2020', 2: '25.09.2020', 3: '02.10.2020', 4: '17.10.2020', 5: '23.10.2020',
                          6: '30.10.2020', 7: '06.11.2020', 8: '21.11.2020', 9: '27.11.2020', 10: '04.12.2020',
                          11: '11.12.2020', 12: '15.12.2020', 13: '18.12.2020', 14: '02.01.2021', 15: '08.01.2021',
                          16: '15.01.2021', 17: '19.01.2021', 18: '22.01.2021', 19: '29.01.2021', 20: '05.02.2021',
                          21: '12.02.2021', 22: '19.02.2021', 23: '26.02.2021', 24: '05.03.2021', 25: '12.03.2021',
                          26: '19.03.2021', 27: '03.04.2021', 28: '09.04.2021', 29: '16.04.2021', 30: '20.04.2021',
                          31: '23.04.2021', 32: '07.05.2021', 33: '15.05.2021', 34: '22.05.2021'}

    matches = []
    last_matchday = 0
    for Tag in Spieltag:
        if  datetime.strptime(Dic_Spieltag_Datum[Tag],"%d.%m.%Y") < datetime.today():
            url = link + str(Tag)
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0"}
            page = requests.get(url, headers=headers)
            soup = BeautifulSoup(page.content, 'html.parser')
            soup.prettify()
            Relevanter_Teil = soup.find_all("div",{"class":"box"})[2]


            Ergebnisse = Relevanter_Teil.find("tbody")
            Spiele = Ergebnisse.find_all("tr")
            Spiele = Spiele[:9]
            for Spiel in Spiele:
                Match = Spiel.find_all("td")
                Mannschaften = Match[0].text
                Mannschaften = Mannschaften.split(":")
                Heimteam = Mannschaften[0].strip()
                Awayteam = Mannschaften[1].strip()
                HS= Match[1].text.strip()
                U = Match[2].text.strip()
                AS = Match[3].text.strip()
                Tipp = Match[4].text.strip()
                Tipp = Tipp.split(":")
                Tipp_Tore_H = Tipp[0]
                Tipp_Tore_A = Tipp[1]
                matches.append(match_object_predict(Heimteam,Awayteam,HS,U,AS,Tipp_Tore_H,Tipp_Tore_A, Tag, Dic_Spieltag_Datum[Tag]))
                last_matchday = Tag
        else:
            print("The {}. Matchday is on the {} .".format(Tag,Dic_Spieltag_Datum[Tag] ))

    df_crowd_prediction = pd.DataFrame([vars(f) for f in matches])
    df_crowd_prediction.loc[df_crowd_prediction["predict_goals_home"]> df_crowd_prediction["predict_goals_away"], "BR"]= "H"
    df_crowd_prediction.loc[df_crowd_prediction["predict_goals_home"]< df_crowd_prediction["predict_goals_away"], "BR"]= "A"
    df_crowd_prediction.loc[df_crowd_prediction["predict_goals_home"] == df_crowd_prediction["predict_goals_away"], "BR"]= "D"

    return df_crowd_prediction
