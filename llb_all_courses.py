from requests import get, post, Session
import json
from bs4 import BeautifulSoup
import json
baseURL = 'https://www.bubt.edu.bd'

def getLLBCourse(programUrl):
    finalData = {'data': list()}

    try:
        programHTML = get(baseURL+programUrl).text
        tables = BeautifulSoup(str(programHTML), 'html.parser').find_all('table')[0]
        rows = BeautifulSoup(str(tables), 'html.parser').find_all('tr')[0:]
        year = semester = ""
        for row in rows[2:59]:
            cols = row.find_all('td')
            if len(cols) > 0:
                if len(cols) == 5:
                    year = cols[0].text.strip()
                    semester = cols[1].text.strip()
                    localData = {
                        # 'year': year,
                        # 'semester': semester,
                        'course_code': cols[2].text.strip(),
                        'course_title': cols[3].text.strip(),
                        'theory_credit': '',
                        'lab_credit': '',
                        'total_credit': cols[4].text.strip(),
                        'prerequisit': ''
                    }
                if len(cols) == 2:
                    semester = cols[0].text.strip()
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
        print(json.dumps(finalData))     
    except Exception as ex:
        finalData = {'status': 'failed', 'reason': str(ex)} 
    return finalData

getLLBCourse("/home/course_details/llb-hons")