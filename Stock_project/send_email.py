import os
import sqlite3
from nsetools import Nse
from pprint import pprint
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart 
from jinja2 import Template, Environment, FileSystemLoader



#file = os.path.dirname(os.path.abspath(__filename__)) + 'db.sqlite3'
with sqlite3.connect('db.sqlite3') as conn:
    c = conn.cursor()
    for rows in c.execute('SELECT * FROM smt_trails'):
        email_id = rows[1]
        stocks = rows[2]
        first_char = stocks.replace('[', '')
        second_char = first_char.replace(']', '')
        third_stocks = second_char.replace("'", '')
        final_stocks = third_stocks.replace(" ", '')
        stock_arr = final_stocks.split(',')


        nse = Nse()
        company_name = []
        open_price = []
        last_price = []
        high_52 = []
        low_52 = []
        avg_price = []

        for stock in stock_arr:
            q = nse.get_quote(stock)
            if q != None:
                company_name.append(q['companyName'])
                open_price.append(q['open'])
                last_price.append(q['lastPrice'])
                high_52.append(q['high52'])
                low_52.append(q['low52'])
                avg_price.append(q['averagePrice'])
        with smtplib.SMTP('smtp.gmail.com', 587) as s:
            from_email = "smitgol007@gmail.com"
            to_email = email_id
            msg = MIMEMultipart()
            msg['From'] = from_email
            msg['To'] = to_email
            msg['Subject'] = "Your Stock Information"


            file_loader = FileSystemLoader('templates')
            env = Environment(loader=file_loader)
            template = env.get_template('EMAIL.html')

            data = zip(company_name, open_price, last_price, high_52, low_52, avg_price)
            tem = template.render(company_data=data)
            msg.attach(MIMEText(tem, 'html'))
            text = msg.as_string()

            s.starttls()
            s.login('smitgol007@gmail.com', 'smitsmit9825397527')
            message = "Hii"
            s.sendmail("smitgol007@gmail.com", email_id, text)
            print("Done!!")

        

