from requests import get, post, Session
import json
from bs4 import BeautifulSoup
import json
baseURL = 'https://www.bubt.edu.bd'


def getEEECourse(programURL):
    finalData = {'data': list()}
    try:
        programHTML = get(baseURL+programURL).text
        titles = BeautifulSoup(str(programHTML), 'html.parser').find_all('h4', class_='panel-title')
        bodys = BeautifulSoup(str(programHTML), 'html.parser').find_all('div', class_='panel-body')
        with open('eee.html', 'w', encoding='utf-8') as f:
            f.write(str(programHTML))
        for data in range(0,87):
            titleData = titles[data].a.text
            bodyData = bodys[data].find_all('p')

            for body in bodyData:
                if "Credits" in body.text:
                    credits = body.text
                if "Prerequisite" in body.text:
                    prerequisite = body.text
            localData = {
                    'course_code': titleData.split(" (")[0],
                    'course_title': titleData.split(" (")[1].replace(')',''),
                    'theory_credit': '',
                    'lab_credit': '',
                    'total_credit': credits.replace('Credits: ',''),
                    'prerequisit': prerequisite.replace('Prerequisite: ','')
            }
            finalData['data'].append(localData)
        print(json.dumps(finalData))
    except Exception as ex:
        finalData = {'status': 'failed', 'reason': str(ex)} 
    return finalData

getEEECourse("/department/curriculam/64")