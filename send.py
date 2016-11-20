import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
 
fromaddr = "edi4"
toaddr = "edi3"
 
msg = MIMEMultipart()
 
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Happy Emails"
 
body = "You success"
 
msg.attach(MIMEText(body, 'plain'))
filename1 = "edit1.txt" 
filename = "/home/edit1/Public/.fol/log"
attachment = open(filename, "rb")
 
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename1)
 
msg.attach(part)
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "edit2")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
