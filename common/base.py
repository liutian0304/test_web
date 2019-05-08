""""""


"""对selenium的二次封装"""

"""1. 导包 """
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""2. 定义一个打开浏览器操作的公共方法"""


def open_browser(browser='chrome'):
    """
    打开浏览器
    :param browser:
    :return:
    """
    driver = None
    if browser == 'chrome':
        driver = webdriver.Chrome()

    elif browser == 'firefox':
        driver = webdriver.Firefox()

    elif browser == 'ie':
        driver = webdriver.Ie()

    else:

        print("请输入正确的浏览器名称,例如:chrome,firefox,ie")

    return driver


"""3. 对selenium中元素操作的方法,进行封装成base类"""


class Base:
    """
    元素操作的基类
    """

    def __init__(self, driver):
        """
        初始化方法
        :param driver:
        """
        self.driver = driver

    def open_url(self, url):
        """
        打开网页
        :return:
        """
        self.driver.get(url)

    def find_element(self, locator,timeout=10):
        """
        定位一个元素,返回一个元素
        :param locator: 定位器
        :param timeout: 最大等待时间
        :return:
        """
        element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        return element

    def find_elements(self, locator,timeout=10):
        """
       定位一组元素,返回一个元素列表
       :param locator: 定位器
       :param timeout: 最大等待时间
       :return:
        """
        elements = WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))
        return elements

    def send_keys(self,locator,text,timeout=10):
        """
        元素操作-输入
        :param locator:定位器
        :param text: 输入的文本
        :param timeout: 最大等待时间
        :return:
        """
        element=self.find_element(locator,timeout)
        element.send_keys(text)

    def click(self,locator,timeout=10):
        """
        元素操作-点击
        :param locator:
        :param timeout:
        :return:
        """
        element = self.find_element(locator, timeout)
        element.click()

    def is_text_in_element(self,locator,text,timeout=10):
        """
        判断文本是否是存在元素中
        :param locator:
        :param timeout:
        :return:
        """
        try:
            result=WebDriverWait(self.driver,timeout).until(EC.text_to_be_present_in_element(locator,text))
            return result
        except:
            return False

    def is_value_in_element(self,locator,text,timeout=10):
        """
        判断元素的value属性是否存在该文本
        :param locator:
        :param text:
        :param timeout:
        :return:
        """
        try:
            result = WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element_value(locator, text))
            return result
        except:
            return False

    def close_brower(self):
        """
        关闭浏览器
        :return:
        """
        self.driver.quit()

if __name__ == '__main__':
    driver=open_browser()
    base=Base(driver)
    url="http://localhost:8080/ecshop/user.php"
    base.open_url(url)
    locator=('name','username')
    base.send_keys(locator,'admin')
