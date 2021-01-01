from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time
# import pymongo
# import numpy as np
# import pandas as pd

PLATFORM_NAME = 'Android'
DEVICE_NAME = 'MI_6X'
APP_PACKAGE = 'com.tencent.mm'
APP_ACTIVITY = '.ui.LauncherUI'
DRIVER_SERVER = 'http://127.0.0.1:4723/wd/hub'


class Moments(object):
    def __init__(self, max_date_back=365, max_num_moments=10000, data_loading_waiting_time=200):
        self.start_time = time.time()
        self.max_date_back = max_date_back
        self.max_num_moments = max_num_moments
        self.data_loading_waiting_time = data_loading_waiting_time
        self.desired_capabilities = {
            'platformName': PLATFORM_NAME,
            'deviceName': DEVICE_NAME,
            'appPackage': APP_PACKAGE,
            'appActivity': APP_ACTIVITY,
            'noReset': "True"
        }
        print('正在启动Appium服务器... 此过程耗时1分钟左右，请您耐心等待')  # 全程不能触碰手机屏幕
        self.driver = webdriver.Remote(DRIVER_SERVER, self.desired_capabilities)
        self.action = TouchAction(self.driver)
        self.wait = WebDriverWait(self.driver, 300)
        print('\n', time.time() - self.start_time)
        print('正在开启数据库...')
        # self.client = pymongo.MongoClient()
        # self.db = self.client.weixin
        # self.collection = self.db.weixin  # 数据会存到self.collection里
        # print('请在下方输入登录方式并回车（如果您希望通过手机号-密码登录，请输入1；如果想通过手机号-短信验证码登录，请输入2）')
        # self.login_method = input('请输入登录方式：')

    def password2keycode(self, password):
        n = len(password)
        keycode = []
        for i in range(n):
            if type(password[i]) == str:
                if password[i].isupper():
                    keycode.append([dict_keycode[password[i]], 1])
                else:
                    keycode.append([dict_keycode[password[i]], 0])
            else:
                keycode.append([dict_keycode[password[i]], 0])
        return n, keycode

    def login(self):
        # 点击”登录“
        phone_num = input('请输入您的手机号：')
        password = input('请输入您的密码：')
        print('\n', time.time() - self.start_time)
        print('正在解析页面信息...')
        login = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/fam')))
        print('\n', time.time() - self.start_time)
        print('正在点击登录按钮...')
        login.click()

        # 输入手机号
        print('\n', time.time() - self.start_time)
        print('正在解析页面信息...')
        phone_num_input = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/bhn')))
        print('\n', time.time() - self.start_time)
        print('正在输入手机号...')
        phone_num_input.send_keys(phone_num)
        # phone_num = input('请输入手机号：')
        # phone.send_keys(phone_num)

        # 点击“下一步”
        print('\n', time.time() - self.start_time)
        print('正在解析页面信息...')
        next_button = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/e3i')))
        print('\n', time.time() - self.start_time)
        print('正在点击下一步...')
        next_button.click()

        # # 权限申请 点击“知道了”
        # print('\n', time.time() - self.start_time)
        # print('正在解析页面信息...')
        # permission = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/doz')))
        # permission.click()
        #
        # # 点击“确定”
        # print('\n', time.time() - self.start_time)
        # print('正在解析页面信息...')
        # confirmation = self.wait.until(EC.presence_of_element_located((By.ID, 'android:id/button1')))
        # confirmation.click()
        # # if self.login_method == '1':
        # print('\n', time.time() - self.start_time)
        # print('正在解析页面信息...')
        # # time.sleep(15)

        # 输入密码
        # print('\n', time.time() - self.start_time)
        # print('正在解析页面信息...')
        # password_input = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/bhn')))
        print('\n', time.time() - self.start_time)
        print('正在输入密码...')
        n, keycode = self.password2keycode(password)
        # print(n, keycode)
        time.sleep(3)
        for i in range(n):  # range(n)中的n为密码的位数
            # print(i, keycode[i])
            if keycode[i][1] == 1:
                time.sleep(3)
                self.driver.press_keycode(keycode[i][0], 1048576, 115)  # left_shift: 64, 59
            else:
                self.driver.press_keycode(keycode[i][0])
        # password_input.send_keys(pass_w)
        # password_input.send_keys(self.password)

        # 点击“登录”
        print('\n', time.time() - self.start_time)
        print('正在解析页面信息...')
        login = self.driver.find_element_by_id('com.tencent.mm:id/e3i')
        # login = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/e3i')))
        print('\n', time.time() - self.start_time)
        print('正在点击登录... 请耐心等待')
        login.click()

        # 提示是否看手机通讯录 点击“否”
        print('\n', time.time() - self.start_time)
        print('正在解析页面信息...')
        tip = self.wait.until(EC.element_to_be_clickable((By.ID, 'com.tencent.mm:id/dom')))
        print('\n', time.time() - self.start_time)
        print('正在点击...')
        tip.click()

        # # 设置字体大小
        # time.sleep(3)
        # print('\n', time.time() - self.start_time)
        # print('正在解析页面信息...')
        # setting = self.wait.until(EC.element_to_be_clickable((By.ID, 'com.tencent.mm:id/dom')))
        # print('\n', time.time() - self.start_time)
        # print('正在点击...')
        # setting.click()
        # # elif self.login_method == '2':
        # #     pass


    def enter(self):
        # 载入数据 & 点击“发现”
        print('\n', time.time() - self.start_time)
        print('正在解析页面信息...')
        # self.driver.implicitly_wait(self.data_loading_waiting_time)
        discover = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//android.widget.RelativeLayout[3]')))
        # '/*[@resource-id="com.tencent.mm:id/cn_"]/..  //*[@resource-id="com.tencent.mm:id/cn_"]
        # presence_of_element_located
        print('\n', time.time() - self.start_time)
        print('正在点击发现...')
        time.sleep(3)
        discover.click()
        # self.wait.until(EC.text_to_be_present_in_element((By.ID,'com.tencent.mm:id/cdj'),'发现'))

        # 点击“朋友圈”
        print('\n', time.time() - self.start_time)
        print('正在解析页面信息...')
        moments = self.wait.until(EC.presence_of_element_located(
            (By.XPATH,
             '//*[@resource-id="com.tencent.mm:id/f43"]')))  # '//*[@resource-id="android:id/list"]/*[@class="android.widget.LinearLayout"][1]'
        print('\n', time.time() - self.start_time)
        print('正在点击朋友圈')
        moments.click()


    def crawl(self, l_nickname_chosen):
        print('\n', time.time() - self.start_time)
        print('准备开始爬取...')
        curr_date = 0
        num_moments = 0
        l_data = []
        while curr_date < self.max_date_back and num_moments < self.max_num_moments:
            # items = self.wait.until(EC.presence_of_all_elements_located(
            #     (By.XPATH, '//*[@resource-id="com.tencent.mm:id/fol"]')))  # '//*[@resource-id="com.tencent.mm:id/dja"]//*[@class="android.widget.FrameLayout"]'
            self.driver.swipe(300, 1400, 300, 150)
            print('\n\n--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--    ',
                  time.time() - self.start_time)
            print('已爬取到{}天内共{}条朋友圈'.format(curr_date, num_moments))
            print('当前页面共有{}条朋友圈'.format(len(self.driver.find_elements(By.XPATH, '//*[@resource-id="com.tencent.mm:id/fn_"]'))))
            for moment in self.driver.find_elements(By.XPATH, '//*[@resource-id="com.tencent.mm:id/fn_"]'):
                # if self.driver.find_element_by_id('//*[@resource-id="com.tencent.mm:id/fn_"]'):
                num_moments += 1
                try:
                    nickname = moment.find_element(By.XPATH, '//*[@resource-id="com.tencent.mm:id/e3x"]').get_attribute('text')  # as6
                    print('\n######################')
                    if len(l_nickname_chosen) > 0 and l_nickname_chosen != ['']:
                        if nickname in l_nickname_chosen:
                            print('nickname', nickname)
                            for a in [
                                "com.tencent.mm:id/b_e", "com.tencent.mm:id/b_l", "com.tencent.mm:id/b_m"
                            ]:
                                try:
                                    content = moment.find_element(By.ID, a).get_attribute('text')  # dkf
                                    print('content:', content)
                                    break
                                except Exception as e:
                                    content = ''
                                    print('Error (content):', e)
                            try:
                                date = moment.find_element(By.ID, 'com.tencent.mm:id/ij').get_attribute('text')
                                print('pre_process:', date)
                                if '天前' in date.strip():
                                    date = int(date.strip('天前'))
                                elif date.strip() == '昨天':
                                    date = 1
                                else:
                                    date = 0
                                print('date_back', date)
                            except Exception as e:
                                date = -1
                                print('Error (date_back):', e)
                            try:
                                image = []
                                for a in [
                                    'com.tencent.mm:id/hx', 'com.tencent.mm:id/hy', 'com.tencent.mm:id/hz',
                                    'com.tencent.mm:id/i0', 'com.tencent.mm:id/i1', 'com.tencent.mm:id/i2',
                                    'com.tencent.mm:id/i3', 'com.tencent.mm:id/i4', 'com.tencent.mm:id/i5'
                                ]:
                                    try:
                                        img = moment.find_element(By.ID, a)
                                        image.append(img)
                                    except:
                                        break
                                print('image', image)
                                data = {'nickname': nickname, 'date_back': date, 'content': content, 'link': '',
                                        'video': '', 'image': image}
                                l_data.append(data)
                                # self.collection.update({'nickname': nickname}, {'$set': data}, True)
                                continue
                            except Exception as e:
                                image = []
                                print('Error (image):', e)
                            try:
                                link = moment.find_element(By.ID, 'com.tencent.mm:id/dm3')
                                print('link', link)
                                data = {'nickname': nickname, 'date_back': date, 'content': content, 'link': link,
                                        'video': '', 'image': []}
                                l_data.append(data)
                                # self.collection.update({'nickname': nickname}, {'$set': data}, True)
                                continue
                            except Exception as e:
                                link = ''
                                print('Error (link):', e)
                            try:
                                video = moment.find_element(By.ID, 'com.tencent.mm:id/gnv')
                                print('video', video)
                                data = {'nickname': nickname, 'date_back': date, 'content': content, 'link': '',
                                        'video': video, 'image': []}
                                l_data.append(data)
                                # self.collection.update({'nickname': nickname}, {'$set': data}, True)
                                continue
                            except Exception as e:
                                video = ''
                                print('Error (video):', e)


                        else:
                            print('nickname not chosen')
                            pass

                    else:
                        print('nickname', nickname)
                        for a in [
                            "com.tencent.mm:id/b_e", "com.tencent.mm:id/b_l", "com.tencent.mm:id/b_m"
                        ]:
                            try:
                                content = moment.find_element(By.ID, a).get_attribute('text')  # dkf
                                print('content:', content)
                                break
                            except Exception as e:
                                content = ''
                                print('Error (content):', e)
                        try:
                            date = moment.find_element(By.ID, 'com.tencent.mm:id/ij').get_attribute('text')
                            print('pre_process:', date)
                            if '天前' in date:
                                date = int(date.strip('天前'))
                            elif date == '昨天':
                                date = 1
                            else:
                                date = 0
                            if date > curr_date:
                                curr_date = date
                            print('date_back', date)
                        except Exception as e:
                            date = -1
                            print('Error (time):', e)
                        try:
                            image = []
                            for a in [
                                'com.tencent.mm:id/hx', 'com.tencent.mm:id/hy', 'com.tencent.mm:id/hz',
                                'com.tencent.mm:id/i0', 'com.tencent.mm:id/i1', 'com.tencent.mm:id/i2',
                                'com.tencent.mm:id/i3', 'com.tencent.mm:id/i4', 'com.tencent.mm:id/i5'
                            ]:
                                try:
                                    img = moment.find_element(By.ID, a)
                                    image.append(img)

                                except:
                                    break
                            print('image', image)
                            data = {'nickname': nickname, 'date_back': date, 'content': content, 'link': '',
                                    'video': '', 'image': image}
                            l_data.append(data)
                            # self.collection.update({'nickname': nickname}, {'$set': data}, True)
                            continue
                        except Exception as e:
                            image = []
                            print('Error (image):', e)
                        try:
                            link = moment.find_element(By.ID, 'com.tencent.mm:id/dm3')
                            print('link', link)
                            data = {'nickname': nickname, 'date_back': date, 'content': content, 'link': link,
                                    'video': '', 'image': []}
                            l_data.append(data)
                            # self.collection.update({'nickname': nickname}, {'$set': data}, True)
                            continue
                        except Exception as e:
                            link = ''
                            print('Error (link):', e)
                        try:
                            video = moment.find_element(By.ID, 'com.tencent.mm:id/gnv')
                            print('video', video)
                            data = {'nickname': nickname, 'date_back': date, 'content': content, 'link': '',
                                    'video': video, 'image': []}
                            l_data.append(data)
                            # self.collection.update({'nickname': nickname}, {'$set': data}, True)
                            continue
                        except Exception as e:
                            video = ''
                            print('Error (video):', e)

                except:
                    pass

        print(l_data)
        # print(pd.DataFrame(l_data))
        # return pd.DataFrame(l_data)


    def main(self):
        # self.login()
        print('\n', time.time() - self.start_time)
        print('登录成功！正在载入数据...请耐心等待')
        self.enter()
        while True:
            print("如果想爬取特定昵称的朋友圈，请以  昵称1,昵称2  的形式传入您想要爬取的昵称（用英文逗号分隔，昵称之间不要输空格）；否则，请直接回车")
            l_nickname_chosen = input('请按上述说明输入：').strip().split(',')
            try:
                assert type(l_nickname_chosen) == list
                self.crawl(l_nickname_chosen)
                break
            except Exception as e:
                print('\nError (nickname_input):', e)
                print('请在下方重新输入您想爬取的昵称\n')
                pass
        # return df


