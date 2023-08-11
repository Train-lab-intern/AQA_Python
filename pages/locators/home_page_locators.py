from selenium.webdriver.common.by import By


train_lab_logo = (By.CSS_SELECTOR, 'img[alt="Logo"]')
about_us_btn = (By.CSS_SELECTOR, 'a[href="#about"] .btn.btn-secondary')
tasks_btn = (By.CSS_SELECTOR, 'a[href="#tasks"] .btn.btn-secondary')
sign_in_but = (By.XPATH, '//a[@href="/auth"]/button')  #CSS нужно использовать
success_banner_bar = (By.CLASS_NAME, 'Banner_h3_banner__BaCln')
our_simulators_banner = (By.CLASS_NAME, 'Banner_text_banner__EfApu')
