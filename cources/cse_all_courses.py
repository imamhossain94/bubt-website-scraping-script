from requests import get, post, Session
import json
from bs4 import BeautifulSoup
import json
baseURL = 'https://www.bubt.edu.bd'

def getCSECourse(programUrl):
    finalData = {'data': list()}
    try:
        programHTML = get(baseURL+programUrl).text
        tables = BeautifulSoup(str(programHTML), 'html.parser').find_all('table')[0:]
        course_data = []
        for table in tables:
            rows = BeautifulSoup(str(table), 'html.parser').find_all('tr')[0:]
            for row in rows[2:]:
                cols = row.find_all('td')
                if len(cols) > 0:
                    course_code = cols[0].text.strip()
                    course_title = cols[1].text.strip()
                    if ',' in course_code:
                        for i in range(2):
                            localData = {
                                'course_code': course_code.split(',')[i].strip() if i == 0 else 'CSE ' + course_code.split(',')[i].strip() ,
                                'course_title': course_title.split('&')[0].strip() if i == 0 else course_title.replace("& ", "").strip(),
                                'theory_credit': cols[2].text.strip(),
                                'lab_credit': cols[3].text.strip(),
                                'total_credit': cols[4].text.strip(),
                                'prerequisit': cols[5].text.strip(),
                                'program':'cse',
                                'semester':''
                            }
                            course_data.append(localData)  
                    else:
                        localData = {
                            'course_code': cols[0].text.strip(),
                            'course_title': cols[1].text.strip(),
                            'theory_credit': cols[2].text.strip(),
                            'lab_credit': cols[3].text.strip(),
                            'total_credit': cols[4].text.strip(),
                            'prerequisit': cols[5].text.strip(),
                            'program':'cse',
                            'semester':''
                        }
                        course_data.append(localData)  
        course_data = [x for x in course_data if x['course_code'] != 'CSE 4**']
        finalData['data'] = course_data
        print(json.dumps(finalData))  
    except Exception as ex:
        finalData = {'status': 'failed', 'reason': str(ex)} 
        print(json.dumps(finalData)) 
    return finalData


getCSECourse("/home/course_details/bsc-in-cse")