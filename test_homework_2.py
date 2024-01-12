from selene import browser, be, have

# browser.open('https://google.com')
# browser.element('[name="q"]').should(be.blank).type('yasha/selene').press_enter()
# browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))




def test_ya(browser_size):
    browser.open('https://ya.ru/')
    browser.element('[id="text"]').should(be.blank).type('yasha/selene').press_enter()
    browser.element('[class="main serp i-bem"] [type="button"]').should(be.blank).click()
    browser.element('[id="search-result"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))
