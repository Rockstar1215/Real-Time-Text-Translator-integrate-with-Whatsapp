from pynput import keyboard
from googletrans import Translator
from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Replace with the path to your Chrome WebDriver
webdriver_path = '../../../../chrome-win64'

# Create a new instance of the Chrome WebDriver
service = Service(executable_path=webdriver_path)
driver = webdriver.Chrome()

# Use the driver to interact with Google Chrome
driver.get('https://web.whatsapp.com')

# Initialize the translator
translator = Translator()

# Define a variable to hold the message being typed
message = ''

# Ask the user to choose the destination language
dest_language = input("Enter the destination language (e.g., 'hi' for Hindi): ")

def on_key_press(key):
    global message
    try:
        # Check if the key pressed is the "Enter" key
        if key == keyboard.Key.enter:
            # Translate the entire message to the chosen language
            translation = translator.translate(message, src='en', dest=dest_language)
            print(f'Message: {message} (Translated: {translation.text})')

            # Send the translated message through WhatsApp Web
            text_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
            text_box.click()
            text_box.send_keys(translation.text)
            text_box.send_keys(Keys.ENTER)

            # Reset the message
            message = ''
        else:
            # Accumulate the characters being typed into the message
            message += key.char

    except AttributeError:
        # Some keys don't have a char attribute (e.g., special keys)
        print(f'Special key pressed: {key}')

# Define a function to handle key release events (if needed)
def on_key_release(key):
    pass

# Create a keyboard listener
with keyboard.Listener(on_press=on_key_press, on_release=on_key_release) as listener:
    # Start listening for keyboard events
    listener.join()
