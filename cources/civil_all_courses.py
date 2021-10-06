from requests import get, post, Session
import json
from bs4 import BeautifulSoup
import json
baseURL = 'https://www.bubt.edu.bd'


def getCIVILCourse(programURL):
    finalData = {'data': list()}
    try:
        programHTML = get(baseURL+programURL).text
        tables = BeautifulSoup(str(programHTML), 'html.parser').find_all('table')[0:9]
        course_data = []
        for table in tables:
            rows = BeautifulSoup(str(table), 'html.parser').find_all('tr')[0:]

            for row in rows[0:]:
                cols = row.find_all('td')
                if len(cols) > 4:
                    localData = {
                        'course_code': cols[0].text.strip(),
                        'course_title': cols[1].text.strip(),
                        'theory_credit': cols[2].text.strip(),
                        'lab_credit': cols[3].text.strip(),
                        'total_credit': cols[3].text.strip(),
                        'prerequisit': cols[4].text.strip() if len(cols) > 4 else ''
                    }
                    course_data.append(localData)  
        finalData['data'] = course_data
        print(json.dumps(finalData))  
    except Exception as ex:
        finalData = {'status': 'failed', 'reason': str(ex)} 
        # print(json.dumps(finalData))  
    return finalData


getCIVILCourse("/department/dept_menu_details/64")
