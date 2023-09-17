from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Set the path to your Chrome WebDriver executable
webdriver_path = 'path/to/chromedriver'

# Start the Chrome browser
driver = webdriver.Chrome(executable_path=webdriver_path)

# Open WhatsApp Web
driver.get('https://web.whatsapp.com/')

# Wait for the user to scan the QR code and log in manually
input("Press Enter after scanning the QR code and logging in...")

# Define the message to be translated
original_message = "Hello, world!"

# Translation API (e.g., Yandex.Translate, Google Translate, etc.)
# Replace this with the actual translation code

# Example: Using Yandex.Translate API
# Replace 'YOUR_API_KEY' with your Yandex.Translate API key
api_key = 'YOUR_API_KEY'
target_language = 'es'  # Target language code

# Perform translation (implement your translation logic here)
# For simplicity, we'll just use the original message
translated_message = original_message

# Find the input field to send a message
input_box = driver.find_element_by_xpath("//div[@class='_2_1wd copyable-text selectable-text']")

# Enter the translated message
input_box.send_keys(translated_message)

# Send the message
input_box.send_keys(Keys.ENTER)

# Close the browser after a few seconds (adjust as needed)
time.sleep(5)
driver.quit()
