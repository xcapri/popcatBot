from selenium import webdriver


def ponCat():
    pondev = webdriver.Chrome("D:/bot/chromedriver_win32/chromedriver")
    # set path ke dir spesifik file chromedriver anda 

    getlink = 'https://popcat.click/'
    
    pondev.get(getlink)
    while True:
        pondev.find_element_by_xpath("//*[@id='app']").click() #auto klik popcat 
  
ponCat()
