import time 
import schedule
import smtplib

def wisher(message,subject,recemail):
    email ="sathishksv2003@gmail.com"
    recemail=str(recemail)
    subject =str(subject)
    message =str(message)
    text = f"subject:{subject}\n\n{message}"
    try:
        server = smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login(email,"zczdmmddvfslrihe")
        server.sendmail(email,recemail,text)
        print("email has been send")
    except:
        print("Unable to send!")

def ctb():
    f=open("member.txt",'r')
    today = time.strftime('%m%d')
    flag =0
    for line in f:
        if today in line:
            line = line.split(' ')
            flag=1
            message="Happy "+line[1].strip()+" my dear "+line[2].strip()+" and stay happy forever " "\n Greated By \n "+line[4].strip()
            subject=line[1]
            recemail=line[3]
            wisher(message,subject,recemail)
    if flag ==0:
        print("no_events")
        message=None
    return message


     

schedule_time="11:30"
schedule.every().day.at(schedule_time).do(ctb)


if __name__ == "__main__":
   while True:
    schedule.run_pending()
    time.sleep(2)

