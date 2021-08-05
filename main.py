from selenium import webdriver
from time import sleep


def get_text(driver, count):
    word = driver.find_element_by_xpath('//*[@id="row1"]/span['+str(count)+']')
    return word.text+' '


def send_texts(text, text_area):
    for c in text:
        text_area.send_keys(c)


def main():
    # Open website
    driver = webdriver.Chrome('./chromedriver')
    driver.get('https://10fastfingers.com/typing-test/english')

    # Allow cookies time
    sleep(5)

    # Main process
    count = 1
    text_area = driver.find_element_by_xpath('//*[@id="inputfield"]')
    while count < 382:
        send_texts(get_text(driver, count), text_area)
        count += 1


if __name__ == '__main__':
    main()
