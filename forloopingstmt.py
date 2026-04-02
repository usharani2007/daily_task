banking={78005:"usha",67890:"shyam",67890:"pavani",987654:"suraj",897543:"ankith"}
user="admin"
password="admin@123"
login_name=input("entre the employe name:")
pasword=input("ente the password:")

if (login_name == user) and (pasword == pasword):
      print("login sucessfully....")
      account=input("entre the account number:")
      for x in banking:
            if x == account:
                      print("account number:",x,"name:",banking[x])
else:
   print("invaild  user & pasword")
