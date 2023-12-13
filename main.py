import random as r
 
print("\t\t\t\t\tMAKE MY TRIP\t\t\t\t\t")
print("\t\t\tCUSTOMER CARE NUMBER:1234567890\t\t\t\t\t")
print("\t\tWELCOME TO THE HOMEPAGE OF MAKE MY TRIP!!!\t\t\t\t\t\n")
 
# creating class for bus transport
class bus:
   # definition to initialize all values
   def _init_(self, bus_trip_choice, bus_type, bus_cost, bus_names, bus_age, bus_gender, bus_trips):
       self.trip_choice = bus_trip_choice
       self.type = bus_type
       self.cost = bus_cost
       self.names = bus_names
       self.age = bus_age
       self.gender = bus_gender
       self.trip = bus_trips
       self.date = None
       self.p = None
   # definition to choose trip
   def TRIPS(self):
       days = self.trip.keys()
       for i in days:
           print(i, " : ", self.trip[i][0], " ", self.trip[i][1])
       self.trip_choice = input("Enter the corresponding available day to your desired bus trip :").upper()
 
   # definition for personal details
   def details(self):
       print(self.trip_choice)
       r = int(input("Sir how many passengers are y'all? :"))
       self.p = r
       print("\n")
       self.date = input("Please enter the corresponding date of your travel:")
       for i in range(1, self.p + 1):
           name = input("ENTER the name of the passenger:")
           self.names.append(name)
           age = int(input("ENTER the age of the passenger:"))
           self.age.append(age)
           gender = input("ENTER the gender of the passenger:")
           self.gender.append(gender)
 
       print("\n")
       c = input("Do you want to continue to the payment panel? (Y/N):").upper()
 
       if c == "Y":
           pass
       else:
           exit()
 
   # definition for payment algorithms
   def payment(self):
       count = len(self.names)
       con = input("Which bus would you prefer? \n1.AC\n2.NON-AC\nCHOICE:").upper()
       print("\n")
 
       if con == "1" or con == "AC":
           self.type = "AC"
           print("The rate of bus travel cost is:  ", self.trip[self.trip_choice][3], "/per person")
           self.cost = count * self.trip[self.trip_choice][3]
           print("Hence your total cost is : ", self.cost, " Rs  ")
 
       elif con == "2" or con == "NON-AC":
           self.type = "NON-AC"
           print("The rate of bus travel cost is:  ", self.trip[self.trip_choice][2], "/per person")
           self.cost = count * self.trip[self.trip_choice][3]
           print("Hence your total cost is : ", self.cost, " Rs  ")
 
       print("\n")
       print("DUE TO THE HARSH CONDITIONS DURING THIS COVID/19 PANDEMIC WE ACCEPT BANKING, ONLINE PAYMENT PLATFORMS "
             "LIKE GOOGLE PAY, PAYTM, PHONE PE, AND SPECIAL LOYALITY CARDS FROM OUR FIRM")
       print("WE DEARLY EXPECT YOU TO THRIVE THIS CONDITION AS THE SAFETY OF OUR EMPLOYES AND CUSTOMERS IS AT UTMOST "
             "IMPORTANCE !!")
 
       print("Plesase select your payment mode:")
       print("1.BANKING\n2.GOOGLE PAY\n3.PHONE PE\n4.PAYTM\n5.SPECIAL LOYALTY CARD")
       mod = input("Enter the mode/srno. : ").upper()
 
       if mod in ("2", "3", "4", "GOOGLE PAY", "PHONE PE", "PAYTM"):
           p = input("Please enter the phone number corresponding to your Online Payment Portal:")
           print("Please enter this OTP in your Online Payment Portal: ", r.randint(1000, 9999))
           print("Now you may continue the payment on the portal!")
 
           e = int(input("\nAfter finishing you may get an OTP from your Online Payment Portal\nPlease Enter that OTP "
                         "here:"))
           print("YOUR TICKET DETAILS WILL BE DESPLAYED NOW :-->\n\n\n\n")
 
       elif mod == "BANKING" or mod == '1':
           ac_no = int(input("Kindly enter the account number:"))
           spin = int(input("Please enter your special pin/password"))
           print("The payment was successful from the bank account number :", ac_no)
           print("YOUR TICKET DETAILS WILL BE DESPLAYED NOW :-->\n\n\n\n")
 
       elif mod == "5" or mod == "SPECIAL LOYALTY CARD":
           n = input("Please enter the name that your loyalty card addresses:")
           g = int(input("Please enter the corresponding special pin number:"))
           print("YOUR TICKET DETAILS WILL BE DESPLAYED NOW :-->\n\n\n\n")
 
   # definition for displaying ticket
   def ticket(self):
       a = input("Please press any Key + Enter to generate the Ticket\n")
       print("THE TICKET :-->\n")
 
       for i in range(0, len(self.names)):
           print("Passenger ", i + 1, " :-")
           print("NAME:", self.names[i], "\nAGE:", self.age[i], "\nGENDER:", self.gender[i])
           print("\n")
 
       print("TRIP: FROM -", self.trip[self.trip_choice][0], " TO -", self.trip[self.trip_choice][1])
       print("TYPE: ", self.type)
       print("COST: ", self.cost)
       print("STATUS : PAID")
 
       with open("database.txt","a") as dat:
           for i in range(1, self.p+1):
               dat.write("BUS TRIP: ")
               dat.write(self.names[i-1])
               dat.write(", ")
               dat.write(str(self.age[i - 1]))
               dat.write(", ")
               dat.write(self.gender[i - 1])
               dat.write(",From: ")
               dat.write(self.trip[self.trip_choice][0])
               dat.write(",To: ")
               dat.write(self.trip[self.trip_choice][1])
               dat.write(",Cost: ")
               dat.write(str(self.cost))
               dat.write(",Date: ")
               dat.write(self.date)
               dat.write("\n")
 
