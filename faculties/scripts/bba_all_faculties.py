from requests import get, post, Session
import json
from bs4 import BeautifulSoup
import json
import random
import base64
from PIL import Image
from io import BytesIO
import firebase_admin
from firebase_admin import storage
from firebase_admin import credentials


baseURL = 'https://www.bubt.edu.bd'
cred = credentials.Certificate("serviceAccountKey.json") #firebase service account json key
firebase_admin.initialize_app(cred, {'storageBucket': 'bubt-smart-routine.appspot.com'})


# decode base64 string and upload it into firebase to get short image link
def uploadImageFile(fileName, stringFile):
    try:
        randId = random.randint(1000,9000)
        im = Image.open(BytesIO(base64.b64decode(stringFile.replace('data:image/png;base64,', ''))))
        im.save('faculties/bba/%s_%d.png'%(fileName, randId), 'PNG')
        bucket = storage.bucket()
        blob = bucket.blob('bba/%s_%d.png'%(fileName, randId))
        blob.upload_from_filename('faculties/bba/%s_%d.png'%(fileName, randId))
        blob.make_public()
        return blob.public_url
    except Exception as e:
        print("Error Uploading Image :" + str(e))
        return ''


def getEmaiAddress(url):
    emailAddress = ''
    try:
        url = get(url).text
        div = BeautifulSoup(str(url), 'html.parser').find('div', class_="col-sm-6 col-md-8")
        p = str(div.find_all('p')[3])
        emailAddress = p.split('<br/>')[1].lower().replace('email:', '').strip()
    except Exception as ex:
        emailAddress = ''

    return emailAddress


def getBBAFaculties(facultyUrl):
    finalData = {'data': list()}
    try:
        for i in range(4):
            url = get(baseURL+facultyUrl[i]).text
            for i in range([20, 11, 6, 8][i]):
                div = BeautifulSoup(str(url), 'html.parser').find_all('div', class_="faculty-member faculty-member%d"%(i))[0]
                h3 = str(div.find('h3'))
                for r in (('/', ''), ('<h3>', ''), ('<span>', ''), ('<sub>', ''), ('amp;', '')):
                    h3 = h3.replace(*r)
                h3 = h3.split('<em>')
                teacher_name = h3[0]
                designation = h3[1]
                status = h3[2].replace('(', '').replace(')', '').strip()
                teacher_code = div.find('img').attrs['alt']
                link = div.find('a', href=True)['href']
                image = uploadImageFile(teacher_name, div.find('img').get('src'))
                email = getEmaiAddress(link)
                localData = {
                    'teacher_name': teacher_name,
                    'teacher_code': teacher_code,
                    'email': email,
                    'designation': designation,
                    'status': status,
                    'link': link,
                    'image': image
                }
                finalData['data'].append(localData)
        print(json.dumps(finalData)) 
    except Exception as ex:
        finalData = {'status': 'failed', 'reason': str(ex)} 
        print(json.dumps(finalData)) 
    return finalData


getBBAFaculties([
    "/home/faculty_member/management",
    "/home/faculty_member/accounting",
    "/home/faculty_member/marketing",
    "/home/faculty_member/finance"
])
