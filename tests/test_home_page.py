from pages.home_page import HomePage

TEXT_BANNER = 'Наши тренажеры разработаны на основе тестовых заданий работодателей. ' \
              'выполняя задания и зарабатывая баллы, ты найдешь работу мечты'


def test_trainlab_logo_is_displayed(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    assert home_page.logo().is_displayed()


def test_o_nas_button_is_displayed(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    assert home_page.o_nas_button().is_displayed()


def test_o_nas_button_text_is_ok(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    assert home_page.o_nas_button_text() == 'О нас'


def test_tasks_button_is_displayed(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    assert home_page.tasks_button().is_displayed()


def test_tasks_button_text_is_ok(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    assert home_page.tasks_button_text() == 'Задания'


def test_sign_in_button_is_displayed(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    assert home_page.sign_in_button().is_displayed()


def test_sign_in_button_text_is_ok(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    assert home_page.sign_in_button_text() == 'Войти'


def test_success_banner_text_is_ok(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    assert home_page.success_banner_text() == 'Создай свой успех'


def test_our_simulators_banner_text_is_ok(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    assert home_page.our_simulators_banner_text() == TEXT_BANNER


def test_db(connect_db):
    front_id = 1.9
    connect_db.execute(f"select front_id, text  from frontend_data where front_id = '{front_id}';")
    all_users = connect_db.fetchall()
    print(all_users)