# creating a class for airplane transport
class airplane:
 
   # definition to initialize all values
   def _init_(self, from_air, to_air, air_cl, air_cost, air_type, air_names, air_age, air_gender, fl_name_int, fl_name_dom):
       self.to = to_air
       self.frm = from_air
       self.cl = air_cl
       self.cost = air_cost
       self.type = air_type
       self.names = air_names
       self.age = air_age
       self.gender = air_gender
       self.name_int = fl_name_int
       self.name_dom = fl_name_dom
       self.date = None
       self.p = None
 
   # definition to choose trip
   def trip(self):
       self.type = input("\nWhat type of VOYAGE are you doing? (Domestic/International):").upper()
       self.frm = input("Please enter your DEPARTURE AIRPORT:")
       self.to = input("Please enter your DESTINATION AIRPORT:")
       self.cl = input("Please enter the CLASS you prefer (Business/Economy/First/Premium Economy):").upper()
 
       c = input("Do you wish to continue to the Detailing counter? (Y/N):").upper()
       if c == "Y":
           pass
       else:
           exit()
 
   # definition for personal details
   def detail(self):
       self.p = int(input("\nSir how many passengers are y'all? :"))
       print("\n")
       self.date = input("Please enter the corresponding date of your travel:")
 
       for i in range(1, self.p + 1):
           name = input("ENTER the name of the passenger:")
           self.names.append(name)
           age = int(input("ENTER the age of the passenger:"))
           self.age.append(age)
           gender = input("ENTER the gender of the passenger:")
           self.gender.append(gender)
 
       print("\n")
 
       c = input("Do you want to continue to the payment panel? (Y/N):").upper()
       if c == "Y":
           pass
       else:
           exit()
 
   # definition for payment algorithms
   def payment(self):
       count = len(self.names)
       if self.type == "INTERNATIONAL":
 
           if self.cl == "ECONOMY":
               self.cost = 103571
 
           elif self.cl == "PREMIUM ECONOMY":
               self.cost = 207142
 
           elif self.cl == "FIRST":
               self.cost = 791580
 
           elif self.cl == "BUSINESS":
               self.cost = 569642
 
       elif self.type == "DOMESTIC":
 
           if self.cl == "ECONOMY":
               self.cost = 4999
 
           elif self.cl == "PREMIUM ECONOMY":
               self.cost = 5999
 
           elif self.cl == "FIRST":
               self.cost = 8999
 
           elif self.cl == "BUSINESS":
               self.cost = 6999
       else:
           exit()
 
       print("\nThe cost of the travel you have opted costs:", self.cost, "Rupees")
       self.cost = self.cost * count
       print("So your total cost is:", self.cost, "Rupees")
       print("\n")
 
       print("\n")
       print("DUE TO THE HARSH CONDITIONS DURING THIS COVID/19 PANDEMIC WE ACCEPT BANKING, ONLINE PAYMENT PLATFORMS "
             "LIKE GOOGLE PAY, PAYTM, PHONE PE, AND SPECIAL LOYALITY CARDS FROM OUR FIRM")
       print("WE DEARLY EXPECT YOU TO THRIVE THIS CONDITION AS THE SAFETY OF OUR EMPLOYES AND CUSTOMERS IS AT UTMOST "
             "IMPORTANCE !!")
 
       print("Plesase select your payment mode:")
       print("1.BANKING\n2.GOOGLE PAY\n3.PHONE PE\n4.PAYTM\n5.SPECIAL LOYALTY CARD")
       mod = input("Enter the mode/srno. : ").upper()
 
       if mod in ("2", "3", "4", "GOOGLE PAY", "PHONE PE", "PAYTM"):
           p = input("Please enter the phone number corresponding to your Online Payment Portal:")
           print("Please enter this OTP in your Online Payment Portal: ", r.randint(1000, 9999))
           print("Now you may continue the payment on the portal!")
 
           e = int(input("\nAfter finishing you may get an OTP from your Online Payment Portal\nPlease Enter that OTP "
                         "here:"))
           print("YOUR TICKET DETAILS WILL BE DESPLAYED NOW :-->\n\n\n\n")
 
       elif mod == "BANKING" or mod == '1':
           ac_no = int(input("Kindly enter the account number:"))
           spin = int(input("Please enter your special pin/password"))
           print("The payment was successful from the bank account number :", ac_no)
           print("YOUR TICKET DETAILS WILL BE DESPLAYED NOW :-->\n\n\n\n")
 
       elif mod == "5" or mod == "SPECIAL LOYALTY CARD":
           n = input("Please enter the name that your loyalty card addresses:")
           g = int(input("Please enter the corresponding special pin number:"))
           print("YOUR TICKET DETAILS WILL BE DESPLAYED NOW :-->\n\n\n\n")
 
   # definition for displaying ticket
   def ticket(self):
       print("THE TICKET :-->\n")
 
       if self.type == "INTERNATIONAL":
           fl = r.choice(self.name_int)
       else:
           fl = r.choice(self.name_dom)
 
       for i in range(0, len(self.names)):
           print("Passenger ", i + 1, " :-")
           print("NAME:", self.names[i], "\nAGE:", self.age[i], "\nGENDER:", self.gender[i])
           print("\n")
 
       print("FLIGHT: FROM -", self.frm, " TO -", self.to)
       print("FLIGHT NAME:", fl)
       print("TYPE: ", self.type)
       print("CLASS:", self.cl)
       print("COST: ", self.cost)
       print("STATUS : PAID")
 
       with open("database.txt","a") as dat:
           for i in range(1, self.p+1):
               dat.write("AIRPLANE TRIP: ")
               dat.write(self.names[i-1])
               dat.write(", ")
               dat.write(str(self.age[i - 1]))
               dat.write(", ")
               dat.write(self.gender[i - 1])
               dat.write(",From: ")
               dat.write(self.frm)
               dat.write(",To: ")
               dat.write(self.to)
               dat.write(",Flight Name: ")
               dat.write(fl)
               dat.write(",Cost: ")
               dat.write(str(self.cost))
               dat.write(",Class: ")
               dat.write(self.cl)
               dat.write(",Type: ")
               dat.write(self.type)
               dat.write(",Date: ")
               dat.write(self.date)
               dat.write("\n")
 
