import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#линк ниже для проверки assert ошибки если кнопки не существует
#link = "http://selenium1py.pythonanywhere.com/" #this link doesn't have an Add To Basket Button to test assert!

def test_guest_should_addtobasket(browser): #checking if Add To Busket button is on the page
    browser.get(link)
    # check = browser.find_element_by_css_selector(".btn-add-to-basket")
    # print(check)
    button = len(browser.find_elements_by_css_selector(".btn-add-to-basket"))
    assert button > 0, '!!!Button NOT found'
    #assertTrue(check, "should be button here Add To Basket")
    time.sleep(30) #to able to see the language, достаточно времени увидеть что страница на испанском