import subprocess
from time import sleep
from clicknium import clicknium as cc, locator, ui

def main():
    if cc.chrome.extension.install_or_update():
      print("Please open chrome browser to enable clicknium extension, then run sample again.")
      return
    # open amazon website        
    tab = cc.chrome.open("https://www.amazon.com/")
    # input key words
    tab.find_element(locator.amazon.text_search).set_text('t-shirts for men')
    # click search button
    tab.find_element(locator.amazon.btn_search).click()
    # wait the first page load
    sleep(5)
    # 'locator.amazon.next_page' is next button locator, it will get top 5 page results.
    objs = cc.scrape_data(locator.amazon.div_container,{},locator.amazon.next_page,max_count=48*5)
    print(objs)
    
    sleep(3)
    tab.close()


if __name__ == "__main__":
    main()