# creting a class for train transport
class train:
 
   # definition to initialize all values
   def _init_(self, from_train, to_train, train_cost, train_names, train_age, train_gender, train_cl):
       self.frm = from_train
       self.to = to_train
       self.cost = train_cost
       self.names = train_names
       self.age = train_age
       self.gender = train_gender
       self.cl = train_cl
       self.date = None
       self.p = None
 
   # definition to choose trip
   def trip(self):
       self.frm = input("Please enter the departure train station:")
       self.to = input("Please enter the destination train station:")
       self.cl = input("Please enter the train class you want to travel with(AC/NON AC):")
 
       d = input("Do you wish to continue to the detailing counter? (Y/N)").upper()
       if d == "Y":
           pass
       else:
           exit()
 
   # definition for personal details
   def detail(self):
       self.p = int(input("\nSir how many passengers are y'all? :"))
       print("\n")
       self.date = input("Please enter the corresponding date of your travel:")
 
       for i in range(1, self.p + 1):
           name = input("ENTER the name of the passenger:")
           self.names.append(name)
           age = int(input("ENTER the age of the passenger:"))
           self.age.append(age)
           gender = input("ENTER the gender of the passenger:")
           self.gender.append(gender)
 
       print("\n")
 
       c = input("Do you want to continue to the payment panel? (Y/N):").upper()
       if c == "Y":
           pass
       else:
           exit()
 
   # definition for payment algorithms
   def payment(self):
       count = len(self.names)
 
       print("The cost of your train ticket per person costs: 5000 Rupees")
       self.cost = count * 5000
       print("So the total cost of the travel is: ", self.cost)
 
       print("\n")
       print("DUE TO THE HARSH CONDITIONS DURING THIS COVID/19 PANDEMIC WE ACCEPT BANKING, ONLINE PAYMENT PLATFORMS "
             "LIKE GOOGLE PAY, PAYTM, PHONE PE, AND SPECIAL LOYALITY CARDS FROM OUR FIRM")
       print("WE DEARLY EXPECT YOU TO THRIVE THIS CONDITION AS THE SAFETY OF OUR EMPLOYES AND CUSTOMERS IS AT UTMOST "
             "IMPORTANCE !!")
 
       print("Plesase select your payment mode:")
       print("1.BANKING\n2.GOOGLE PAY\n3.PHONE PE\n4.PAYTM\n5.SPECIAL LOYALTY CARD")
       mod = input("Enter the mode/srno. : ").upper()
 
       if mod in ("2", "3", "4", "GOOGLE PAY", "PHONE PE", "PAYTM"):
           p = input("Please enter the phone number corresponding to your Online Payment Portal:")
           print("Please enter this OTP in your Online Payment Portal: ", r.randint(1000, 9999))
           print("Now you may continue the payment on the portal!")
 
           e = int(input("\nAfter finishing you may get an OTP from your Online Payment Portal\nPlease Enter that OTP "
                         "here:"))
           print("YOUR TICKET DETAILS WILL BE DESPLAYED NOW :-->\n\n\n\n")
 
       elif mod == "BANKING" or mod == '1':
           ac_no = int(input("Kindly enter the account number:"))
           spin = int(input("Please enter your special pin/password"))
           print("The payment was successful from the bank account number :", ac_no)
           print("YOUR TICKET DETAILS WILL BE DESPLAYED NOW :-->\n\n\n\n")
 
       elif mod == "5" or mod == "SPECIAL LOYALTY CARD":
           n = input("Please enter the name that your loyalty card addresses:")
           g = int(input("Please enter the corresponding special pin number:"))
           print("YOUR TICKET DETAILS WILL BE DESPLAYED NOW :-->\n\n\n\n")
 
   # definition for displaying ticket
   def ticket(self):
       for i in range(0, len(self.names)):
           print("Passenger ", i + 1, " :-")
           print("NAME:", self.names[i], "\nAGE:", self.age[i], "\nGENDER:", self.gender[i])
           print("\n")
 
       print("TRAIN: FROM -", self.frm, " TO -", self.to)
       print("CLASS:", self.cl)
       print("COST: ", self.cost)
       print("STATUS : PAID")
 
       with open("database.txt","a") as dat:
           for i in range(1, self.p+1):
               dat.write("TRAIN TRIP: ")
               dat.write(self.names[i-1])
               dat.write(", ")
               dat.write(str(self.age[i - 1]))
               dat.write(", ")
               dat.write(self.gender[i - 1])
               dat.write(",From: ")
               dat.write(self.frm)
               dat.write(",To: ")
               dat.write(self.to)
               dat.write(",Class: ")
               dat.write(self.cl)
               dat.write(",Cost: ")
               dat.write(str(self.cost))
               dat.write(",Date: ")
               dat.write(self.date)
               dat.write("\n")
 
 
 