dict_keycode = {'0': 7, '1': 8, '2': 9, '3': 10, '4': 11, '5': 12, '6': 13, '7': 14, '8': 15, '9': 16,
                'A': 29, 'B': 30, 'C': 31, 'D': 32, 'E': 33, 'F': 34, 'G': 35, 'H': 36, 'I': 37, 'J': 38,
                'K': 39, 'L': 40, 'M': 41, 'N': 42, 'O': 43, 'P': 44, 'Q': 45, 'R': 46, 'S': 47, 'T': 48,
                'U': 49, 'V': 50, 'W': 51, 'X': 52, 'Y': 53, 'Z': 54,
                'a': 29, 'b': 30, 'c': 31, 'd': 32, 'e': 33, 'f': 34, 'g': 35, 'h': 36, 'i': 37, 'j': 38,
                'k': 39, 'l': 40, 'm': 41, 'n': 42, 'o': 43, 'p': 44, 'q': 45, 'r': 46, 's': 47, 't': 48,
                'u': 49, 'v': 50, 'w': 51, 'x': 52, 'y': 53, 'z': 54,
                'META_ALT_LEFT_ON': 16,
                'META_ALT_MASK': 50,
                'META_ALT_ON': 2,
                'META_ALT_RIGHT_ON': 32,
                'META_CAPS_LOCK_ON': 1048576,
                'META_CTRL_LEFT_ON': 8192,
                'META_CTRL_MASK': 28672,
                'META_CTRL_ON': 4096,
                'META_CTRL_RIGHT_ON': 16384,
                'META_FUNCTION_ON': 8,
                'META_META_LEFT_ON': 131072,
                'META_META_MASK': 458752,
                'META_META_ON': 65536,
                'META_META_RIGHT_ON': 262144,
                'META_NUM_LOCK_ON': 2097152,
                'META_SCROLL_LOCK_ON': 4194304,
                'META_SHIFT_LEFT_ON': 64,
                'META_SHIFT_MASK': 193,
                'META_SHIFT_ON': 1,
                'META_SHIFT_RIGHT_ON': 128,
                'META_SYM_ON': 4,
                'KEYCODE_APOSTROPHE': 75,
                'KEYCODE_AT': 77,
                'KEYCODE_BACKSLASH': 73,
                'KEYCODE_COMMA': 55,
                'KEYCODE_EQUALS': 70,
                'KEYCODE_GRAVE': 68,
                'KEYCODE_LEFT_BRACKET': 71,
                'KEYCODE_MINUS': 69,
                'KEYCODE_PERIOD': 56,
                'KEYCODE_PLUS': 81,
                'KEYCODE_POUND': 18,
                'KEYCODE_RIGHT_BRACKET': 72,
                'KEYCODE_SEMICOLON': 74,
                'KEYCODE_SLASH': 76,
                'KEYCODE_STAR': 17,
                'KEYCODE_SPACE': 62,
                'KEYCODE_TAB': 61,
                'KEYCODE_ENTER': 66,
                'KEYCODE_ESCAPE': 111,
                'KEYCODE_CAPS_LOCK': 115,
                'KEYCODE_CLEAR': 28,
                'KEYCODE_PAGE_DOWN': 93,
                'KEYCODE_PAGE_UP': 92,
                'KEYCODE_SCROLL_LOCK': 116,
                'KEYCODE_MOVE_END': 123,
                'KEYCODE_MOVE_HOME': 122,
                'KEYCODE_INSERT': 124,
                'KEYCODE_SHIFT_LEFT': 59,
                'KEYCODE_SHIFT_RIGHT': 60,
                'KEYCODE_F1': 131,
                'KEYCODE_F2': 132,
                'KEYCODE_F3': 133,
                'KEYCODE_F4': 134,
                'KEYCODE_F5': 135,
                'KEYCODE_F6': 136,
                'KEYCODE_F7': 137,
                'KEYCODE_F8': 138,
                'KEYCODE_F9': 139,
                'KEYCODE_F10': 140,
                'KEYCODE_F11': 141,
                'KEYCODE_F12': 142,
                'KEYCODE_BACK': 4,
                'KEYCODE_CALL': 5,
                'KEYCODE_ENDCALL': 6,
                'KEYCODE_CAMERA': 27,
                'KEYCODE_FOCUS': 80,
                'KEYCODE_VOLUME_UP': 24,
                'KEYCODE_VOLUME_DOWN': 25,
                'KEYCODE_VOLUME_MUTE': 164,
                'KEYCODE_MENU': 82,
                'KEYCODE_HOME': 3,
                'KEYCODE_POWER': 26,
                'KEYCODE_SEARCH': 84,
                'KEYCODE_NOTIFICATION': 83,
                'KEYCODE_NUM': 78,
                'KEYCODE_SYM': 63,
                'KEYCODE_SETTINGS': 176,
                'KEYCODE_DEL': 67,
                'KEYCODE_FORWARD_DEL': 112,
                'KEYCODE_NUMPAD_0': 144,
                'KEYCODE_NUMPAD_1': 145,
                'KEYCODE_NUMPAD_2': 146,
                'KEYCODE_NUMPAD_3': 147,
                'KEYCODE_NUMPAD_4': 148,
                'KEYCODE_NUMPAD_5': 149,
                'KEYCODE_NUMPAD_6': 150,
                'KEYCODE_NUMPAD_7': 151,
                'KEYCODE_NUMPAD_8': 152,
                'KEYCODE_NUMPAD_9': 153,
                'KEYCODE_NUMPAD_ADD': 157,
                'KEYCODE_NUMPAD_COMMA': 159,
                'KEYCODE_NUMPAD_DIVIDE': 154,
                'KEYCODE_NUMPAD_DOT': 158,
                'KEYCODE_NUMPAD_EQUALS': 161,
                'KEYCODE_NUMPAD_LEFT_PAREN': 162,
                'KEYCODE_NUMPAD_MULTIPLY': 155,
                'KEYCODE_NUMPAD_RIGHT_PAREN': 163,
                'KEYCODE_NUMPAD_SUBTRACT': 156,
                'KEYCODE_NUMPAD_ENTER': 160,
                'KEYCODE_NUM_LOCK': 143,
                'KEYCODE_MEDIA_FAST_FORWARD': 90,
                'KEYCODE_MEDIA_NEXT': 87,
                'KEYCODE_MEDIA_PAUSE': 127,
                'KEYCODE_MEDIA_PLAY': 126,
                'KEYCODE_MEDIA_PLAY_PAUSE': 85,
                'KEYCODE_MEDIA_PREVIOUS': 88,
                'KEYCODE_MEDIA_RECORD': 130,
                'KEYCODE_MEDIA_REWIND': 89,
                'KEYCODE_MEDIA_STOP': 86,
                }


if __name__ == '__main__':
    M = Moments(max_num_moments=120)
    M.main()
    # selenium.common.exceptions.NoSuchElementException
