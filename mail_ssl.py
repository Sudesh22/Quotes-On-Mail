import smtplib, datetime, time, requests
from email.message import EmailMessage
from api_class import *

SENDER_EMAIL_ADDRESS = 'sender-email-address'
SENDER_EMAIL_PASSWORD = 'sender-password'
RECEIVER_EMAIL_ADDRESS = 'receiver-email-address'

ssl_port = 465
smtp_server = 'smtp.gmail.com'

while(1):
    date = datetime.datetime.strftime(datetime.datetime.now(), '%H:%M:%S')
    if date == "09:00:00":
        try: 

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

            msg = EmailMessage()
            msg['Subject'] = 'Quote of the Day!'
            msg['From'] = EMAIL_ADDRESS
            msg['To'] = RECEIVER_EMAIL_ADDRESS
            msg.set_content(content, subtype='html')
            
            with smtplib.SMTP_SSL(smtp_server, ssl_port) as smtp:
                smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                smtp.send_message(msg)
            print ("Email sent successfully!") 
                
        except Exception as excp: 
            print("Something went wrong....",excp)
    time.sleep(1)
