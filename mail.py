import smtplib
server = smtplib.SMTP('smtp.gmail.com',587)

server.starttls()

server.login('laluyadavyadav717@gmail.com', 'ivws clno oaap jfwx')

server.sendmail('laluyadavyadav717@gmail.com', 'rohitprajapat171202@gmail.com', 'fall detected')
print('mail sent')