# defining the main definition
def main():
   print("\nWelcome this is the availability checking counter!")
   print("We do intercity (MAHARASHTRA) travels through busses of all classes and comfort!")
   print("We do international as well as domestic air travels of all classes and comfort!")
   print("We do interstate train travels of all classes and comfort!")
 
   mot = input("Which mode of transport would you like to travel with:\n1.BUS\n2.AIRPLANE\n3.TRAIN\nENTER CHOICE:")
   print("\n")
   if mot == "BUS" or mot == "1":
       y = bus(None, None, None, [], [], [],
               {"MONDAY": ["MUMBAI", "PUNE", 250, 300], "TUESDAY": ["MUMBAI", "GOA", 550, 650],
                "WEDNESDAY": ["MUMBAI", "MAHABALESHWAR", 425, 550], "SATURDAY": ["MUMBAI", "LONAVALA", 400, 420],
                "SUNDAY": ["MUMBAI", "ALIBAUG", 200, 250]})
       y.TRIPS()
       y.details()
       y.payment()
       y.ticket()
 
   elif mot == "2" or mot == "AIRPLANE":
       z = airplane(None, None, None, None, None, [], [], [],
                    ["Qatar Airways", "Singapore Airlines", "All Nippon Airways", "Cathay Pacific Airways"],
                    ["Air India", "Indigo", "Vistara", "AirAsia"])
       z.trip()
       z.detail()
       z.payment()
       z.ticket()
 
   elif mot == "3" or mot == "TRAIN":
       v = train(None, None, None, [], [], [], None)
       v.trip()
       v.detail()
       v.payment()
       v.ticket()
 
# calling the main definition
main()