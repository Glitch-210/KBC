questions = [
    [
        "Who is not in singham again?",
        "Ajay Devgan","Shahrukh khan","Ranveer Singh","Tiger Shroff",2
    ],
    [
        "Who is not in Bhool bhulaiya 3?",
        "Kartik Aryan","Vidya Balan","Tripti Dimri","Akshay kumar",4
    ],
    [
        "When is Srk's Birthday?",
        "1 Nov","4 Oct","2 Nov","3 Nov",3
    ],
    [
        "How Long is Singham Again Trailer is?",
        "4m 43s","4m 58s","3m 40s","5m",2
    ],
    [
        "Who is known as 'Bhaijaan' in bollywood",
        "Salman Khan","Shahrukh khan","Amir Khan","Saif Ali Khan",1
    ],
    [
        "What was the collection of bahubali 2 in 10 days from release?",
        "100 crore","400 crore","1000 crore","2000 crore",3
    ],
    [
        "Release Date of Action Jackson?",
        "5 December 2014","1 December 2013","4 November 2014","5 December 2012",1
    ],
    [
        "Gross Collection of film 'Jai ho'?",
        "195 crore","200 crore","222 crore","295 crore","none",1
    ],
    [
        "Which is the First Movie of Sunil Shetty",
        "Jawaan","Balwaan","Bhai","Krishna","none",2
    ],
    [
        "What was the name of Jhonny Lever in the film 'De Dana Dan'",
        "Maama","Javed","Krishna","Kaala",4
    ],
    [
        "Which of the following film is not made by Sandeep Reddy Vanga?",
        "Kabir Singh","Animal","Adithya Varma","Spirit","none",3
    ],
    [
        "Which Film was rejected by Srk?",
        "Munna Bhai Mbbs","Highway","A Wednesday","Spirit","none",1
    ],
    [
        "In which year did Katrina Kaif made her debut in Bollywood?",
        "2000","2001","2002","2003","none",4
    ],
    [
        "Net Worth Of Shahid Kapoor",
        "300 crore","500 crore","1000 crore","100 crore",1
    ],
    [
        "Which is the first movie of karan johar as a director?",
        "Kabhi Khushi Kabhi Gham","Kuch Kuch Hota Hai","Ddlj","Student of the year",2
    ]
]

levels = [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000]
money=0
for i in range(0,len(questions)):
    question = questions[i]
    print(f"Question for Rs.{levels[i]}")
    print(f"{question[0]}")
    print(f"a.{question[1]}       b.{question[2]}")
    print(f"c.{question[3]}       d.{question[4]}")
    reply = int(input("Enter Answer(1-4): "))
    if(reply == question[-1]):
        print(f"Congratulations!, you have won {levels[i]} rupees\n")
        if(i==4):
            money=10000
            print(f"Now You have {money} rupees to take away with you!")
            ask = input("Do you want to quit (y/n)")
            if(ask == 'n'.lower):
                break
        elif(i==9):
            money=320000
            print(f"Now You have {money} rupees to take away with you!")
            ask = input("Do you want to quit (y/n)")
            if(ask == 'n'.lower):
                break
        elif(i==14):
            money==10000000

    else:
        print("Sorry wrong answer")
        break
print(f"Now You have {money} rupees to take away with you!,See you Next Time!")
