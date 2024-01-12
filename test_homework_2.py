from selene import browser, be, have

def test_google_available_text(browser_scale):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yasha/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

def test_google_not_available_text(browser_scale):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('Какой$то бред товориться#$@$$%$%$%#%^%^&%@&%^@$').press_enter()
    browser.element('.card-section [role="heading"]').should(have.exact_text('По запросу Какой$то бред товориться#$@$$%$%$%#%^%^&%@&%^@$ ничего не найдено.'))