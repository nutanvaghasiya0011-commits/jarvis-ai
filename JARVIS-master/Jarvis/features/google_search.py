from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import re
import pyttsx3



def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voices', voices[0].id)
    engine.say(text)
    engine.runAndWait()
    engine.setProperty('rate', 180)


def google_search(command):

    reg_ex = re.search('search google for (.*)', command)
    search_for = command.split("for", 1)[1]
    url = 'https://www.google.com/'
    if reg_ex:
        subgoogle = reg_ex.group(1)
        url = url + 'r/' + subgoogle
    speak("Okay sir!")
    speak(f"Searching for {subgoogle}")
    try:
        service = Service()
        driver = webdriver.Chrome(service=service)  # pylint: disable=not-callable
    except (webdriver.WebDriverException, FileNotFoundError) as e:
        speak("Chrome driver not available. Please install ChromeDriver.")
        print(f"Webdriver error: {e} - google_search.py:33")
        return
    driver.get('https://www.google.com')
    search = driver.find_element(By.NAME, 'q')
    search.send_keys(str(search_for))
    search.send_keys(Keys.RETURN)