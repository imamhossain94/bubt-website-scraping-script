# BUBT WEBSITE SCRAPPING SCRIPT

Convert html into json data

#### Directories:
courses:    contains all courses scrapping scripts.\
faculties/script:   contains all faculties scrapping scripts.\
faculties/..:   contains all faculties image by department name.\
json_data/..:   contains all the courses and faculties information in json format.


#### Sample Json Data

##### courses:
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