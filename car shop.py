import pyodbc

server = 'LAPTOP-UD384DN9\SQLEXPRESS' 
database = 'car shop' 
username = ''
password = '' 
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

def values(var):
    cursor.execute("SELECT * FROM " + var)
    
    row = cursor.fetchone()
    while row:
        print(row[0], '-', row [1])
        row = cursor.fetchone()
        
def choice(var):
    choose = 1

    while choose == 1:
        print("\nSelect number of the " + var + " from list (if you would like to choose 'any' enter '0'): ")
        values(var)
        ch = input('\nYour choice: ')
        
        cursor.execute("SELECT COUNT(id) FROM " + var)
        row = cursor.fetchone()

        if (int(ch) in range(1, row[0], 1)):
            return ('= ' + ch)
            
        elif ch == '0':
            return 'BETWEEN 1 AND ' + str(row[0])
            
        else:
            print("\nSorry, you entered an incorrect value! Please, try again!")
            
print("\nWelcome you to our car shop!")

brand = choice('brand')
type_ = choice('type')
engine = choice('engine')
transm = choice('transm')
kit = choice('kit')
 
cursor.execute('''
    SELECT c.name, s.name, b.name, t.name, e.name, tr.name, k.name 
    FROM car c, status s, brand b, type t, engine e, transm tr, kit k
    WHERE c.fkey_status = s.id
    AND c.fkey_brand = b.id
    AND c.fkey_type = t.id
    AND c.fkey_engine = e.id
    AND c.fkey_transm = tr.id
    AND c.fkey_kit = k.id
    AND b.id ''' + brand +
    ''' AND t.id ''' + type_ +
    ''' AND e.id ''' + engine +
    ''' AND tr.id ''' + transm +
    ''' AND k.id ''' + kit)

row = cursor.fetchone()

if row:
    print("\nSo, that's what we can offer you:")
         
    while row:
        print('\n' + row[0], '\nStatus:', row[1], '\nCharacteristics:', row[3], row[4], row[5], row[6])
        row = cursor.fetchone()
else:
     print("\nSorry, but we can't find anything according to your requests")
