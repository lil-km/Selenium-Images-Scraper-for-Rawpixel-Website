from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from tqdm import tqdm
import time
import pickle

# PATH = "C:\Program Files (x86)\WebDriver\chromedriver.exe"
# r'C:\ENP\Projects\GAN\Scripts\Download_img'

def webdriver_instantiation(PATH, download_path):
    options = Options()
    options.add_argument("--headless")

    browser_driver = webdriver.Chrome(PATH, options=options)

    params = {'behavior': 'allow', 'downloadPath': download_path}
    browser_driver.execute_cdp_cmd('Page.setDownloadBehavior', params)

    return browser_driver


def download_image(browser_driver, link):
    browser_driver.get(link)
    try:
        button = WebDriverWait(browser_driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'button.btn.download'))
        )
    except TimeoutException:
        print("TimeOut error!!!")

    button.click()
    time.sleep(3)

def add_cookies(browser_driver, cookies_file):
    cookies = pickle.load(open(cookies_file, "rb"))
    for cookie in cookies:
        browser_driver.add_cookie(cookie)

    time.sleep(3)
    browser_driver.refresh()

def scroll_down(browser_driver):
    jscript = """
        window.scrollTo(0, document.body.scrollHeight);
        var page_depth = document.body.scrollHeight;
        return page_depth;
    """

    page_depth = browser_driver.execute_script(jscript)
    match = False
    while(match == False):
        current_count = page_depth
        time.sleep(3)
        page_depth = browser_driver.execute_script(jscript)
        if(current_count == page_depth):
            match = True


if __name__ == '__main__':
    url =  "https://www.rawpixel.com/board/574376/les-roses-pierre-joseph-redoute-free-cc0-roses-illustrations?sort=curated&mode=shop&page=1"

    driver = webdriver_instantiation(
        "C:\Program Files (x86)\WebDriver\chromedriver.exe",
        r'C:\ENP\Projects\GAN\Scripts\Download_img'
    )
    
    driver.get(url)
    
    add_cookies(driver, "cookies.pkl")
    scroll_down(driver)

    elements = driver.find_elements_by_css_selector('div.container-full.page-content figure a.img-link')
    links = [element.get_attribute('href') for element in elements]

    print(f"There is {len(links)} image to download")

    for link in tqdm(links[:2]):
        download_image(driver, link)