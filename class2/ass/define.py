import pymysql.cursors
import csv


appli_data = pymysql.connect(host='localhost', 
                    user='root', 
                    password='', 
                    db='app_data', 
                    charset='utf8mb4', 
                    cursorclass=pymysql.cursors.DictCursor)

def create_table():

    try:
        with appli_data.cursor() as cursor:
            # create new table
            sql = "CREATE TABLE application_data (id INT(3) PRIMARY KEY NOT NULL AUTO_INCREMENT, customerID VARCHAR(12), loanID VARCHAR(15), applicationDate VARCHAR(11), LoanNumber INT(3), loanAmount INT(6), interestRate DECIMAL(3,1), TermDays INT(3), repaymentDuedate VARCHAR(11), repaymentPaidDate VARCHAR(11));"
            
            cursor.execute(sql)
        
        appli_data.commit()
    
    finally:
        appli_data.close()
        print('Successful')

def add_data():

    try:
        with appli_data.cursor() as cursor:
            #read a single record
            fname = 'application_data.csv'

            with open(fname) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                for row in csv_reader:
                    print(row)
                    customerID=row[0]
                    loanID=row[1]
                    applicationDate=row[2]
                    LoanNumber=row[3]
                    loanAmount=row[4]
                    interestRate=row[5]
                    TermDays=row[6]
                    repaymentDuedate=row[7]
                    repaymentPaidDate=row[8]
                    cursor.execute(f"INSERT INTO application_data (customerID, loanID, applicationDate, LoanNumber, loanAmount, interestRate, TermDays, repaymentDuedate, repaymentPaidDate) VALUES ('{customerID}', '{loanID}', '{applicationDate}', '{LoanNumber}', '{loanAmount}', '{interestRate}', '{TermDays}', '{repaymentDuedate}', '{repaymentPaidDate}');")


        appli_data.commit()
    finally:
        print("Successfully Added Data...!!")
        appli_data.close()