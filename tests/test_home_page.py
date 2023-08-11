import allure
import database as Database
from pages.home_page import HomePage


@allure.feature('Home page')
@allure.story('Trainlab logo')
@allure.title('Testing Trainlab logo')
def test_trainlab_logo_is_displayed(browser):
    home_page = HomePage(browser)
    with allure.step('Open Home page'):
        home_page.open_page()
    with allure.step('Check that Trainlab logo is displayed'):
        assert home_page.logo_is_displayed()


@allure.feature('Home page')
@allure.story('About us button')
@allure.title('Testing about us button')
def test_about_us_button_is_displayed(browser):
    home_page = HomePage(browser)
    with allure.step('Open Home page'):
        home_page.open_page()
    with allure.step('Check that about us button is displayed'):
        assert home_page.about_us_button_is_displayed()


@allure.feature('Home page')
@allure.story('About us button')
@allure.title('Testing about us button')
def test_about_us_button_text_is_ok(browser):
    home_page = HomePage(browser)
    with allure.step('Open Home page'):
        home_page.open_page()
    with allure.step('Check that about us button text is displayed'):
        assert home_page.o_nas_button_text() == 'О нас'


@allure.feature('Home page')
@allure.story('Tasks button')
@allure.title('Testing tasks button')
def test_tasks_button_is_displayed(browser):
    home_page = HomePage(browser)
    with allure.step('Open Home page'):
        home_page.open_page()
    with allure.step('Check that tasks button is displayed'):
        assert home_page.tasks_button_is_displayed()


@allure.feature('Home page')
@allure.story('Tasks button')
@allure.title('Testing tasks button')
def test_tasks_button_text_is_ok(browser):
    home_page = HomePage(browser)
    with allure.step('Open Home page'):
        home_page.open_page()
    with allure.step('Check that tasks button text is displayed'):
        assert home_page.tasks_button_text() == 'Задания'


@allure.feature('Home page')
@allure.story('Sign in button')
@allure.title('Testing sign in button')
def test_sign_in_button_is_displayed(browser):
    home_page = HomePage(browser)
    with allure.step('Open Home page'):
        home_page.open_page()
    with allure.step('Check that sign in button is displayed'):
        assert home_page.sign_in_button_is_displayed()


@allure.feature('Home page')
@allure.story('Sign in button')
@allure.title('Testing sign in button')
def test_sign_in_button_text_is_ok(browser):
    home_page = HomePage(browser)
    with allure.step('Open Home page'):
        home_page.open_page()
    with allure.step('Check that sign in button text is displayed'):
        assert home_page.sign_in_button_text() == 'Войти'


@allure.feature('Home page')
@allure.story('Success banner')
@allure.title('Testing success banner')
def test_success_banner_text_is_ok(browser):
    home_page = HomePage(browser)
    with allure.step('Open Home page'):
        home_page.open_page()
    with allure.step('Check that success banner text is displayed'):
        assert home_page.success_banner_text() == 'Создай свой успех'


@allure.feature('Home page')
@allure.story('Success banner')
@allure.title('Testing success banner')
def test_success_banner_text_takes_from_bd(browser):  #надо менять структуру
    with allure.step('Take text from database by front id'):
        text_from_database = Database.take_text_from_database_by_front_id(1.1)
    with allure.step('Change text in database by front id'):
        Database.change_text_in_database_by_front_id(1.1, 'Текст изменен')
    home_page = HomePage(browser)
    with allure.step('Open Home page'):
        home_page.open_page()
    with allure.step('Take text from element on website'):
        new_text_from_website = home_page.success_banner_text()
    with allure.step('Return text to database by front id'):
        Database.change_text_in_database_by_front_id(1.1, f"{text_from_database}")
    with allure.step('Check that text for website element takes from database'):
        assert new_text_from_website == 'Текст изменен'


@allure.feature('Home page')
@allure.story('Simulators banner')
@allure.title('Testing simulators banner')
def test_our_simulators_banner_text_is_ok(browser):
    home_page = HomePage(browser)
    with allure.step('Open Home page'):
        home_page.open_page()
    with allure.step('Check that simulators banner text is displayed'):
        assert home_page.our_simulators_banner_text() == 'Наши тренажеры' \
             ' разработаны на основе тестовых заданий работодателей. ' \
             'выполняя задания и зарабатывая баллы, ты найдешь работу мечты'


@allure.feature('Home page')
@allure.story('Simulators banner')
@allure.title('Testing simulators banner')
def test_our_simulators_banner_text_takes_from_bd(browser):  #надо менять структуру
    with allure.step('Take text from database by front id'):
        text_from_database = Database.take_text_from_database_by_front_id(1.2)
    with allure.step('Change text in database by front id'):
        Database.change_text_in_database_by_front_id(1.2, 'Текст изменен')
    home_page = HomePage(browser)
    with allure.step('Open Home page'):
        home_page.open_page()
    with allure.step('Take text from element on website'):
        new_text_from_website = home_page.our_simulators_banner_text()
    with allure.step('Return text to database by front id'):
        Database.change_text_in_database_by_front_id(1.2, f"{text_from_database}")
    with allure.step('Check that text for website element takes from database'):
        assert new_text_from_website == 'Текст изменен'


@allure.feature('Home page')
@allure.story('Start the journey button')
@allure.title('Testing start the journey button')
def test_start_the_journey_button_is_displayed(browser):
    home_page = HomePage(browser)
    with allure.step('Open Home page'):
        home_page.open_page()
    with allure.step('Check that start the journey button is displayed'):
        assert home_page.start_the_journey_button_is_displayed()


@allure.feature('Home page')
@allure.story('Start the journey button')
@allure.title('Testing start the journey button')
def test_start_the_journey_button_text_is_ok(browser):
    home_page = HomePage(browser)
    with allure.step('Open Home page'):
        home_page.open_page()
    with allure.step('Check that start the journey button text is displayed'):
        assert home_page.start_the_journey_button_text() == 'Начать путь'
