import smtplib

gmail_user = "lufu.family@gmail.com"
gmail_pwd = "242familyacc"
FROM = "lufu.family@gmail.com"
TO = "sunny.lu.sl@gmail.com"
SUBJECT = "test"
TEXT = "test"

# Prepare actual message
message = """From: %s\nTo: %s\nSubject: %s\n\n%s
""" % (FROM, ", ".join(TO), SUBJECT, TEXT)
try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_user, gmail_pwd)
    server.sendmail(FROM, TO, message)
    server.close()
    print('successfully sent the mail')
except:
    print("failed to send mail")