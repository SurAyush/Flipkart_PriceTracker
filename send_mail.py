import smtplib

def send_mail_func(product,price,url,threshold):
    Sender_email = "avisinghal627@gmail.com"
    reciever_email = "ayushsur26@gmail.com"
    subject = f"Exciting News: Price Drop Alert for {product}!"
    text = f"Dear Valued Customer,\n We hope this message finds you well. We're delighted to inform you of some fantastic news regarding the product you've shown interest in, {product}.\nAs per your request, we've been closely monitoring the pricing for the product and are thrilled to announce that there has been a significant drop in its price! The current price has fallen below the threshold price of {threshold}, which you provided to us earlier.\nYou can take advantage of this price drop by visiting the following link: {url} \nWe understand how important it is to get the best value for your money, and we're thrilled to be able to offer you this reduced price on {product}.\nThank you for choosing us for your needs. We look forward to serving you again soon!"
    message = f"Subject : {subject}\n\n{text}"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(Sender_email, "eqvcevttodervvfe")
    server.sendmail(Sender_email, reciever_email, message)
    print("Email has been sent to " + reciever_email)