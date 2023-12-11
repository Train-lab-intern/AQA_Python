from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGO = (By.CSS_SELECTOR, 'img[alt="Logo"]')
    LINKEDIN_LINK = (By.CSS_SELECTOR, "[alt='linkedin']")
    GITHUB_LINK = (By.CSS_SELECTOR, "[alt='github']")
    ABOUT_US_BUTTON = (By.XPATH, '//*[@id="basic-navbar-nav"]/div[1]/a[1]/button')
    TASKS_BUTTON = (By.XPATH, '//*[@id="basic-navbar-nav"]/div[1]/a[2]/button')
    REG_BUTTON = (By.CSS_SELECTOR, "[href='/auth']")
    TOOLTIP_O_NAS = (By.XPATH, '//*[@id="basic-navbar-nav"]/div[1]/a[1]')
    HEADER_BUTTONS = [ABOUT_US_BUTTON, TASKS_BUTTON, REG_BUTTON]
