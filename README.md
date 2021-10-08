# BUBT WEBSITE SCRAPPING SCRIPT

I think this is the first public repository that provides free BUBT website scraping API  script on github. When I was doing my 3rd year project one for my friend <a href="https://github.com/xaadu">Abdullah Xayed</a> wrote an web scraping project for me. Now I add some extra feature on it.

## Important Note
I am not sharing some api script with you due to security reason. And I am requisting you not to use any of this provided api for production use. I already give you the API script. So, Host them on your web server and then use them for the production.

## Project Directories
| Path | Description |
| :-- | :-- |
| `./cources` | Contains all course scrapping scripts.|
| `./faculties/scripts` | Contains all facultie scrapping scripts.|
| `./notices_events` | Contains notices_events scrapping scripts.|
| `./faculties` | Contains all faculties image by department name sub folder.|
| `./json_data` | Contains all the courses, faculties & notices_events information in json format.|

## API Contribution
* <a href="https://github.com/xaadu">API BY BUBT</a>

           •Student Verify 
           •Faculty Verify
* <a href="https://github.com/xaadu">Abdullah Xayed</a>

           •Annex Login 
           •Annex Result 
           •Annex Fees 
           •Annex Routine 
           •All Events 
           •Event Details 
           •All Notices 
           •Notice Details 
* <a href="https://github.com/xaadu">Md. Imam Hossain</a>

           •Courses API Scrit: CSE, EEE, CIVIL, TEXTILE, BBA, ECO, EDE, LLB, ENG.
           •Faculty API Script: CSE, EEE, CIVIL, TEXTILE, BBA, ECO, EDE, LLB, ENG.
           •Notice 
           •Notice Details 
           •Events 
           •Events Details 
           •Routine API
    
### API Response & Type
BUBT API:

