from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.EdgeOptions()
options.add_experimental_option("detach",True)
#options.add_argument("user-data-dir=/path/to/your/custom/profile")
driver = webdriver.Edge(options=options)
driver.get("https://melvoridle.com/")

def login():
    WebDriverWait(driver,30).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="formElements-language-container"]/div[1]/button'))
        ).click()
    

    #UserName
    WebDriverWait(driver,30).until(
            EC.element_to_be_clickable((By.NAME, 'formElements-signIn-username'))
        ).send_keys('saabendtsen')
    
    #password
    WebDriverWait(driver,30).until(
            EC.element_to_be_clickable((By.NAME, 'formElements-signIn-password'))
        ).send_keys('bendtsen13')
    
    #signIn
    WebDriverWait(driver,30).until(
            EC.element_to_be_clickable((By.ID, 'formElements-signIn-submit'))
        ).click()
    
    #closeAd
    WebDriverWait(driver,30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div/div/div/div[1]/div/button'))
        ).click()
    
    #ShowCloudSaves
    WebDriverWait(driver,30).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="character-selection-container"]/div[2]/button[1]'))
        ).click()
    
    #SelectSaveFile
    WebDriverWait(driver,30).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="save-slot-display-0"]/div/character-display/div/button'))
        ).click()

    #Confirm
    WebDriverWait(driver,30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[15]/div/div[6]/button[1]'))
        ).click()
    
    #CloseRecap
    WebDriverWait(driver,30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[15]/div/div[6]/button[1]'))
        ).click()
    return True

loggedIn = login()


#OpenSideMenu
driver.find_element((By.ID,'sidebar-btn'))

WebDriverWait(driver,30).until(
        EC.element_to_be_clickable((By.ID, 'sidebar-btn'))
    ).click()

#OpenBank
WebDriverWait(driver,30).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="sidebar"]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[8]/li[5]/a'))
    ).click()

#OpenRunesTab
WebDriverWait(driver,30).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="bank-tab-menu"]/div/ul/li[8]'))
    ).click()

#Count Runes
waterrunes = WebDriverWait(driver,30).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-item-id='melvorD:Water_Rune']"))
    ).get_property('badge-pill bg-secondary')
print(f"waterrunes: {waterrunes}")



def mining():
    try:
        # Wait until the element containing the text "Mining" is visible and clickable
        mining_element = WebDriverWait(driver,30).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Mining')]"))
        )
        mining_element.click()
        print("Clicked on 'Mining' link.")
    except Exception as e:
        print(f"Error clicking on the 'Mining' link: {e}")