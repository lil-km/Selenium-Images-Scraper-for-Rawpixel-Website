# Selenium Images Scraper for Rawpixel Website
This project scrape images from [rawpixel website](https://www.rawpixel.com/) that are on public domain.

## Prerequisites
* Install Chrome [Web Browser](https://www.google.com/chrome/).
* Install Chrome [WebDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads), just make sure version compatibility with you chrome web browser version.

## Requirements
* Install Requirements `pip install -r requirements.txt`, it's good to install dependencies in Python virtual environment.
* The `requirements.txt` file contain `Selenium` and `tqdm` libraries.

## Getting started
to use this project you need to create an account in [rawpixel website](https://www.rawpixel.com/).

1. Open chrome web browser in debbuger mode this.
2. navigate to where your chrome web browser application `chrome.exe` is installed in your filesystem.
3. to make system entrie for system environment variable `i.e PATH`.
4. Open command prompt, and enter this command:

```
chrome.exe -remote-debugging-port=9014 --user-data-dir="C:\Selenium\Chrome_Test_Profile
```

5. the new directory is added to avoid conflict between your already installed chrome web browser and chrome web browser in debbuging mode.
6. the port number is any four number of your choice.
7. the command will launch chrome web browser window in debbuging mode.
8. in the opened window (tab) navigate to [rawpixel website](https://www.rawpixel.com/) and login with your account informations.
9. Next, you need to run `get_session_cookies.py` python script. to save your session cookies as `cookies.pkl` file.
10. this feature run on >= 63 version of chrome web browser.

## Running the tests
10. Finally, you need to run `img_scraper_rawpixel.py` python script. to downlowd images in `download-directory`.

11. command:

```
python img_scraper_rawpixel.py \ 
    --browser_path="C:\Program Files (x86)\WebDriver\chromedriver.exe" \
    --output_dir="C:\ENP\Projects\GAN\Scripts\Download_img" \
    --url="https://www.rawpixel.com/board/574376/les-roses-pierre-joseph-redoute-free-cc0-roses-illustrations?sort=curated&mode=shop&page=1"

```

## Authors


## License













































