
import requests
from bs4 import BeautifulSoup 
import csv
import datetime


 

def main(date):
    
    page= requests.get(f'https://www.yallakora.com/match-center?date={date}' )
    src=page.content
    soup = BeautifulSoup(src, 'lxml')
    championship = soup.find_all("div",{'class':'matchCard'})
    match_details=[]
    
    def get_match_info(championship):
        championship_name= championship.contents[1].find('h2').text.strip()
        
                
        # Convert the user input to a datetime object
        user_date = datetime.datetime.strptime(date, "%m/%d/%Y").date()

        # Get the current actual date
        current_date = datetime.date.today()
        
        if user_date >= current_date:
            all_matches= championship.contents[3].find_all("li",{'class':'item future'})
        else:
            all_matches= championship.contents[3].find_all("li",{'class':'item finish'})
    

        for match in all_matches:           
            match_info= match.find('a').find('div').find('div',{'class':'teamCntnr'}).find('div',{'class':'teamsData'})
            match_result=match_info.find('div',{'class':'MResult'})
            
            match_scor = match_result.find_all('span',{'class':'score'})
            score= f'{match_scor[0].text.strip()} |-| {match_scor[1].text.strip()}'
            
            match_time = match_result.find('span',{'class':'time'}).text.strip()
            
            
            
            match_teams= match_info.find_all('div', {'class':'teams'})
            teamA= match_teams[0].find('p').text.strip()
            teamB= match_teams[1].find('p').text.strip()
            
#            match_details.append({'نوع البطولة': championship_name,'الفريق الاول':teamA,'الفريق الثاني':teamB,'الميعاد':match_time,'النتيجة': str(score)})
            match_details.append({'1': championship_name,'2':teamA,'3':teamB,'4':match_time,'5': str(score)})
            
    for champ in championship:
        get_match_info(champ)
    
    return   match_details
    
    




#exemple of input: 7/30/2023




