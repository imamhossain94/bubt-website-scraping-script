from requests import get, post, Session
import json
from bs4 import BeautifulSoup
import json




def getStudentsNameInfo():

    finalData = list()
    try:
        for i in range(17182103001, 17182103500):
            # 99,999,999,999 - 10,000,000,000 = 89,999,999,999
            baseURL = 'https://bubt.edu.bd/global_file/getData.php?id=%s&type=stdVerify'%(i)
            response = get(baseURL)
            json_data = json.loads(response.text)

            if json_data is not None:
                print("%s, %s"%(json_data['sis_std_id'], json_data['sis_std_name']))
        print(json.dumps(finalData))
    except Exception as ex:
        print('error: %s'%(ex))
        print(i)

getStudentsNameInfo()
