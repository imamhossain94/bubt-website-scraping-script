from requests import get, post, Session
import json
from bs4 import BeautifulSoup
import json




def getFacultiesID():

    finalData = list()
    try:
        for i in range(18020330000, 18020339999):
            # 99,999,999,999 - 10,000,000,000 = 89,999,999,999
            baseURL = 'https://bubt.edu.bd/global_file/getData.php?id=%s&type=empVerify'%(i)
            response = get(baseURL)
            json_data = json.loads(response.text)

            if 'StatusId' not in json_data:
                data = {
                    'EmpId' : json_data[0]['EmpId'],
                    'DemoId' : json_data[0]['DemoId'],
                    'EmpName' : json_data[0]['EmpName'],
                }
                print(i)
                finalData.append(data)
        print(json.dumps(finalData))
    except Exception as ex:
        print('error')
        print(i)

# getFacultiesID()


# EmpIds = [18020331033,18020331034,18020331035,18020331036,18020331037,18020331038,18020331039,18020331047,18020331049,18020332020,18020332021,18020332022,18020332023,18020332024,18020332025,18020332026,18020332027,18020332028,18020332029,18020332032,18020332035,18020332036,18020332037,18020332051,18020333005,18020333050,18020335001,18020336001]

# print(len(EmpIds))



# 0004934709075,19509
def getFacultiesID():

    finalData = list()
    try:
        for i in range(18020330000, 18020339999):
            # 99,999,999,999 - 10,000,000,000 = 89,999,999,999
            baseURL = 'https://bubt.edu.bd/global_file/getData.php?id=%s&type=empVerify'%(i)
            response = get(baseURL)
            json_data = json.loads(response.text)

            if 'StatusId' not in json_data:
                data = {
                    'EmpId' : json_data[0]['EmpId'],
                    'DemoId' : json_data[0]['DemoId'],
                    'EmpName' : json_data[0]['EmpName'],
                }
                print(i)
                finalData.append(data)
        print(json.dumps(finalData))
    except Exception as ex:
        print('error')
        print(i)