from playwright.sync_api import sync_playwright, expect, Request, Response

# Логирование запросов
def log_request(request: Request):
    print(f"Request: {request.url}")

# Логирование ответов
def log_response(response: Response):
    print(f"Response: {response.url}")

with (sync_playwright() as playwright):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.on("request", log_request)
    page.on("response", log_response)
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    auth_button = page.get_by_test_id('registration-page-registration-button')
    expect(auth_button).to_be_disabled()

    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.focus()
    for character in 'user@gmail.com':
       page.keyboard.press(character, delay=300)

    username_input = page.get_by_test_id("registration-form-username-input").locator('input')
    username_input.focus()
    for character in 'username':
        page.keyboard.press(character, delay=300)

    password_input = page.get_by_test_id("registration-form-password-input").locator('input')
    password_input.focus()
    for character in 'password':
        page.keyboard.press(character, delay=300)


    expect(auth_button).not_to_be_disabled()