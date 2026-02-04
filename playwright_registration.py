from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    email_registration = page.get_by_test_id("registration-form-email-input").locator('input')
    email_registration.fill("user.name@gmail.com")

    username_registration = page.get_by_test_id("registration-form-username-input").locator('input')
    username_registration.fill("username")

    username_registration = page.get_by_test_id("registration-form-password-input").locator('input')
    username_registration.fill("password")

    button_registration = page.get_by_test_id("registration-page-registration-button")
    button_registration.click()

    dashbords_alert = page.get_by_test_id("dashboard-toolbar-title-text")
    expect(dashbords_alert).to_be_visible()
    expect(dashbords_alert).to_have_text("Dashboard")
