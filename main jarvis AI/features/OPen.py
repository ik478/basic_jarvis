import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.service import Service

# Replace with the path to your chromedriver executable (not the Chrome browser executable)
chromedriver_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"

# Create a Service object for the ChromeDriver
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://web.whatsapp.com")



def send_message(contact_name, message):
    # Open WhatsApp Web
    time.sleep(10)  # Allowing time to scan the QR code

    try:
        # Locate the search bar and search for the contact
        search_bar = driver.find_element_by_xpath("//input[@title='Search or start new chat']")
        search_bar.send_keys(contact_name)
        search_bar.send_keys(Keys.ENTER)
        time.sleep(2)  # Wait for the chat to load

        # Locate the message input field and send the message
        message_box = driver.find_element_by_xpath("//div[@contenteditable='true'][@data-tab='1']")
        message_box.send_keys(message)
        message_box.send_keys(Keys.ENTER)
        print(f"Message sent to {contact_name}: {message}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage:
send_message("kiran kumar", "Hello, John! This is Jarvis. How can I assist you today?")

# Close the browser window
driver.quit()
