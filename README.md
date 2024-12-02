# Google Image Downloader and Emailer

This application allows users to download images from Google based on a specified keyword and send the images to a provided email address. It leverages the `icrawler` library for image downloading, `streamlit` for the user interface, and `smtplib` for sending emails with attachments.

## Features

1. **Keyword-Based Image Downloading**:
   - Users can specify a keyword to search for images.
   - The number of images to be downloaded can be customized.

2. **Email Integration**:
   - The application sends the ZIP file as an email attachment to the user.

3. **Interactive UI**:
   - Built with Streamlit, providing a clean and interactive user experience.


## How It Works
1. The user inputs:
   - A keyword for the images (e.g., "beautiful landscapes").
   - The desired number of images to download.
   - Their email address to receive the images.

2. The application:
   - Downloads the specified number of images using GoogleImageCrawler.
   - Saves the images in a local directory.
   - Compresses the images into a ZIP file.
   - Sends the ZIP file to the provided email address.

## Requirements
### Prerequisites
- Python 3.7 or later
- Libraries:
  - `streamlit`
  - `icrawler`
  - `smtplib`
  - `email`
  - `pathlib`
  - `zipfile`

## File Structure

├── app.py                  
├── requirements.txt       
├── README.md               

## Configuration
### Email Setup
Ensure you use a valid Gmail account for sending emails:
1. Replace the `sender_email` and `sender_password` variables in the script with your email and app-specific password.
   - Follow [Google's guide](https://support.google.com/accounts/answer/185833?hl=en) to create an app-specific password.

### Download Directory
- Images are saved in the default Downloads folder under a subdirectory named `downloaded_images`.
- The ZIP file is saved in the Downloads folder as `images.zip`.

## Limitations
- GoogleImageCrawler may be rate-limited or blocked based on usage. Ensure you adhere to Google's terms of service.
- The provided Gmail account must have "Allow less secure apps" enabled or use an app-specific password.

## Future Enhancements
- Add support for multiple email providers (e.g., Outlook, Yahoo).
- Allow users to select specific image formats (e.g., PNG, JPG).
- Provide progress tracking for image downloads.
- Include error handling for invalid email addresses or network interruptions.

## Collaboration
This project was done in collaboration with https://github.com/arnavtiet.

## Acknowledgments
- **icrawler** for simplifying image downloads.
- **Streamlit** for providing a robust platform for building interactive apps.


