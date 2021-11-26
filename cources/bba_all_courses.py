from requests import get, post, Session
import json
from bs4 import BeautifulSoup
import json
baseURL = 'https://www.bubt.edu.bd'

def getBBACourse(programUrl):
    finalData = list()
    try:
        programHTML = get(baseURL+programUrl).text
        rows = BeautifulSoup(str(programHTML), 'html.parser').find_all('tr')[0:]
        listItem = BeautifulSoup(str(programHTML), 'html.parser').find_all('li')[314:347]

        localData = dict()
        size = len(rows)
        for row in range(7, size):
            cols = rows[row].find_all('td')
            if len(cols) > 0:
                localData = {
                    'course_code': cols[1].text.strip(),
                    'course_title': cols[2].text.strip(),
                    'theory_credit': '',
                    'lab_credit': '',
                    'total_credit': '',
                    'prerequisit': '',
                    'program':'bba',
                    'semester':''
                }
            finalData.append(localData)
        for item in listItem:
            localData = {
                'course_code': item.text[0:7].strip(),
                'course_title': item.text[8:].strip(),
                'theory_credit': '',
                'lab_credit': '',
                'total_credit': '',
                'prerequisit': '',
                'program':'bba',
                'semester':''
                
            }
            finalData.append(localData)

        print(json.dumps(finalData))
    except Exception as ex:
        finalData = {'status': 'failed', 'reason': str(ex)} 
    return finalData


getBBACourse("/home/course_details/bba")