| Name | Method | Description | Examples |
| :-- | :-- | :-- | :-- |
| Student Verify | `GET`| Verify bubt students | [`/global_file/getData.php?id=?&type=?`](https://bubt.edu.bd/global_file/getData.php?id=17181103084&type=stdVerify) |
| Faculty Verify | `GET`| Verify bubt faculty  | [`/global_file/getData.php?id=?&type=?`](https://bubt.edu.bd/global_file/getData.php?id=18020331033&type=empVerify) |

Abdullah Xayed API: (v1)

| Name | Method | Description | Examples |
| :-- | :-- | :-- | :-- |
| Annex Login | `GET`| Verify bubt faculty  | [`/bubt/v1/login?id=?&pass=?`](https://bubt.herokuapp.com/bubt/v1/login?id=17181103084&pass=password) |
| Annex Result | `GET`| Get student result from annex by session id | [`/bubt/v1/prevCourses?phpsessid=?`](https://bubt.herokuapp.com/bubt/v1/prevCourses?phpsessid=7d1755fe6c32b74d321fe3d3ba69a4ad) |
| Annex Fees | `GET`| Get student fees from annex by session id | [`/bubt/v1/fees?phpsessid=?`](https://bubt.herokuapp.com/bubt/v1/fees?phpsessid=7d1755fe6c32b74d321fe3d3ba69a4ad) |
| Annex Routine | `GET`| Get student routine  from annex by session id `Not working, Cause routine shift from annex to BUBT Soft` | [`/bubt/v1/routine?phpsessid=?`](https://bubt.herokuapp.com/bubt/v1/routine?phpsessid=7d1755fe6c32b74d321fe3d3ba69a4ad) |
| All Events | `GET`| Get all events from bubt website | [`/bubt/v1/allEvent?`](https://bubt.herokuapp.com/bubt/v1/allEvent?) |
| Events Details | `GET`| Get an event details by events url | [`/bubt/v1/eventDetails?url=?`](https://bubt.herokuapp.com/bubt/v1/eventDetails?url=https://www.bubt.edu.bd/home/event_details/200) |
| All Notice | `GET`| Get all notices from bubt website | [`/bubt/v1/allNotice?`](https://bubt.herokuapp.com/bubt/v1/allEvent?) |
| Notice Details | `GET`| Get a notice details by notices url | [`/bubt/v1/noticeDetails?url=?`](https://bubt.herokuapp.com/bubt/v1/noticeDetails?url=https://www.bubt.edu.bd/home/notice_details/665) |

Md. Imam Hossain API: (v2)

| Name | Method | Description | Examples |
| :-- | :-- | :-- | :-- |
| Events | `GET`| Get events from bubt website by page and limit | [`/bubt/v2/allEvent?page=?&limit=?`](https://smart-notice-bubt.herokuapp.com/bubt/v2/allEvent?page=0&limit=5) |
| Events Details | `GET`| Get an event details by events url | [`bubt/v2/eventDetails?url=?`](https://smart-notice-bubt.herokuapp.com/bubt/v2/eventDetails?url=https://www.bubt.edu.bd/home/event_details/200) |
| Notice | `GET`| Get notices from bubt website by page and limit | [`/bubt/v2/allNotice?page=?&limit=?`](https://smart-notice-bubt.herokuapp.com/bubt/v2/allNotice?page=0&limit=5) |
| Notice Details | `GET`| Get a notice details by notices url | [`/bubt/v2/noticeDetails?url=?`](https://smart-notice-bubt.herokuapp.com/bubt/v2/noticeDetails?url=https://www.bubt.edu.bd/home/notice_details/665) |
| Smart Routine | `GET`| Get student routine  from BUBT Soft by students id `Secret API` | [`/bubt/v2/getRoutine?stdId=?`](https://smart-routine-bubt-four.herokuapp.com/bubt/v2/getRoutine?stdId=17181103084) |


### Sample Json Data

Student Verify:
```json
{
  "sis_std_id": "17181103084",
  "sis_std_name": "Md. Imam Hossain",
  "sis_std_prgrm_sn": "B.Sc. Engg. in CSE",
  "sis_std_prgrm_id": "006",
  "sis_std_intk": "37",
  "sis_std_email": "imamagun94@gmail.com",
  "sis_std_father": "Mahbub Rashid",
  "sis_std_gender": "M",
  "sis_std_LocGuardian": "Mahbub Rashid",
  "sis_std_Bplace": "Vasantek, Dhaka",
  "sis_std_Status": "R",
  "sis_std_blood": "",
  "gazo": "data:image/jpeg;base64,"
}
```

Faculty Verify:
```json
[
  {
    "EmpId": "18020331033",
    "DemoId": "18020331033",
    "EmpName": "Md. Ahsanul Haque",
    "DOB": "1996-06-21T00:00:00",
    "PermanentAddress": "South Atapara, Bogura Sadar-5800, Bogura",
    "FatherName": "Md. Abdul Awal",
    "ECName": "Md. Abdul Awal",
    "ECNo": "01711936404",
    "ECRelation": "Father",
    "Gender": "Male",
    "DeptName": "Department of Computer Science & Engineering",
    "PosName": "Lecturer",
    "BloodGroup": "A+",
    "StatusId": "1",
    "EmpImage": "data:image/jpeg;base64,"
    }
]
```

Annex Login:
```json
{
  "PHPSESSID": "7d1755fe6c32b74d321fe3d3ba69a4ad",
  "status": "success"
}
```

Annex Result:
```json
{
  "data": [
    {
      "cgpa": "3.22",
      "results": [
        {
          "code": "ENG 101",
          "credit": "3",
          "grade": "B-",
          "title": "English Language-I",
          "type": "Theory"
        }
      ],
      "semester": "Fall, 2017-18",
      "sgpa": "3.22"
    }
  ],
  "status": "success"
}
```

Annex Fees:
```json
{
  "data": [
    {
      "Demand": "44195",
      "Due": "0",
      "Paid": "44195",
      "Remarks": "Semester Charge+Tuition Fees+Others",
      "Semester": "Fall, 2017-18",
      "Waiver": "0",
      "payments": [
        {
          "Account_Code": "319",
          "Payment_Amount": "15600",
          "Payment_No": "1",
          "Reciept_No": "18888",
          "Waiver": "0"
        },
        {
          "Account_Code": "319",
          "Payment_Amount": "28595",
          "Payment_No": "2",
          "Reciept_No": "43019",
          "Waiver": "0"
        }
      ]
    }
  ],
  "result": {
    "Total_Demand": "384816",
    "Total_Due": "7442",
    "Total_Paid": "353923",
    "Total_Waiver": "23451"
  },
  "status": "success"
}
```

Annex Routine:
```json
{
  "data": [
    {
      "Building": "",
      "Day": "Saturday",
      "Intake": "",
      "Room_No": "",
      "Schedule": "08:30 AM to 10:00 AM",
      "Section": "",
      "Subject_Code": "",
      "Teacher_Code": ""
    }
  ],
  "status": "success"
}
```

All Events:
```json
{
  "data": [
    {
      "published_on": "5 Aug 2021",
      "title": "International Conference on Science and Contemporary Technologies (ICSCT) Opened at BUBT",
      "url": "https://www.bubt.edu.bd/home/event_details/200"
    }
  ],
  "status": "success"
}
```

Annex Notices:
```json
{
  "data": [
      {
        "category": "Exam Related",
        "published_on": "8 Oct 2021",
        "title": "Defense Notice",
        "url": "https://www.bubt.edu.bd/home/notice_details/665"
      }
  ],
  "status": "success"
}
```

Events Details:
```json
{
    "data": {
      "description": "Bangladesh University of  Business and Technology  (BUBT) organized a virtual Orientation  Program for Spring 2021 Students on April 22, 2021....",
      "downloads": [
        {
          "url": ""
        }
      ],
      "images": [
        {
          "url": "https://www.bubt.edu.bd/assets/frontend/media/1619504011BUBT_22_04__2021.jpg"
        }
      ],
      "pubDate": "25 Apr 2021",
      "title": "Virtual Orientation for Spring 2021 Students at BUBT"
    },
    "status": "success"
  }
```


Annex Login:
```json
{
  "PHPSESSID": "7d1755fe6c32b74d321fe3d3ba69a4ad",
  "status": "success"
}
```


Annex Login:
```json
{
  "PHPSESSID": "7d1755fe6c32b74d321fe3d3ba69a4ad",
  "status": "success"
}
```

```json
{
    "data":[
       {
          "course_code":"CSE 101",
          "course_title":"Computer and Programming Concepts",
          "theory_credit":"3.00",
          "lab_credit":"1.50",
          "total_credit":"4.50",
          "prerequisit":""
       },
       {
          "course_code":"102",
          "course_title":"Computer and Programming Concepts Lab",
          "theory_credit":"3.00",
          "lab_credit":"1.50",
          "total_credit":"4.50",
          "prerequisit":""
       },
       {
          "course_code":"MAT 101",
          "course_title":"Differential and Integral Calculus",
          "theory_credit":"3.00",
          "lab_credit":"-",
          "total_credit":"3.00",
          "prerequisit":""
       },
       {
          "course_code":"ENG 101",
          "course_title":"English Language-I",
          "theory_credit":"3.00",
          "lab_credit":"-",
          "total_credit":"3.00",
          "prerequisit":""
       },
       ...
    ]
}
```

##### faculties:
```json
{
    "data":[
       {
        "teacher_name": "Dr.Muhammad Firoz Mridha",
        "teacher_code": "DMFM",
        "email": "firoz@bubt.edu.bd",
        "designation": "Associate Professor & Chairman",
        "status": "",
        "link": "https://www.bubt.edu.bd/department/member_details/332",
        "image": "https://storage.googleapis.com/bubt-smart-routine.appspot.com/cse/Dr.Muhammad%20Firoz%20Mridha_3199.png"
      },
      {
        "teacher_name": "Md. Saifur Rahman",
        "teacher_code": "SR",
        "email": "saifurs@gmail.com",
        "designation": "Assistant Professor",
        "status": "",
        "link": "https://www.bubt.edu.bd/department/member_details/80",
        "image": "https://storage.googleapis.com/bubt-smart-routine.appspot.com/cse/Md.%20Saifur%20Rahman_4345.png"
      },
      {
        "teacher_name": "Md. Raisul Alam",
        "teacher_code": "MRA",
        "email": "ralam02@yahoo.com",
        "designation": "Assistant Professor",
        "status": "",
        "link": "https://www.bubt.edu.bd/department/member_details/81",
        "image": "https://storage.googleapis.com/bubt-smart-routine.appspot.com/cse/Md.%20Raisul%20Alam_5333.png"
      },
      {
        "teacher_name": "Mijanur Rahman",
        "teacher_code": "MRN",
        "email": "riponcse.it@bubt.edu.bd",
        "designation": "Assistant Professor",
        "status": "",
        "link": "https://www.bubt.edu.bd/department/member_details/87",
        "image": "https://storage.googleapis.com/bubt-smart-routine.appspot.com/cse/Mijanur%20Rahman_4327.png"
      },
      {
        "teacher_name": "Md. Shahiduzzaman",
        "teacher_code": "MSZ",
        "email": "shahid@bubt.edu.bd",
        "designation": "Assistant Professor",
        "status": "",
        "link": "https://www.bubt.edu.bd/department/member_details/89",
        "image": "https://storage.googleapis.com/bubt-smart-routine.appspot.com/cse/Md.%20Shahiduzzaman_4477.png"
      },
      {
        "teacher_name": "Sabiha Firdaus",
        "teacher_code": "SF",
        "email": "sabiha@bubt.edu.bd",
        "designation": "Assistant Professor",
        "status": "",
        "link": "https://www.bubt.edu.bd/department/member_details/90",
        "image": "https://storage.googleapis.com/bubt-smart-routine.appspot.com/cse/Sabiha%20Firdaus_3649.png"
      },
      {
        "teacher_name": "M. M. Fazle Rabbi",
        "teacher_code": "MMFR",
        "email": "rabbi102@gmail.com",
        "designation": "Assistant Professor",
        "status": "",
        "link": "https://www.bubt.edu.bd/department/member_details/94",
        "image": "https://storage.googleapis.com/bubt-smart-routine.appspot.com/cse/M.%20M.%20Fazle%20Rabbi_7663.png"
      },
      {
        "teacher_name": "Milon Biswas",
        "teacher_code": "MBW",
        "email": "milonbiswas@bubt.edu.bd",
        "designation": "Assistant Professor",
        "status": "",
        "link": "https://www.bubt.edu.bd/department/member_details/103",
        "image": "https://storage.googleapis.com/bubt-smart-routine.appspot.com/cse/Milon%20Biswas_2341.png"
      },
       ...
    ]
}
```



