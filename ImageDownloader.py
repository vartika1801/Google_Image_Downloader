import streamlit as st
from icrawler.builtin import GoogleImageCrawler
import os
from pathlib import Path
import zipfile
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# Email sending function
def send_email_with_attachment(receiver_email, attachment_path):
    sender_email = "achaudhary_be22@thapar.edu"  # Replace with your email
    sender_password = "dmie jfpm lnnm jkkt"  # Replace with your app-specific password

    # Create a multipart message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "Your Requested Images"

    # Attach the file to the email
    with open(attachment_path, 'rb') as file:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(file.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(attachment_path)}')
        msg.attach(part)

    # Sending the email via SMTP
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, sender_password)
            server.send_message(msg)
        return True
    except Exception as e:
        return str(e)


st.title('Google Image Downloader and Emailer')

# User inputs
keyword = st.text_input("Enter the keyword for images:", value="beautiful landscapes")
num_images = st.number_input("Enter the number of images to download:", min_value=1, value=10, step=1)
user_email = st.text_input("Enter your email address:")

# Directory to save images in Downloads
downloads_dir = str(Path.home() / "Downloads")
save_dir = os.path.join(downloads_dir, 'downloaded_images')

# When the "Download and Send" button is clicked
if st.button("Download and Send Email"):
    try:
        # Ensure the email field is not empty
        if not user_email:
            st.error("Please enter your email address.")
        else:
            # Check if the save directory exists, if not create it
            if not os.path.exists(save_dir):
                os.makedirs(save_dir)

            # Initialize the GoogleImageCrawler with storage location
            google_crawler = GoogleImageCrawler(storage={'root_dir': save_dir})

            # Start the crawling process
            with st.spinner(f"Downloading {num_images} images for '{keyword}'..."):
                google_crawler.crawl(keyword=keyword, max_num=num_images)

            # Create a zip file from the downloaded images
            zip_file_path = os.path.join(downloads_dir, 'images.zip')
            with zipfile.ZipFile(zip_file_path, 'w') as zipf:
                for foldername, subfolders, filenames in os.walk(save_dir):
                    for filename in filenames:
                        file_path = os.path.join(foldername, filename)
                        zipf.write(file_path, os.path.basename(file_path))

            # Send the zip file to the user via email
            with st.spinner("Sending email..."):
                email_status = send_email_with_attachment(user_email, zip_file_path)

            if email_status is True:
                st.success(f"Successfully downloaded {num_images} images and sent them to {user_email}.")
            else:
                st.error(f"Failed to send email: {email_status}")

    except Exception as ex:
        st.error(f"An unexpected error occurred: {str(ex)}")