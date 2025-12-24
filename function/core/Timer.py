"""
Web Clock Automation (Timer + Alarm)
-----------------------------------
Requirements:
pip install selenium webdriver-manager
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


# -------------------- DRIVER SETUP -------------------- #
def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    return webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def start_timer(minutes: int):
    driver = get_driver()
    driver.get("https://www.online-stopwatch.com/countdown-timer/")

    wait = WebDriverWait(driver, 20)

    # --------- SWITCH TO IFRAME ---------
    iframe = wait.until(
        EC.presence_of_element_located((By.TAG_NAME, "iframe"))
    )
    driver.switch_to.frame(iframe)

    # --------- FIND MINUTE INPUT ---------
    min_box = wait.until(
        EC.presence_of_element_located((By.NAME, "cd-minutes"))
    )
    min_box.clear()
    min_box.send_keys(str(minutes))

    # --------- CLICK START ---------
    start_btn = wait.until(
        EC.element_to_be_clickable((By.ID, "startBut"))
    )
    start_btn.click()

    print(f"[OK] {minutes} minute timer started")

# -------------------- ALARM FUNCTION -------------------- #
def set_alarm(hour: int, minute: int = 0, period: str = "pm"):
    """
    Example:
    set_alarm(2, 0, "pm")  # sets 2:00 PM alarm
    set_alarm(7, 30, "am")
    """
    driver = get_driver()
    driver.get("https://www.timeanddate.com/alarms/create.html")

    time.sleep(4)

    # Hour
    h = driver.find_element(By.ID, "aHour")
    h.clear()
    h.send_keys(str(hour))

    # Minute
    m = driver.find_element(By.ID, "aMinute")
    m.clear()
    m.send_keys(f"{minute:02d}")

    # AM / PM
    ap = driver.find_element(By.ID, "aAmPm")
    ap.send_keys(period.upper())

    # Save alarm
    driver.find_element(By.XPATH, "//button[contains(text(),'Save')]").click()

    print(f"[OK] Alarm set for {hour}:{minute:02d} {period.upper()}")


