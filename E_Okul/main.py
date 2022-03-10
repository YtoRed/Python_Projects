print("░P░y░t░h░o░n░ ░E░l░e░c░t░r░o░i░c░ ░S░c░h░o░o░l░ ░S░y░s░t░e░m░")

username = input("Username: ")

password = input("Password: ")

if username and password =="123":
    main = int(input("System load success: \n 0: Announcements \n 1: Exam Grades \n 2: Schedule \n 3: Exam Schedule \n : "))

if main == 0:
    print("Announcements: \n HappySnow Holiday 3/10/2022 \n Exams on the way! 3/2/2022 \n Happy Term Holiday! 10/02/2022")

if main ==1:
    print("Grades: \n Turkish: 70 \n Math: 50 \n Biology: 85 \n English: 90 \n Physics: 90")

if main== 2:
    print("Schedule : \n Monday: Turkish \n Tuesday: Math \n Wednesday: Geo \n Thursday: English \n Friday: Chemical")

if main==3:
    print("Exam Schedule: \n Empty")


else:
    print("Username or password not match")
    pass