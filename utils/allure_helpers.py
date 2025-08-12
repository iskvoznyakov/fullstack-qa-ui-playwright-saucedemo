import allure


def attach_screenshot(page, name="Screenshot"):
    allure.attach(
        page.screenshot(),
        name=name,
        attachment_type=allure.attachment_type.PNG
    )


def attach_page_source(page, name="Page Source"):
    allure.attach(
        page.content(),
        name=name,
        attachment_type=allure.attachment_type.HTML
    )


def attach_text_log(content, name="Log"):
    allure.attach(
        content,
        name=name,
        attachment_type=allure.attachment_type.TEXT
    )
