from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from tqdm import tqdm
import argparse
import time
import pickle


def parse_args():
    desc = "Tools to download public domain images from rawpixel website"
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--webdriver', type=str,
        help='Directory path to Chrome WebDriver application'
    )

    parser.add_argument('--output_dir', type=str,
        help='Directory path to the folder where to save images'
    )

    parser.add_argument('--url', type=str,
        help='URL link to public domain groupe of images in rawpixel website'
    )
    
    args = parser.parse_args()
    return args


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
    args = parse_args()
    driver = webdriver_instantiation(
        args.webdriver,
        args.output_dir
    )

    driver.get(args.url)
    
    add_cookies(driver, "cookies.pkl")
    scroll_down(driver)

    elements = driver.find_elements_by_css_selector('div.container-full.page-content figure a.img-link')
    links = [element.get_attribute('href') for element in elements]

    print(f"There is {len(links)} image to download")

    for link in tqdm(links[:2]):
        download_image(driver, link)