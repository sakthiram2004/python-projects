class Account:
    def __init__(self,accnumber,balance):
        self._accnumber = accnumber
        self._balance   = balance

class SBAccount(Account):
    def __init__(self,accnumber,balance):
        super().__init__(accnumber,balance)
        print("SBAccount is opened with the account balance of ",self._balance,"is created")
    def deposit(self,amount):
        if amount>0:
            self._balance = self._balance + amount
            print("New Balance = ",self._balance)
        else:
            print("Invalid amount")
    def withdraw(self,amount):
        if self._balance - amount > 1000:
            self._balance = self._balance-amount
            print("New Balance =",self._balance)
        else:
            print("Insufficient balance")
    def calc_interest(self):
        self._balance = self._balance+self._balance*0.04
        print("New Balance = ",self._balance)

class FDAccount(Account):
    def __init__(self,accnumber,period,balance):
        super().__init__(accnumber,balance)
        self.period = period
        print("FDAccount is opened with the account balance of ",self._balance,"is created")
    def calc_interest(self):
        return self._balance*0.0825*self.period
   
    def close(self):
         self._balance = self.calc_interest()+self._balance
         print("Maturity amount = ",self._balance)

class Customer:
    sbaccno = 1000
    fdaccno = 2002
    def __init__(self,cust_id,name,address):
        self.cust_id = cust_id
        self.name = name
        self.address = address
    def createAccount(self,type):
        if type == 1:
            bal = float(input('Enter Initial amount to open SB account :'))
            self.sb = SBAccount(Customer.sbaccno,bal)
            Customer.sbaccno += 1
        else:
            period = int(input('Enter Period for FD : '))
            bal = float(input('Enter Initial amount to deposit FD account :'))
            self.fd = FDAccount(Customer.fdaccno,period,bal)
            Customer.fdaccno += 1
    def transaction(self,type):
        if type == 1:
            amt = float(input('Enter amount to deposit in SB account : '))
            self.sb.deposit(amt)
        elif type == 2:
            amt = float(input('Enter amount to withdraw in SB account : '))
            self.sb.withdraw(amt)
        elif type ==3:
            self.sb.calc_interest()
        elif type == 4:
            self.fd.close()
        else:
            print("Invalid Choice")


if __name__ == '__main__':
    c = []
    i = 0

    while True:
        print("**************************")
        print("Create new Account -----> 1")
        print("Existing Account -----> 2")
        print("Exit -----> 3")
        print("**************************")
       
        ch1 = int(input("Enter your choice : "))
        match(ch1):
            case 1:
                while True:
                    print("**************************")
                    print("SBAccount-----> 1")
                    print("FDAccount -----> 2")
                    print("Exit -----> 3")
                    print("**************************")
                    ch2 = int(input("Enter Your choice : "))
                    if ch2 == 1 or ch2 == 2:
                        name = input("Enter name : ")
                        address = input("Enter address : ")
                        c.append(Customer(i,name,address))
                        c[i].createAccount(ch2)
                        i += 1
                    elif ch2 == 3:
                        break
                    else:
                        print('Invalid choice')
            case 2:
                while True:
                    print("**************************")
                    print("SBAccount-----> 1")
                    print("FDAccount -----> 2")
                    print("Exit -----> 3")
                    print("**************************")
                    ch2 = int(input("Enter Your choice : "))
                    if ch2 == 1 or ch2 == 2 or ch2 == 3:
                       
                       
                        match(ch2):
                            case 1:
                                print("**************************")
                                print('Deposit ------ > 1')
                                print('Withdraw ----- > 2')
                                print('Cal Interest --> 3')
                                print('Exit ------> 4')
                                print("**************************")
                                ch3 = int(input('Enter ur choice : '))
                                match(ch3):
                                    case 1:
                                        cid = int(input('Enter Customer Id : '))
                                        c[cid].transaction(1)
                                    case 2:
                                        cid = int(input('Enter Customer Id : '))
                                        c[cid].transaction(2)
                                    case 3:
                                        cid = int(input('Enter Customer Id : '))
                                        c[cid].transaction(3)
                                    case 4:
                                        break
                            case 2:
                                cid = int(input('Enter Customer Id : '))
                                c[cid].transaction(4)
                            case 3:
                                break
                    else:
                        #print("\t**************************")
                        print("*****Enter valid choice*****")
            case 3:
                break

           
