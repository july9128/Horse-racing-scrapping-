# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 22:30:28 2019
Horse racing crawling : Thanks to the 마사회

@author: Yeonju Baik , UW Madison- Economics Phd

"""


import numpy as np
import os
import pandas as pd
from bs4 import BeautifulSoup
import urllib.request
import requests
import json

os.chdir("C:/Users/july9/Dropbox/Research Idea/RA/Paola/race/korea_scrapping")    

client_key='QCjxACoLlu8YvghK2mPkHkHTVQOy6Ln585hmUyvpSJSqkVGnxRtwrPBo7cE4H3qm8W9VUxzgJEQ2lINDcotH8w%3D%3D'  




def ownerinfo():
    Total=pd.DataFrame()
    for i_page in range(1,50):
            
        ind=str(i_page)
        url='http://apis.data.go.kr/B551015/API14/horseOwnerInfo?ServiceKey='+client_key+'&numOfRows=10&pageNo='+ind
        resp=requests.get(url)
        resp.encoding=None
        html=resp.text
        
        soup=BeautifulSoup(html,'html.parser')
        
        game_St=soup.find_all('meet')
        calc=soup.find_all('cancledhorses')
        owName=soup.find_all('owname')
        ow_num=soup.find_all('owno')
        tot_horse=soup.find_all('tothorses')
        own_horses=soup.find_all('ownerhorses')
        date_from=soup.find_all('stdate')
        first_1yr=soup.find_all('ord1cnty')
        second_1yr=soup.find_all('ord2cnty')
        third_1yr=soup.find_all('ord3cnty')
        total_game_1yr=soup.find_all('rccnty')
        total_earn=soup.find_all('chaksunt')
        total_game=soup.find_all('rccntt')
        total_earn_1yr=soup.find_all('chaksuny')
        first_tot=soup.find_all('ord1cntt')
        second_tot=soup.find_all('ord2cntt')
        third_tot=soup.find_all('ord3cntt')
        
        game_St = [x.text for x in game_St]
        calc = [x.text for x in calc]
        owName = [x.text for x in owName]
        ow_num = [x.text for x in ow_num]
        tot_horse = [x.text for x in tot_horse]
        own_horses = [x.text for x in own_horses]
        date_from = [x.text for x in date_from]
        
        first_1yr = [x.text for x in first_1yr]
        second_1yr= [x.text for x in second_1yr]
        third_1yr= [x.text for x in third_1yr]
        total_game_1yr= [x.text for x in total_game_1yr]
        total_earn= [x.text for x in total_earn]
        total_game = [x.text for x in total_game]
        total_earn_1yr= [x.text for x in total_earn_1yr]
        first_tot= [x.text for x in first_tot]
        second_tot = [x.text for x in second_tot]
        third_tot= [x.text for x in third_tot]
        
        
        
        df=pd.DataFrame()
        df['game_St']=game_St
        df['owName']=owName
        df['tot_horse']=tot_horse
        df['own_horses']=own_horses
        df['ow_num']=ow_num
        df['calc']=calc
        df['date_from']=date_from
        df['first_1yr']=first_1yr
        df['second_1yr']=second_1yr
        df['third_1yr']=third_1yr
        
        df['total_game_1yr']=total_game_1yr
        df['total_earn']=total_earn
        df['total_game']=total_game
        df['total_earn_1yr']=total_earn_1yr
        df['first_tot']=first_tot
        df['second_tot']=second_tot
        df['third_tot']=third_tot
        
        Total=Total.append(df)
        
        
    Total.to_csv('my_csv.csv',mode='a',encoding='ms949')


###############################################################
################## scrapping game results


def game_result():
    
    Horse_inf =pd.DataFrame()
    
    for i_page in range(1,180):
            
        ind=str(i_page)
        url='http://apis.data.go.kr/B551015/API15/raceHorseResult?ServiceKey='+client_key+'&numOfRows=10&pageNo='+ind
        resp=requests.get(url)
        resp.encoding=None
        html=resp.text
        
        soup=BeautifulSoup(html,'html.parser')
        
        hor_name=soup.find_all('hrname')
        hor_num=soup.find_all('hrno')
        national=soup.find_all('name')
        sex=soup.find_all('sex')
        age=soup.find_all('age')
        debut=soup.find_all('debut')
        total_game=soup.find_all('rccntt')
        total_first=soup.find_all('ord1cntt')
        total_second=soup.find_all('ord2cntt')    
        win_rate=soup.find_all('winratet')
        total_game_1yr=soup.find_all('rccnty')
        winrate_1yr=soup.find_all('winratey')
        total_earn=soup.find_all('chaksunt')
        total_earn_1yr=soup.find_all('chaksuny')
        
        national = [x.text for x in national]
        hor_name = [x.text for x in hor_name]
        hor_num = [x.text for x in hor_num]
        sex = [x.text for x in sex]
        age = [x.text for x in age]
        debut = [x.text for x in debut]
        total_first= [x.text for x in total_first]
        total_second = [x.text for x in total_second]
        total_game = [x.text for x in total_game]
        win_rate = [x.text for x in win_rate]
        total_game_1yr= [x.text for x in total_game_1yr]
        winrate_1yr = [x.text for x in winrate_1yr]
        total_earn= [x.text for x in total_earn]
        total_earn_1yr= [x.text for x in total_earn_1yr]
        
        
        
        df=pd.DataFrame()
        df['national']=national
        df['hor_name']=hor_name
        df['hor_num']=hor_num
        df['sex']=sex
        df['age']=age
        df['debut']=debut
        df['total_first']=total_first
        df['total_second']=total_second
        df['total_game']=total_game
        df['win_rate']=win_rate
        df['total_game_1yr']=total_game_1yr
        df['total_earn']=total_earn
        df['total_earn_1yr']=total_earn_1yr
        
        Horse_inf = Horse_inf.append(df)
        
        
    Horse_inf.to_csv('horse_inf.csv',mode='a',encoding='ms949')
    

#########################################################################################
######################################################################################3333
#######Game record crawling

def game_record():

    
    df=pd.DataFrame()
    
    for i_page in range(1,600):
            
        ind=str(i_page)
        url='http://apis.data.go.kr/B551015/API4/raceResult?ServiceKey='+client_key+'&numOfRows=10&pageNo='+ind
        resp=requests.get(url)
        resp.encoding=None
        html=resp.text
        
        soup=BeautifulSoup(html,'lxml')
        
        for a in soup.find_all('item'):
          
            meet=a.find_all('meet')
            rcDate=a.find_all('rcdate')
            rcDay=a.find_all('rcday')
            rcDist=a.find_all('rcdist')
            rank=a.find_all('rank')
            prizeCond=a.find_all('prizecond')
            ageCond=a.find_all('agecond')
            weather=a.find_all('weather')
            track=a.find_all('track')    
            first_earn=a.find_all('chaksun1')
            secon_earn=a.find_all('chaksun2')
            third_earn=a.find_all('chaksun3')
            fourth_earn=a.find_all('chaksun4')
            fifth_earn_1yr=a.find_all('chaksun5')    
            hor_name=a.find_all('hrname')
            hor_num=a.find_all('hrno')
            rating=a.find_all('rating')
            jkName=a.find_all('jkname')    
            jkNo=a.find_all('jkno')
            trName=a.find_all('trname')
            trNo=a.find_all('trno')
            owName=a.find_all('owname')    
            owNo=a.find_all('owno')
            order=a.find_all('ord')
            wgHr=a.find_all('wghr')    
            winodds=a.find_all('winodds')
            plcodds=a.find_all('plcodds')
    
            meet = [x.text for x in meet]
            rcDate = [x.text for x in rcDate]
            rcDay= [x.text for x in rcDay]
            rcDist= [x.text for x in rcDist]
            rank= [x.text for x in rank]
            prizeCond = [x.text for x in prizeCond]
            ageCond= [x.text for x in ageCond]
            weather = [x.text for x in weather]
            track = [x.text for x in track]
            secon_earn = [x.text for x in secon_earn]
            first_earn= [x.text for x in first_earn]
            third_earn = [x.text for x in third_earn]
            fourth_earn= [x.text for x in fourth_earn]
            fifth_earn_1yr= [x.text for x in fifth_earn_1yr]    
            hor_name = [x.text for x in hor_name]
            hor_num = [x.text for x in hor_num]
            rating= [x.text for x in rating]
            jkName = [x.text for x in jkName]
            jkNo= [x.text for x in jkNo]
            trName= [x.text for x in trName]    
            trNo = [x.text for x in trNo]
            owName = [x.text for x in owName]
            owNo= [x.text for x in owNo]
            order = [x.text for x in order]
            wgHr= [x.text for x in wgHr]
            winodds= [x.text for x in winodds]
            plcodds= [x.text for x in plcodds]
       
            ss=[secon_earn,first_earn,third_earn,fourth_earn,fifth_earn_1yr,hor_name,hor_num,rating]
            varlist=[meet,rcDate,rcDay,rcDist,rank,prizeCond,ageCond,weather,track]
            varlist.extend(ss)
            varlist.extend([jkName,jkNo,trName,trNo,owName,owNo,order,wgHr,winodds,plcodds])
            dd=pd.DataFrame(varlist).T
            df=pd.concat([df,dd])
     
    
    df.columns = ['meet','rcDate','rcDay','rcDist','rank','prizeCond','ageCond','weather','track','secon_earn','first_earn','third_earn','fourth_earn','fifth_earn_1yr','hor_name','hor_num','rating','jkName','jkNo','trName','trNo','owName','owNo','order','wgHr','winodds','plcodds']
    df.to_csv('Game_result.csv',mode='a',encoding='ms949')



#########################################################################################
######################################################################################3333
#######Betting Revenue

def betting_revenue():
    
    df=pd.DataFrame()
    
    for i_page in range(1,50):
            
        ind=str(i_page)
        url='http://apis.data.go.kr/B551015/API38/ticketSalesRanking?ServiceKey='+client_key+'&numOfRows=10&pageNo='+ind
        resp=requests.get(url)
        resp.encoding=None
        html=resp.text
        soup=BeautifulSoup(html,'lxml')
        
        for a in soup.find_all('item'):
            meet=a.find_all('meet')
            rcDate=a.find_all('rcdate')
            rcno=a.find_all('rcno') 
            winAmt=a.find_all('winamt')
            plcAmt=a.find_all('plcamt')
            qnlAmt=a.find_all('qnlamt')
            exaAmt=a.find_all('exaamt')
            qplAmt=a.find_all('qplamt')
            tlaAmt=a.find_all('tlaamt')    
            triAmt=a.find_all('triamt')
            totalAmt=a.find_all('totalamt')
            
            meet = [x.text for x in meet]
            rcDate = [x.text for x in rcDate]
            rcno= [x.text for x in rcno]
            winAmt= [x.text for x in winAmt]
            plcAmt= [x.text for x in plcAmt]
            qnlAmt = [x.text for x in qnlAmt]
            exaAmt= [x.text for x in exaAmt]
            qplAmt = [x.text for x in qplAmt]
            tlaAmt= [x.text for x in tlaAmt]
            triAmt = [x.text for x in triAmt]
            totalAmt= [x.text for x in totalAmt]
       
            varlist=[meet,rcDate,rcno,winAmt,plcAmt,qnlAmt,exaAmt,qplAmt,tlaAmt,triAmt,totalAmt]
            dd=pd.DataFrame(varlist).T
            df=pd.concat([df,dd])
     
    
    df.columns = ['meet','rcDate','rcno','winAmt','plcAmt','qnlAmt','exaAmt','qplAmt','tlaAmt','triAmt','totalAmt']
    df.to_csv('betting_Revenue.csv',mode='a',encoding='ms949')


#########################################################################################
######################################################################################3333
#######Jockey information

def jockey_info():
    
    df=pd.DataFrame()
    
    for i_page in range(1,58):
            
        ind=str(i_page)
        url='http://apis.data.go.kr/B551015/API12/jockeyInfo?ServiceKey='+client_key+'&numOfRows=10&pageNo='+ind
        resp=requests.get(url)
        resp.encoding=None
        html=resp.text
        soup=BeautifulSoup(html,'lxml')
        
        for a in soup.find_all('item'):
            meet=a.find_all('meet')
            jkName=a.find_all('jkname')
            jkNo=a.find_all('jkno') 
            part=a.find_all('part')
            age=a.find_all('age')
            debut=a.find_all('debut')
            spDate=a.find_all('spdate')
            total_game=a.find_all('rccntt')
            
            first=a.find_all('ord1cntt')    
            second=a.find_all('ord2cntt')
            third=a.find_all('ord3cntt')
            total_game_1yr=a.find_all('rccnty')
            first_1yr=a.find_all('ord1cnty')    
            second_1yr=a.find_all('ord2cnty')
            third_1yr=a.find_all('ord3cnty')
            
            meet = [x.text for x in meet]
            jkName = [x.text for x in jkName]
            jkNo= [x.text for x in jkNo]
            part= [x.text for x in part]
            age= [x.text for x in age]
            debut = [x.text for x in debut]
            spDate= [x.text for x in spDate]
            total_game = [x.text for x in total_game]
            first= [x.text for x in first]
            second = [x.text for x in second]
            third= [x.text for x in third]
       
            total_game_1yr = [x.text for x in total_game_1yr]
            first_1yr= [x.text for x in first_1yr]
            second_1yr= [x.text for x in second_1yr]
            third_1yr= [x.text for x in third_1yr]
            
            varlist=[meet,jkName,jkNo,part,age,debut,spDate,total_game,first,second,third,total_game_1yr,first_1yr,second_1yr,third_1yr]
            dd=pd.DataFrame(varlist).T
            df=pd.concat([df,dd])
     
    
    df.columns = ['meet','rcDate','rcno','winAmt','plcAmt','qnlAmt','exaAmt','qplAmt','tlaAmt','triAmt','totalAmt']
    df.to_csv('Jockey_info.csv',mode='a',encoding='ms949')




################################################
######################################################################################3333
#######trainer information

def trainer_info():
    
    df=pd.DataFrame()
    
    for i_page in range(1,58):
            
        ind=str(i_page)
        url='http://apis.data.go.kr/B551015/API19/trainerInfo?ServiceKey='+client_key+'&numOfRows=10&pageNo='+ind
        resp=requests.get(url)
        resp.encoding=None
        html=resp.text
        soup=BeautifulSoup(html,'lxml')
        
        for a in soup.find_all('item'):
            meet=a.find_all('meet')
            trName=a.find_all('trname')
            trNo=a.find_all('trno') 
            part=a.find_all('part')
            age=a.find_all('age')
            stDate=a.find_all('stdate')
            total_game=a.find_all('rccntt')
            first=a.find_all('ord1cntt')    
            second=a.find_all('ord2cntt')
            third=a.find_all('ord3cntt')
            winRateT=a.find_all('winratet')    
            qnlRateT=a.find_all('qnlratet')
            plcRateT=a.find_all('plcratet')
            total_game_1yr=a.find_all('rccnty')
            first_1yr=a.find_all('ord1cnty')    
            second_1yr=a.find_all('ord2cnty')
            third_1yr=a.find_all('ord3cnty')
            winRate_1yr=a.find_all('winratey')    
            qnlRate_1yr=a.find_all('qnlratey')
            plcRate_1yr=a.find_all('plcratey')
            
            meet = [x.text for x in meet]
            trName= [x.text for x in trName]
            trNo= [x.text for x in trNo]
            part= [x.text for x in part]
            age= [x.text for x in age]
            stDate= [x.text for x in stDate]
            total_game = [x.text for x in total_game]
            first= [x.text for x in first]
            second = [x.text for x in second]
            third= [x.text for x in third]
       
            winRateT= [x.text for x in winRateT]
            qnlRateT = [x.text for x in qnlRateT]
            plcRateT= [x.text for x in plcRateT]
            
            total_game_1yr = [x.text for x in total_game_1yr]
            first_1yr= [x.text for x in first_1yr]
            second_1yr= [x.text for x in second_1yr]
            third_1yr= [x.text for x in third_1yr]
            
            winRate_1yr= [x.text for x in winRate_1yr]
            qnlRate_1yr = [x.text for x in qnlRate_1yr]
            plcRate_1yr= [x.text for x in plcRate_1yr]
            varlist=[meet,trName,trNo,part,age,stDate,total_game,first,second,third,winRateT,qnlRateT,plcRateT,total_game_1yr,first_1yr,second_1yr,third_1yr,winRate_1yr,qnlRate_1yr,plcRate_1yr]
            dd=pd.DataFrame(varlist).T
            df=pd.concat([df,dd])
     
    
    df.columns = ['meet','trName','trNo','part','age','stDate','total_game','first','second','third','winRateT','qnlRateT','plcRateT','total_game_1yr','first_1yr','second_1yr','third_1yr','winRate_1yr','qnlRate_1yr','plcRate_1yr']
    df.to_excel('trainer_info.xlsx', sheet_name='sheet1')


###########################
######################################################################################3333
#######Betting information 

def betting_info():
    
    df=pd.DataFrame()
    
    for i_page in range(1,411):
            
        ind=str(i_page)
        url='http://apis.data.go.kr/B551015/API179/salesAndDividendRate?ServiceKey='+client_key+'&numOfRows=10&pageNo='+ind
        resp=requests.get(url)
        resp.encoding=None
        html=resp.text
        soup=BeautifulSoup(html,'lxml')
        
        for a in soup.find_all('item'):
            meet=a.find_all('meet')
            rcdate=a.find_all('rcDate')
            rcNo=a.find_all('rcNo') 
            pool=a.find_all('pool')
            revenue=a.find_all('amt')
            odds=a.find_all('odds')
            
            meet = [x.text for x in meet]
            rcdate= [x.text for x in rcdate]
            rcNo= [x.text for x in rcNo]
            pool= [x.text for x in pool]
            revenue= [x.text for x in revenue]
            odds= [x.text for x in odds]
       
            varlist=[meet,rcdate,rcNo,pool,revenue,odds]
            dd=pd.DataFrame(varlist).T
            df=pd.concat([df,dd])
     
    
    df.columns = ['meet','rcdate','rcNo','pool','revenue','odds']
    df.to_excel('betting_info.xlsx', sheet_name='sheet1')


