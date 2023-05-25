import smtplib, datetime, time, requests
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from api_class import *

Sender_Email = "sender-email-address"
Sender_Password = "sender-password"
Receiver_Email = "receiver-email-address"

tls_Port = 587
smtp_server = 'smtp.gmail.com'


while(1):
    date = datetime.datetime.strftime(datetime.datetime.now(), '%H:%M:%S')
    if date == "09:00:00":
        try: 
            smtp = smtplib.SMTP(smtp_server, tls_Port) 

            smtp.starttls() 

            smtp.login(Sender_Email,Sender_Password)

            api_call = CallAPI("http://192.168.0.105:5000/quote")

            content = '''
                        <!DOCTYPE html>
                        <html>
                        <head>
                            <link rel="stylesheet" type="text/css" hs-webfonts="true" href="https://fonts.googleapis.com/css?family=Lato|Lato:i,b,bi">
                            <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1.0">
                            <style type="text/css">

                            @import url(https://fonts.googleapis.com/css?family=Open+Sans:400italic);
                            .otro-blockquote{
                            font-size: 1.4em;
                            width:60%;
                            margin:50px auto;
                            font-family:Open Sans;
                            font-style:italic;
                            color: #555555;
                            padding:1.2em 30px 1.2em 75px;
                            border-left:8px solid #78C0A8 ;
                            line-height:1.6;
                            position: relative;
                            background:#EDEDED;
                            }

                            .otro-blockquote::before{
                            font-family:Arial;
                            
                            color:#78C0A8;
                            font-size:4em;
                            position: absolute;
                            left: 10px;
                            top:-10px;
                            }

                            .otro-blockquote::after{
                            
                            }

                            .otro-blockquote span{
                            display:block;
                            color:#333333;
                            font-style: normal;
                            font-weight: bold;
                            margin-top:1em;
                            }
                                    </style>
                                </head>
                                <body>
                            <blockquote class="otro-blockquote">
                            
                            '''+api_call.quote+'''
                            <span>'''+api_call.author+'''</span>
                            </blockquote>
                                </body>
                                </html>
                    '''

            message = MIMEMultipart("alternative")
            message["Subject"] = "Quote of the Day!"
            message["From"] = Sender_Email
            message["To"] = Receiver_Email

            part1 = MIMEText(content, "html")

            message.attach(part1)

            smtp.sendmail(Sender_Email, Receiver_Email, str(message)) 

            smtp.quit() 
            print ("Email sent successfully!") 

        except Exception as excp:   
            print("Something went wrong....",excp)
    time.sleep(1)