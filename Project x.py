# Banking Sector
import time
class Andhra_Bank:
    def ATM_Machine(self):
        f = open("Account_book.txt",'w')
        e = ("5699\n","1122\n","1234\n","123456\n","5633\n","7899\n")
        f.writelines(e)
        f.close
        print("WELCOMETO ANDHRA BANK ATM")
        print()
        print("Please_insert_your_card and do_not_remove_your_card")
        print()
        ATM_Pin = input("Enter the your pin : ")
        for i in e:
            if ATM_Pin in i:
                Renter_pin = input("Renter the pin : ")
                if ATM_Pin == Renter_pin:
                    print()
                    print("Welcome to Andhra Bank ATM Machine Services")
                    print()
                    Balance = 1000
                    services_all = input("Please select the services : ")
                    if services_all == "Deposit" :
                        Amount = int(input("Please insert the cash in hub : "))
                        Denotes = int(input("Please enter the 500 denotes : "))
                        Denotes_1 = int(input("Please enter the 200 denotes : "))
                        Denotes_2 = int(input("Please enter the 100 denotes :"))
                        Balance += Denotes * 500
                        Balance += Denotes_1 * 200
                        Balance += Denotes_2 * 100
                        print("Your deposited amount is : ",Amount)
                        print("Your account balance is : ",Balance)
                    elif services_all == "Withdraw":
                        Amount = int(input("Please Enter the Withdraw cash : "))
                        Balance-= Amount
                        print("Your Withdraw amount is : ",Amount)
                        print("Your account balance is : ",Balance)
                    elif services_all == "Mini_Statement":
                        print("Your Accont Statement from last three months is",Balance)
                    elif services_all == "Pin_Change":
                        Old_pin = input("Please enter the your pin : ")
                        if ATM_Pin == Old_pin:
                            New_pin = input("Please Enter Your new pin")
                            print()
                            Rpin = input("Please Renter you new pin : ")
                            if New_pin == Rpin:
                                print("Your Pin has Changed Sucessfully")
                            else:
                                print("You Entered worng pin")
                        else:
                            print("You Entered worng pin")
                    elif services_all == "Aadhaar Verification":
                        Aadhaar_no = input("Please enter the your 12 digit Aadhaar No : ")
                        Raadhaar_no = input("Please Renter the your 12 digit Aadhaar No : ")
                        if Aadhaar_no == Raadhaar_no:
                            print("Please wait a minute we are updating your aadhaar")
                            time.sleep(5)
                            print("Your Aadhaar updated sucess fully")
                    elif services_all == "Passbook_printing":
                        print("Please insert your passbook in the Machine and open last updated page")
                        time.sleep(2)
                        print("Please wait untill your passbook is printing")
                        time.sleep(5)
                        print("Your Passbook printing done Susess fully")
                    else:
                        print("In_valid_Operation")
                else:
                    print("In_Valid_pin_your_Entered")
Smart_services = Andhra_Bank()
Smart_services.ATM_Machine()
