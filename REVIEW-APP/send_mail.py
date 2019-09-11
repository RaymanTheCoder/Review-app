import smtplib
from email.mime.text import MIMEText


def send_mail(customer, dealer, rating, comments):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = '3a4b54d3402a51'
    password = '4953f271ab847a'
    message = f"<h3>New Feedback Submission</h3><ul><li>Customer: {customer} </li><li>Dealer: {dealer} </li><li>Rating: {rating} </li><li>Comments: {comments} </li></ul>"
    
    sender_email = 'email@example.com'
    receiver_email = 'email2@example.com'
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Lexus Feedback'
    msg['Form'] = sender_email
    msg['To'] = receiver_email

    #Send mail
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())