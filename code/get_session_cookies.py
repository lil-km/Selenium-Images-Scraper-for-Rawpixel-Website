from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pickle


def parse_args():
    desc = "Get session cookies for given website"
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--webdriver', type=str,
        help='Directory path to Chrome WebDriver application'
    )

    args = parser.parse_args()
    return args


def webdriver_instantiation(PATH):
    options = Options()
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9014")

    browser_driver = webdriver.Chrome(PATH, options=options)
    print(f"The current URL: {browser_driver.current_url}")

    return browser_driver


if __name__ '__main__':
    args = parse_args()

    driver = webdriver_instantiation(args.webdriver)

    pickle.dump(driver.get_cookies() , open("cookies.pkl","wb"))

