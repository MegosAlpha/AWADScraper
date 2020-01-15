from selenium import webdriver
from bs4 import BeautifulSoup, NavigableString
# Set this path within the quotes to the latest version of ChromeDriver
# See the readme to download
driver = webdriver.Chrome(r"chromedriver-path")
# List words from AWAD line-by-line in file words.txt
f = open("words.txt", "r")
words = [x.strip() for x in f.readlines()]
for word in words:
    driver.get(f"https://wordsmith.org/words/{word}.html")
    content = driver.page_source
    soup = BeautifulSoup(content, features="lxml")
    hub = soup.select("body > topbar > table:nth-child(7) > tbody > tr > td:nth-child(4)")
    meaning = 0
    usage = 0
    safehub = [ a for a in hub[0].children if not isinstance(a, NavigableString)]
    for i, child in enumerate(safehub):
        if child.text == "MEANING:":
            meaning = i + 1
        elif child.text == "USAGE:":
            usage = i + 1
    print(f"{word}: {safehub[meaning].text.strip()}")
    print(safehub[usage].text.strip())