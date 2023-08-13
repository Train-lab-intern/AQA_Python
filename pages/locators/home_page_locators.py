from selenium.webdriver.common.by import By


train_lab_logo = (By.CSS_SELECTOR, 'img[alt="Logo"]')
about_us_btn = (By.CSS_SELECTOR, 'a[href="#about"] .btn.btn-secondary')
tasks_btn = (By.CSS_SELECTOR, 'a[href="#tasks"] .btn.btn-secondary')
sign_in_btn = (By.XPATH, '//a[@href="/auth"]/button')  #CSS нужно использовать
success_banner_bar = (By.CLASS_NAME, 'Banner_h3_banner__BaCln')
our_simulators_banner = (By.CLASS_NAME, 'Banner_text_banner__EfApu')
start_the_journey_btn = (By.CLASS_NAME, 'Banner_btn_banner__ZteJM')
sql_banner = (By.CSS_SELECTOR, 'li[data-index="0"] h3')
python_banner = (By.CSS_SELECTOR, 'li[data-index="1"] h3')
java_script_banner = (By.CSS_SELECTOR, 'li[data-index="2"] h3')
