import smtplib
import email.message
import email.utils


def send_email(send_from, send_to):

    msg = email.message.Message()
    msg['From'] = send_from
    msg['To'] = send_to
    msg['Subject'] = "Python E-mail Subject"
    msg.add_header('Content-Type', 'text')
    msg.set_payload("This message brought to you by Python and Eric. \n \n We can now use python to send email notifications.")

    smtp_obj = smtplib.SMTP("smtpapp.gavilon.com")
    smtp_obj.sendmail(msg['From'], [msg['To']], msg.as_string())
    smtp_obj.quit()

#These lines are not needed.  They are only here to test the send mail func.
#Remove them before implementing, but this shows the format for calling this function.
send_email("eric.carstensen@gavilon.com", "imjacksdad@gmail.com,")
send_email("imjacksdad@gmail.com,", "eric.carstensen@gavilon.com")
