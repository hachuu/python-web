from selenium import webdriver
from selenium.webdriver.common.by import Bydkssud
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Chrome 웹 드라이버 경로 설정
driver_path = "D:\webdriver\chromedriver.exe"

# 웹 드라이버 초기화
driver = webdriver.Chrome(driver_path)

# 웹 페이지로 이동
login_url = "로그인_페이지_URL"
driver.get(login_url)

# 로그인 정보 입력
username = "사용자명"
password = "비밀번호"
username = driver.find_element_by_name("username")  # 사용자명 입력 필드 선택
password = driver.find_element_by_name("password")  # 비밀번호 입력 필드 선택

username.send_keys(username)  # 사용자명 입력
password.send_keys(password)  # 비밀번호 입력

# 로그인 버튼 클릭
login_button = driver.find_element_by_xpath("//button[contains(text(), '로그인')]")
login_button.click()

# 로그인 후 처리 대기
wait = WebDriverWait(driver, 10)  # 최대 10초까지 대기
wait.until(EC.title_contains("로그인 성공 페이지 제목"))

# 라디오 체크박스 선택
radio_button = driver.find_element_by_id("라디오_체크박스_ID")
radio_button.click()

# 버튼 클릭
button = driver.find_element_by_id("버튼_ID")
button.click()

# 웹 드라이버 종료
driver.quit()