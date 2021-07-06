from selenium import webdriver
from time import sleep
#----
def get_text(count):
    word = driver.find_element_by_xpath('//*[@id="row1"]/span['+str(count)+']')
    return word.text+' '
def send_texts(text, text_area):
    for c in text:
        text_area.send_keys(c)
def main():
    sleep(5)
    count = 1
    text_area = driver.find_element_by_xpath('//*[@id="inputfield"]')
    while count < 382:
        send_texts(get_text(count), text_area)
        count += 1
if __name__ == '__main__':
    driver = webdriver.Chrome('./chromedriver')
    driver.get('https://10fastfingers.com/typing-test/english')
    main()







# prefs = {"profile.default_content_setting_values.notifications" : 2}
# options = webdriver.ChromeOptions()
# options.add_argument("--disable-infobars")
# options.add_experimental_option("prefs", prefs)
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option('useAutomationExtension', False)