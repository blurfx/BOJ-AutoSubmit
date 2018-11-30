import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


chrome_options = Options()
chrome_options.add_argument('headless')  # If you don`t want headless mode, comment out this line.
chrome_options.add_argument("--window-size=1920,1920")
driver = webdriver.Chrome('./chromedriver.exe', chrome_options=chrome_options)


def login(id, password):
    driver.get('https://www.acmicpc.net/login?next=%2F')
    el_id = driver.find_element_by_name('login_user_id')
    el_pass = driver.find_element_by_name('login_password')
    bt_login = driver.find_element_by_css_selector('.btn-u.pull-right')

    el_id.send_keys(id)
    el_pass.send_keys(password)
    bt_login.click()

    return driver.find_element_by_css_selector('.loginbar li:first-child .username').text == id


def submit(problem_id, language, source_code):
    driver.get('https://www.acmicpc.net/submit/{0}'.format(problem_id))

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'language_chosen')))
    driver.execute_script('$("#language_chosen").trigger("mousedown");')

    langs = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.chosen-results li')))
    lang_selected = False

    for lang in langs:
        if lang.text.lower() == language.lower():
            lang_selected = True
            lang.click()
            break

    if not lang_selected:
        return False

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'CodeMirror-code')))
    driver.execute_script('myCodeMirror.setValue("{0}");'.format(source_code))

    driver.find_element_by_css_selector('button.btn.btn-primary').click()
    result = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#status-table tbody tr:first-child .result-text')))
    if ('점' in result.text and '채점' not in result.text) or ('맞았습니다' in result.text) :
        print(source_code)
        print(result)
        return True
    else:
        return False


def can_i_be_a_millionare():
    for a in range(1, 46):
        for b in range(a+1, 46):
            for c in range(b+1, 46):
                for d in range(c+1, 46):
                    for e in range(d+1, 46):
                        for f in range(e+1, 46):
                            if submit(10948, 'text', '{0} {1} {2} {3} {4} {5}'.format(a, b, c, d, e, f)):
                                sys.exit(0)
                            time.sleep(60)  # delay for re-submission

login('YOUR_BOJ_ID', 'YOUR_BOJ_PASSWORD')
can_i_be_a_millionare()
