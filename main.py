# 자동화 테스트를 위해 셀리니움을 불러옵니다.
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import pyperclip

####################
def clipboard_input(user_xpath, user_input):
    temp_user_input = pyperclip.paste()  # 사용자 클립보드를 따로 저장
    
    pyperclip.copy(user_input)
    driver.find_element_by_xpath(user_xpath).click()
    ActionChains(driver).key_down(Keys.COMMAND).send_keys('v').key_up(Keys.COMMAND).perform()
    
    pyperclip.copy(temp_user_input)  # 사용자 클립보드에 저장 된 내용을 다시 가져 옴
    time.sleep(1)
    
    clipboard_input('//*[@id="id"]', login.get("id"))

####################

# FireFox 드라이버의 경로를 설정합니다. 
driver = webdriver.Firefox(executable_path='/etc/geckodriver')

# 접속할 url
url = "https://nid.naver.com/nidlogin.login"

# 접속 시도
driver.get(url)


login = {
    "id" : "msjiyouth",
    "pw" : "Awake2023!!!"
}

# # 아이디와 비밀번호를 입력합니다.
# time.sleep(0.5) ## 0.5초
# # driver.find_element_by_name('id').send_keys('아이디') # "아이디라는 값을 보내준다"
# driver.find_element_by_name('id').send_keys(login.get("id"))
# time.sleep(0.5) ## 0.5초
# driver.find_element_by_name('pw').send_keys(login.get("pw"))


clipboard_input('//*[@id="pw"]', login.get("pw"))
driver.find_element_by_xpath('//*[@id="log.login"]').click()

