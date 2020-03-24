from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import base64, time, datetime

target_list = ['www.tongxueqn.com', 'su.tongxueqn.com', 'ten.tongxueqn.com' ,'ali.tongxueqn.com']
driverpath = './chromedriver'

for target in target_list:
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')

    driver = webdriver.Chrome(executable_path=driverpath, options=chrome_options)
    driver.get('https://www.boce.com/')

    url_input = driver.find_element_by_class_name('el-input__inner')
    url_input.send_keys(target)

    url_enter = driver.find_elements_by_class_name('el-button--primary')[1]
    url_enter.click()

    while(True):
        try:
            result_button = driver.find_element_by_css_selector('.result-wrap .detail-wrap .el-button')
            result_button.click()
            break
        except:
            pass

    map = driver.find_element_by_tag_name('canvas')
    canvas_base64 = driver.execute_script("return arguments[0].toDataURL('image/png').substring(21);", map)
    canvas_png = base64.b64decode(canvas_base64)

    with open(r"./screenshot/"+target+"_"+datetime.datetime.now().strftime('%m-%d %H:%M:%S')+".png", 'wb') as f:
        f.write(canvas_png)

    time.sleep(10)
    driver.close()

