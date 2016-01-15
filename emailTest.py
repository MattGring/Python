def send_email():
            import smtplib

            gmail_user = "gring.matt@gmail.com"
            gmail_pwd = "6shadow1"
            FROM = 'gring.matt@gmail.com'
            TO = ['gring.matt@gmail.com'] #must be a list
            SUBJECT = "Testing sending using gmail"
            TEXT = "Testing sending mail using gmail servers"

            # Prepare actual message
            message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
            """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
            try:
                #server = smtplib.SMTP(SERVER) 
                server = smtplib.SMTP("smtp.gmail.com", 587) #or port 465 doesn't seem to work!
                server.ehlo()
                print("server.ehlo() has run")
                server.starttls()
                print("server.starttls() has run")
                server.login(gmail_user, gmail_pwd)
                print("attempted login...")
                server.sendmail(FROM, TO, message)
                print("attempted server.sendmail()")
                #server.quit()
                server.close()
                print("successfully sent the mail")
            except:
                print("failed to send mail")

send_email()
