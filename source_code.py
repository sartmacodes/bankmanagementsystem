import mysql.connector

mydb = mysql.connector.connect(
host="sql6.freesqldatabase.com",
user="sql6471020",
password="XRlQ5Fdq3u",
database = "sql6471020"
)

print(mydb)
mycursor = mydb.cursor()

# mycursor.execute('CREATE TABLE ACCOUNT(name varchar(20), mobile int, type int, acnum int, balance int, city varchar(10))')

def Main():
  input('Press any key to go to main menu')

def Insert():
  mycursor.execute('SELECT acnum FROM ACCOUNT ORDER BY  acnum ASC')
  acc = mycursor.fetchall()[-1][0]
  cmd = 'INSERT INTO ACCOUNT VALUES(%s,%s,%s,%s,%s,%s)'
  rec = []
  while True:
    name = input('Name: ')
    mob = int(input('Mobile Number: '))
    accn = acc
    acc += 1
    actype = int(input("Type: "))
    city = input('City: ')
    bal = float(input('Balance: '))
    rec.append(tuple([name, mob, actype, accn, bal, city]))

    out = input('Enter more records?(Y/N): ')
    if out.lower() == 'y':
      continue
    else:
      break
  mycursor.executemany(cmd, rec)
  mydb.commit()
  print('-'*15)
  Main()

def Search():
  accn = int(input('Enter account number: '))
  cmd = f'SELECT * FROM ACCOUNT WHERE acnum={accn}'
  mycursor.execute(cmd)
  result = mycursor.fetchall()
  if result:
    print(f'''Name: {result[0][0]}
Mobile: {result[0][1]}
Type: {result[0][2]}
Account Number: {result[0][3]}
Balance: {result[0][4]}
City: {result[0][5]}''')
    print('-'*15)
    Main()
  else:
    print('DETAILS NOT FOUND')
    Main()
  mydb.commit() 
  print('-'*15)

def Delete():
  accn = int(input("Account Number to Delete: "))
  cmdin = f'SELECT balance FROM ACCOUNT WHERE acnum = {accn}'
  mycursor.execute(cmdin)
  out = mycursor.fetchall()
  cmd = f'DELETE FROM ACCOUNT WHERE acnum = {accn}'
  if out:
    mycursor.execute(cmd)
    print(f'ACCOUNT: {accn} DELETED WITH BALANCE: {out[0][0]}')
    Main()
  else:
    print('ACCOUNT NOT FOUND')
    Main()
  mydb.commit()
  print('-'*15)

def Modify():
  accn = int(input("Account Number to Modify: "))

  cmd = f'SELECT * FROM ACCOUNT WHERE acnum={accn}'
  mycursor.execute(cmd)
  result = mycursor.fetchall()

  if result:
    print('CURRENT DETAILS:')
    print(f'''Name: {result[0][0]}
Mobile: {result[0][1]}
Type: {result[0][2]}
Account Number: {result[0][3]}
Balance: {result[0][4]}
City: {result[0][5]}''')
    print('-'*15)

    nameinp = input('Change Name(Y/N): ')
    if nameinp.lower() == 'y':
      newname = str(input('Enter Name: '))
      cmd = f"UPDATE ACCOUNT SET name='{newname}' where acnum={accn}"
      mycursor.execute(cmd)
      print('UPDATED')

    mobinp = input('Change Mobile Number(Y/N): ')
    if mobinp.lower() == 'y':
      newmob = int(input('Enter Mobile Number:'))
      cmd = f'UPDATE ACCOUNT SET mobile={newmob} where mobile={result[0][1]}'
      mycursor.execute(cmd)
      print('UPDATED')

    cityinp = input('Change City(Y/N): ')
    if cityinp.lower() == 'y':
      newcity = input('Enter City:')
      cmd = f"UPDATE ACCOUNT SET city='{newcity}' where acnum={accn}"
      mycursor.execute(cmd)
      print('UPDATED')

    typeinp = input('Change Account Type(Y/N): ')
    if typeinp.lower() == 'y':
      newtype = int(input('Enter Account Type:'))
      cmd = f'UPDATE ACCOUNT SET type={newtype} where type={result[0][2]}'
      mycursor.execute(cmd)
      print('UPDATED')
    
    Main()

  else:
    print('ACCOUNT NOT FOUND')
    Main()
  mydb.commit()
  print('-'*15)

def Debit():
  accn = int(input("Account Number to withdraw from: "))
  cmdin = f'SELECT balance FROM ACCOUNT WHERE acnum = {accn}'
  mycursor.execute(cmdin)
  out = mycursor.fetchall()
  if out:
    bal = out[0][0]
    amt = int(input('Amount to withdraw: '))
    if amt < bal:
      new_amt = bal - amt

      cmd = f'UPDATE ACCOUNT SET balance={new_amt} where acnum={accn}'
      mycursor.execute(cmd)
      print(f'UPDATED BALANCE: {new_amt}')
      Main()
    else:
      print('INSUFFICIENT BALANCE')
      Main()
  else:
    print('ACCOUNT NOT FOUND')
    Main()
  mydb.commit()
  print('-'*15)

def Credit():
  accn = int(input("Account Number to credit: "))
  cmdin = f'SELECT balance FROM ACCOUNT WHERE acnum = {accn}'
  mycursor.execute(cmdin)
  out = mycursor.fetchall()
  if out:
    bal = out[0][0]
    amt = int(input('Amount to credit: '))
    new_amt = bal + amt

    cmd = f'UPDATE ACCOUNT SET balance={new_amt} where acnum={accn}'
    mycursor.execute(cmd)
    print(f'UPDATED BALANCE: {new_amt}')
    Main()
  else:
    print('ACCOUNT NOT FOUND')
    Main()
  mydb.commit()
  print('-'*15)

def Sort():
  basis = input('Sort on basis of(Account/Balance/Name): ')
  if basis.lower() == 'account':
    cmd = 'SELECT * FROM ACCOUNT ORDER BY acnum ASC'
    mycursor.execute(cmd)
    res = mycursor.fetchall()
    for i in res:
      print(i)
    print('-'*15)
    Main()

  if basis.lower() == 'balance':
    cmd = 'SELECT * FROM ACCOUNT ORDER BY balance ASC'
    mycursor.execute(cmd)
    res = mycursor.fetchall()
    for i in res:
      print(i)
    print('-'*15)
    Main()
  
  if basis.lower() == 'name':
    cmd = 'SELECT * FROM ACCOUNT ORDER BY name ASC'
    mycursor.execute(cmd)
    res = mycursor.fetchall()
    for i in res:
      print(i)
    print('-'*15)
    Main()

def Div():
  print('-'*15)

while True:
  print('''Commands:
create: To Create Account
search: To Search for Account
debit: To withdraw
credit: To credit
modify: To modify details
remove: To remove Account
sort: a-On basis of account number
      b-On basis of balance
      c-On basis of name
quit: To quit''')

  print('-'*15)

  cmd = input('Enter command: ')

  if cmd.lower() == 'create':
    Insert()
    Div()

  if cmd.lower() == 'search':
    Search()
    Div()

  if cmd.lower() == 'debit':
    Debit()
    Div()

  if cmd.lower() == 'credit':
    Credit()
    Div()

  if cmd.lower() == 'modify':
    Modify()
    Div()

  if cmd.lower() == 'remove':
    Delete()
    Div()
  
  if cmd.lower() == 'sort':
    Sort()
    Div()

  if cmd.lower() == 'quit':
    print('PROGRAM CLOSED')
    Div()
    break
    





