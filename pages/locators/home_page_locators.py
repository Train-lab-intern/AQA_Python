from selenium.webdriver.common.by import By


train_lab_logo = (By.CSS_SELECTOR, 'img[alt="Logo"]')
o_nas_bar = (By.CSS_SELECTOR, 'a[href="#about"]')
tasks_but = (By.XPATH, '//a[@href="#tasks"]/button')
sign_in_but = (By.XPATH, '//a[@href="/auth"]/button')
success_banner_bar = (By.CLASS_NAME, 'Banner_h3_banner__BaCln')
our_simulators_banner = (By.CLASS_NAME, 'Banner_text_banner__EfApu')
o_nas = (By.CSS_SELECTOR, 'a[href="#about"] .btn.btn-secondary')
