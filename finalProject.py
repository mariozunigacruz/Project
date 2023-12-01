import csv
import pandas as pd

def read_csv(csv_seats):
    seats={}
    with open(csv_seats,'r') as csv_file:
        reader=csv.reader(csv_file)
        next(reader)
        seats = {rows[0]:rows[1] for rows in reader}
    return seats


def theater():
    print("Which movie do you want to watch ")
    print("Enter 1 for Movie 1")
    print("Enter 2 for Movie 2")
    print("Enter 3 for Movie 3")
    print("Enter 4 to exit.")
    a = int(input("Choose your movie: "))
    return a
    

def movietype(a=int):
    if a ==1:
        seat = str(input("Choose a seat 1-50: "))
        return seat
        
    elif a == 2:
        seat = str(input("Choose a seat 1-60: "))
        return seat

    elif a == 3:
        seat = str(input("Choose a seat 1-70: "))
        return seat

    elif a ==4:
        print("Thank you for your time. \n")
        return '0'
    else:
       print("Invalid Input. Please Try again. \n")
       return '1'


def availability(movieDict=dict, seat=str):
    values = movieDict.values()
    values_list = list(values)
    countSeats=values_list.count("Taken")
    output=''

    if countSeats == len(values_list):
        output=str("Error! This movie is full, please try again with a different film. \n")
        print(output)
        return output

    elif seat not in movieDict:
        output=str("Invalid seat, please try again. \n")
        print(output)
        return output
        
    else:
        if movieDict[seat] == "Taken":
            output=str("This seat is taken. Please try again. \n")
            print(output)
            return output
        if movieDict[seat] == "Free":
            output=str("Please enter your information \n")
            print(output)
            return output            


def information(a=int,seat=int):
    indexNum=seat-1
    name = str(input("Enter your name: "))
    phone = str(input("Enter your phone: "))
    email = str(input("Enter your email: "))

    if a ==1:
        df = pd.read_csv('Movie 1.csv')
        df.loc[indexNum,'Availability'] = 'Taken'
        df.loc[indexNum,'Name'] = name
        df.loc[indexNum,'Phone'] = phone
        df.loc[indexNum,'email'] = email
        df.to_csv("Movie 1.csv", index= False)
        print("Your ticket as been made. Enjoy your film!")

    elif a == 2:
        df = pd.read_csv("Movie 2.csv")
        df.loc[indexNum,'Availability'] = 'Taken'
        df.loc[indexNum,'Name'] = name
        df.loc[indexNum,'Phone'] = phone
        df.loc[indexNum,'email'] = email
        df.to_csv("Movie 2.csv", index= False)
        print("Your ticket as been made. Enjoy your film!")

    elif a == 3:
        df = pd.read_csv("Movie 3.csv")
        df.loc[indexNum,'Availability'] = 'Taken'
        df.loc[indexNum,'Name'] = name
        df.loc[indexNum,'Phone'] = phone
        df.loc[indexNum,'email'] = email
        df.to_csv("Movie 3.csv", index= False)
        print("Your ticket as been made. Enjoy your film!")


def main():
    #Int choosing the movie
    movieNum=theater()
    #Int choosing the seat
    seatStr=movietype(movieNum)
    #Str choosing the seatA
    seatNum=int(seatStr)
    
    if movieNum ==1:
        availableSeats=read_csv("Movie 1.csv")
        if availability(availableSeats,seatStr) == "Please enter your information \n":
            information(movieNum,seatNum)

    elif movieNum ==2:
        availableSeats=read_csv("Movie 2.csv")
        if availability(availableSeats,seatStr) == "Please enter your information \n":
            information(movieNum,seatNum)

    elif movieNum ==3:
        availableSeats=read_csv("Movie 3.csv")
        if availability(availableSeats,seatStr) == "Please enter your information \n":
            information(movieNum,seatNum)

main()