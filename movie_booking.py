import mysql.connector
databases=mysql.connector.connect(host="localhost",username="root",password="12345",database="movie_ticket_booking")
cur=databases.cursor()
import smtplib
import random  
def email_sendings(movie_name,No_of_seats,Enter_row,Ticket_cost,):
        try:
           receiver_mails=["sivan25970@gmail.com"]
           for i in receiver_mails:
            you_booked_movie_name=movie_name
            print(i,you_booked_movie_name)
            s=smtplib.SMTP("smtp.gmail.com",587)
            s.starttls()
            s.login("rogini263@gmail.com","syvt numl jpjn mqri")
            message=f"In GJ Theatre you booked the movie {you_booked_movie_name} with {No_of_seats} seats of row {Enter_row}  the total cost of {Ticket_cost}/- \nThank for booking in GJ theatre!! "
            s.sendmail("rogini263@gmail.com",i,message)
            s.quit()
            print("mail sends sucessfully")
        except:
          print("mail not send")
def Maharaja():
    per_person_ticket_rate={'elite1':170,'elite2':150,'economy1':130}
    orginal_ticket_rate={'elite1':165,'elite2':146,'economy1':125}
    movie_name=input("enter the movie name for confirm:")
    movie_time=input("enter the movie_time:")
    print("The avaliable seats:\n 1.Elite1 \n 2.Elite2 \n 3.Economy1")
    Enter_row=input("enter you row seats:")
    No_of_seats=int(input("enter the no of seats:"))
    Ticket_cost=per_person_ticket_rate[Enter_row]*No_of_seats
    Gst_amount=per_person_ticket_rate[Enter_row]-orginal_ticket_rate[Enter_row]
    Gst_percent=((Gst_amount*100)/orginal_ticket_rate[Enter_row])
    Gst_amount=Gst_amount*No_of_seats
    print("you booked tickets sucessfully")
    import datetime 
    x=datetime.datetime.now()
    f=open("bill.txt","a")
    f.write(f"you booked movie {movie_name} with  {No_of_seats}{Enter_row} seats with the gst cost of  {Gst_amount}/-  and  the total cost{Ticket_cost}/- at the time {x}  \n")
    email_sendings(f"{movie_name}",f"{No_of_seats}",f"{Enter_row}",f"{Ticket_cost}")
    sql="insert into movie_booking values(%s,%s,%s,%s,%s)"
    movie_name=movie_name
    no_of_seats=No_of_seats
    gst_cost=Gst_amount
    gst_percent=Gst_percent
    ticket_cost=Ticket_cost
    val=(movie_name,no_of_seats,gst_cost,gst_percent,ticket_cost)
    cur.execute(sql,val)
    databases.commit()
    print("data saved sucessfully")
    main()
def kalki():
    per_person_ticket_rate={'elite3d':200,'elite2':150,'balcony':130}
    orginal_ticket_rate={'elite3d':194,'elite2':143,'balcony':125}
    movie_name=input("enter the movie name for confirm:")
    movie_time=input("enter the movie_time:")
    print("The avaliable seats:\n 1.Elite 3d \n 2.Elite2 \n 3.Balcony")
    Enter_row=input("enter you row seats:")
    No_of_seats=int(input("enter the no of seats:"))
    Ticket_cost=per_person_ticket_rate[Enter_row]*No_of_seats
    Gst_amount=per_person_ticket_rate[Enter_row]-orginal_ticket_rate[Enter_row]
    Gst_percent=((Gst_amount*100)/orginal_ticket_rate[Enter_row])
    Gst_amount=Gst_amount*No_of_seats
    print("you ticket booked sucessfully")
    import datetime 
    x=datetime.datetime.now()
    f=open("bill.txt","a")
    f.write(f"you booked movie {movie_name} with {No_of_seats}{Enter_row} seats with the gst cost  {Gst_amount}/-  and  the total cost{Ticket_cost}/- at the time {x} \n")
    email_sendings(f"{movie_name}",f"{No_of_seats}",f"{Enter_row}",f"{Ticket_cost}")
    sql="insert into movie_booking values(%s,%s,%s,%s,%s)"
    movie_name=movie_name
    no_of_seats=No_of_seats
    gst_cost=Gst_amount
    gst_percent=Gst_percent
    ticket_cost=Ticket_cost
    val=(movie_name,no_of_seats,gst_cost,gst_percent,ticket_cost)
    cur.execute(sql,val)
    databases.commit()
    print("data saved sucessfully")
    main()
def A_quiet_place_one_day():
    per_person_ticket_rate={'elite2':150,'elite3':130,'economy3':100}
    orginal_ticket_rate={'elite2':143,'elite3':125,'economy3':96}
    movie_name=input("enter the movie name for confirm:")
    movie_time=input("enter the movie_time:")
    print("The avaliable seats:\n 1.Elite3 \n 2.Elite2 \n 3.Economy3")
    Enter_row=input("enter you row seats:")
    No_of_seats=int(input("enter the no of seats:"))
    Ticket_cost=per_person_ticket_rate[Enter_row]*No_of_seats
    Gst_amount=per_person_ticket_rate[Enter_row]-orginal_ticket_rate[Enter_row]
    Gst_percent=((Gst_amount*100)/orginal_ticket_rate[Enter_row])
    Gst_amount=Gst_amount*No_of_seats
    print("you booked ticket sucessfully")
    import datetime 
    x=datetime.datetime.now()
    f=open("bill.txt","a")
    f.write(f"you booked movie {movie_name} with{No_of_seats}{Enter_row} seats with the gst cost and  {Gst_amount}/- and  the total cost{Ticket_cost}/- at the time {x} \n")
    email_sendings(f"{movie_name}",f"{No_of_seats}",f"{Enter_row}",f"{Ticket_cost}")
    sql="insert into movie_booking values(%s,%s,%s,%s,%s)"
    movie_name=movie_name
    no_of_seats=No_of_seats
    gst_cost=Gst_amount
    gst_percent=Gst_percent
    ticket_cost=Ticket_cost
    val=(movie_name,no_of_seats,gst_cost,gst_percent,ticket_cost)
    cur.execute(sql,val)
    databases.commit()
    print("data saved sucessfully")
    main()
def main():
    print("**GJ Theatre**")
    print("The avaliable movies:\n 1.Maharaja \n 2.Kalki \n 3.A quit place:day one")
    print("The movie timings:\n 1->10:00 \n 2->1:30 \n 3->3:00 \n 4->6:30 \n 5->9:00")
    Book=input("you want to book ticket:")
    if Book=="yes":
        Date=input("enter the date you want to watch movie :")
        Day=input("enter the day you want to watch movie:")
        Movie_name=input("enter the movie name you want to book tickets:")
        if Movie_name=="maharaja":
            Maharaja()
        if Movie_name=="kalki":
           kalki()
        if Movie_name=="a quiet place":
           A_quiet_place_one_day()
    else:
       print("Thanks for visting GJ theatre")
main()



   
  


