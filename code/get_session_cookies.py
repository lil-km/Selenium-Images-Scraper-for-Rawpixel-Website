from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pickle



# chrome.exe -remote-debugging-port=9014 --user-data-dir="C:\Selenium\Chrome_Test_Profile"


PATH = "C:\Program Files (x86)\WebDriver\chromedriver.exe"

options = Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9014")

driver = webdriver.Chrome(PATH, options=options)

pickle.dump(driver.get_cookies() , open("cookies.pkl","wb"))

print(driver.current_url)