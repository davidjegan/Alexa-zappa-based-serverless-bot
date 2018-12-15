#Author name: David Jegan Abishek
#Mail ID: mailtodavidjegan@gmail.com
#Github: @davidjegan

import sys
import json
import boto3
import smtplib
from flask import Flask
from email import encoders
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email.MIMEMultipart import MIMEMultipart
from flask_ask import Ask, statement, question
from boto3.dynamodb.conditions import Key, Attr
#imported packages

#connect to AWS services
region_value = 'us-east-1'
dynamodb = boto3.resource('dynamodb', region_name=region_value)
s3 = boto3.resource('s3', region_name=region_value)
dynamodbclient = boto3.client('dynamodb', region_name=region_value)
table = dynamodb.Table('Insert your dynamodb name here')
codeflag = 'True'

#init flask app
app = Flask(__name__)
ask = Ask(app, "/")

#All intents are based on Zappa and Flask-ask
#The intents are initialized and the method is called
#Contents from the DynamoDB is called with error check 

#initialization intent
@ask.launch
def hello():
    msg = 'getname'
    #intent name is parsed and contents from the DB are validated
    if(table.get_item(Key={'partkey': msg})):
        codeflag = 'True'
        response = table.get_item(Key={'partkey': 'getname'})
        if(int(response['ResponseMetadata']['HTTPHeaders']['content-length']) < 3):
            codeflag = 'False'
            #Dynamodb lookup has failed
        if(codeflag == 'True'):
            item = response['Item']
            for key, value in item.items():
                if(key == 'answer'):
                    sol = value
                    #return solution
    return question(sol)


#example to process based on the user input
@ask.intent("NameIntent", convert={'firstname': str})
def answer(firstname):
    msg = 'savename'
    #intent name is parsed and contents from the DB are validated
    if(table.get_item(Key={'partkey': msg})):
        codeflag = 'True'
        response = table.get_item(Key={'partkey': 'savename'})
        if(int(response['ResponseMetadata']['HTTPHeaders']['content-length']) < 3):
            codeflag = 'False'
            #Dynamodb lookup has failed
        if(codeflag == 'True'):
            item = response['Item']
            for key, value in item.items():
                if(key == 'answer'):
                    sol = value
                    #return solution
    return question(sol)


#example for static response from an intent
@ask.intent("MethodAIntent")
def answer():
    msg = 'methodaans'
    if(table.get_item(Key={'partkey': msg})):
        codeflag = 'True'
        response = table.get_item(Key={'partkey': 'methodaans'})
        if(int(response['ResponseMetadata']['HTTPHeaders']['content-length']) < 3):
            codeflag = 'False'
            #Dynamodb lookup has failed
        if(codeflag == 'True'):
            item = response['Item']
            for key, value in item.items():
                if(key == 'answer'):
                    sol = value
                    #return solution
    return question(sol)

#example for SMTP mailer intent
@ask.intent("MailIntent")
def answer():
    #mailing part
    msg = MIMEMultipart()
    msg['From'] = 'sender@gmail.com'
    msg['To'] = 'receiver@gmail.com'
    msg['Subject'] = "Insert Subject here"
    body = "Insert Message here"
    msg.attach(MIMEText(body, 'plain'))
    #import image from s3 bucket
    filename = 'demo.jpg'
    s3.meta.client.download_file('my.raw.bucket', filename, '/tmp/demo.jpg')
    attachment = open('/tmp/demo.jpg', 'rb')
    #create parts for sending the mail
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename= %s' % filename)
    msg.attach(part)
    #SMTP details
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, 'yourpwd')
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    msg = 'mailans'
    if(table.get_item(Key={'partkey': msg})):
        codeflag = 'True'
        response = table.get_item(Key={'partkey': 'mailans'})
        if(int(response['ResponseMetadata']['HTTPHeaders']['content-length']) < 3):
            codeflag = 'False'
        if(codeflag == 'True'):
            item = response['Item']
            for key, value in item.items():
                if(key == 'answer'):
                    sol = value
    return question(sol)

#exit intent
@ask.intent("ExitIntent")
def answer():
    msg = 'exitname'
    if(table.get_item(Key={'partkey': msg})):
        codeflag = 'True'
        response = table.get_item(Key={'partkey': 'exitname'})
        if(int(response['ResponseMetadata']['HTTPHeaders']['content-length']) < 3):
            codeflag = 'False'
        if(codeflag == 'True'):
            item = response['Item']
            for key, value in item.items():
                if(key == 'answer'):
                    sol = value
    return statement(sol)