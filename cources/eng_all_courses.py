from requests import get, post, Session
import json
from bs4 import BeautifulSoup
import json
baseURL = 'https://www.bubt.edu.bd'

def getENGCourse(programUrl):
    finalData = {'data': list()}
    try:
        programHTML = get(baseURL+programUrl).text
        tables = BeautifulSoup(str(programHTML), 'html.parser').find_all('table')[1:]
        for table in tables:
            rows = BeautifulSoup(str(table), 'html.parser').find_all('tr')[0:]
            localData = dict()
            for row in rows[0:]:
                cols = row.find_all('td')
                if len(cols) == 3:
                    localData = {
                        'course_code': cols[0].text.strip(),
                        'course_title': cols[1].text.strip(),
                        'theory_credit': '',
                        'lab_credit': '',
                        'total_credit': cols[2].text.strip(),
                        'prerequisit': ''
                    }
                    finalData['data'].append(localData)
        # print(json.dumps(finalData))
    except Exception as ex:
        finalData = {'status': 'failed', 'reason': str(ex)} 
    return finalData

getENGCourse("/home/course_details/ba-hons-in-english")