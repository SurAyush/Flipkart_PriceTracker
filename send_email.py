import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

# Input email details
def send_email_func(product,price,url,threshold,imgname,receiver):
    sender_email = "projectworksnit@gmail.com"
    receiver_email = receiver
    subject = f"Exciting News: Price Drop Alert for {product}!"
    text = f"Dear Valued Customer,\n We hope this message finds you well. We're delighted to inform you of some fantastic news regarding the product you've shown interest in, {product}.\nAs per your request, we've been closely monitoring the pricing for the product and are thrilled to announce that there has been a significant drop in its price! The current price has fallen below the threshold price of {threshold}, which you provided to us earlier.\nNew price: {price}\nYou can take advantage of this price drop by visiting the following link: {url} \nWe understand how important it is to get the best value for your money, and we're thrilled to be able to offer you this reduced price on {product}.\nThank you for choosing us for your needs. We look forward to serving you again soon!"
    img_location = f"{imgname}.png"

    # Create a multipart message
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject

    # Attach the text message
    message.attach(MIMEText(text, 'plain'))

    # Attach the image file
    with open(img_location, 'rb') as f:
        img = MIMEImage(f.read())
        img.add_header('Content-Disposition', 'attachment', filename=img_location)
        message.attach(img)

    # Connect to the SMTP server
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, "sdujytqxxpvuwpoe")  # Use the actual sender's password here
        server.send_message(message)

    print("Email has been sent to " + receiver_email)

# send_email_func("Test",198,"www.google.com",200,"commodity_price_variation")