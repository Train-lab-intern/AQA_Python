EMAIL = 'test.trainlab@gmail.com'

PASSWORD = 'Qaz12345'

EMPTY_FIELD = ''

VALID_EMAIL = [
    'test.trainlab@gmail.com', 'TEST.TRAINLAB@GMAIL.COM', 'test.trainlab+1234567890@gmail.com',
    'test.trainlab@gmail1234567890.com', 'test-trainlab@gmail.com', 'test.trainlab@gmail-mail.com',
    'test.trainlab@gmail.com', 'test_trainlab@gmail.com', 'test.trainlab@gmail.com.com',
    'test$trainlab@gmail.com', 'test#trainlab@gmail.com', 'test%trainlab@gmail.com',
    'test&trainlab@gmail.com', 'test*trainlab@gmail.com', 'test‘trainlab@gmail.com'
    'test/trainlab@gmail.com', 'test=trainlab@gmail.com', 'test^trainlab@gmail.com',
    'test?trainlab@gmail.com', 'test`trainlab@gmail.com', 'test{trainlab}@gmail.com',
    'test|trainlab@gmail.com', 'test~trainlab@gmail.com', 'b@gmail.com', 'ab@gmail.com',
    'a@ya.ru', 'Test.TraiNlab@gmail.com',
    'test.trainlab+Sun_of_the_sleepless_Melancholy_star_Whose_tearful_beam_'
    'glows_tremulously_far_That_showst_the_darkness_thou_canst_not_dispel_How'
    '_like_art_thou_to_joy_rememberd_well_What_is_this_life_if_ful_of_care_We'
    '_have_no_time_to_stand_andstare@gmail.com',
    'test.trainlab+Sun_of_the_sleepless_Melancholy_star_Whose_tearful_beam_glows_tremulously'
    '_far_That_showst_the_darkness_thou_canst_not_dispel_How_like_art_thou_to_joy_rememberd'
    '_well_What_is_this_life_if_ful_of_care_We_have_no_time_to_stand_and_stare@gmail.com']

INVALID_EMAIL = [
    'test.trainlabgmail.com', 'test.trainlab@gmailcom', 'тест.траинлаб@gmailcom', '', '     ',
    '.test.trainlab@gmail.com', 'test.trainlab@gmail.com.', 'test..trainlab@gmail.com',
    'test trainlab@gmail.com', 'test.trainlab@gm ail.com', '@gmailcom',
    'test.trainlab+Sun_of_the_sleepless_Melancholy_star_Whose_tearful_beam_glows_tremulously_far'
    '_That_showst_the_darkness_thou_canst_not_dispel_How_like_art_thou_to_joy_rememberd_well_What'
    '_is_this_life_if_ful_of_care_We_have_no_time_to_stand_and_stare1@gmail.com'
]

VALID_PASSWORD = [
    'Qaz1234567890123456789012345678901234567890123456789xexexcefcrgv'
    'thc1234567890123556790qertyooasdfghkozxvbnmqeryoadfhjkzxcvbnmasdfgh'
    'kqetyuiizsdfghjjkjzxcderfvtgbyhnqazwsx1234567890qwertyuioasdgghjklz'
    'xcvbnmmececfvrvtgbhbybcedxwsxwdcefvrgtbrcexwxexrgvtvhbrcfe',
    'Qaz12345', '12345azQ', '123Q45we'
]

INVALID_PASSWORD = [
    '', '        ', '1 ', '   1234567    Q a ', '12345678',
    'qazwsxedc', 'QWERASDFZ', 'Aqazwsxedc', 'Фйц123456',
    'Qaz1234', 'Qaz12345678901234567890123456789012345678'
    '90123456789xexexcefcrgvthc12345678901235567'
    '90qertyooasdfghkozxvbnmqeryoadfhjkzxcvbnmasdfghk'
    'qetyuiizsdfghjjkjzxcderfvtgbyhnqazwsx1234567890qw'
    'ertyuioasdgghjklzxcvbnmmececfvrvtgbhbybcedxwsxwdce'
    'fvrgtbrcexwxexrgvtvhbrcfed', 'QAZ12345', 'Qaz12345`',
    'Qaz12345,<.>/?;:~!@#$%^&*()_-+=|'
]

USERNAMES = [
    'VASIA', 'vasia', '1vasia', 'Vasia,./<>?:;|{}[]~`!@#$%^&*()_+=-', '', '   '
]

USERNAME = 'Vasia'
