from playwright.sync_api import sync_playwright
from utils import UIInteractions, ErrorHandler


UI = UIInteractions()
ER = ErrorHandler()


def process_buttons(page):
    """Locate and interact with all buttons on the sidebar."""
    buttons = page.locator("a.sidebar__nav-link")
    count = buttons.count()

    for i in range(count):
        button = buttons.nth(i)

        # Get the text content of the button
        button_text = button.text_content()  # Or use button.inner_text() if needed
        href_value = button.get_attribute("href")

       #Кнопка нажимается до тех пор, пока родительская кнопка не будет активна

        if href_value:
            not_done_flag = False
            maxRetry = i
            while not_done_flag == False:
                try:
                    UI.make_button_visible(button)
                    UI.move_mouse_to_element(page, button)
                    button.click()
                    print(i + 1, "/", count, "\tclick", button_text)
                    not_done_flag = True
                    pass

                except Exception as e:
                    if maxRetry <= 0:
                        button_2 = buttons.nth(maxRetry)
                        UI.make_button_visible(button_2)
                        UI.move_mouse_to_element(page, button_2)

                        print('not done: ')
                    maxRetry -= 1
                    import time
                    time.sleep(1)
            #button.click()

            #print(i + 1, "/", count, "\tclick", button_text)

            # page.wait_for_timeout(500)


        else:

            UI.make_button_visible(button)
            UI.move_mouse_to_element(page, button)

        UI.handle_popups(page)
        ER.handle_error_toasts(page)
        ER.handle_page_load_error(page, timeout=5)

        # page.mouse.wheel(0, 50)


def test_smoke_basic(url):
    """Main test function to open a browser, login, and process sidebar buttons."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url)



       

        # page.set_viewport_size({"width": 1200, "height": 900})  # Resize the window

        if not UI.login(page, "admin", "?tP28#c2uK1rx'FeAFFO", ER):
            browser.close()
            return

        # UI.zoom_out(page, 0.50)        

        process_buttons(page)

        browser.close()


link = "https://dev.fp.big3.ru/cabinet/lists/registry_taskscheckorders_list?view=list&limit=10&offset=0"
test_smoke_basic(link)