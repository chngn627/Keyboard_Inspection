# 鼠标键盘监控
from pynput import keyboard, mouse
# 日志处理
from loguru import logger
# 多线程处理
from threading import Thread


logger.add('lister.log')


def on_keyboard_press(key):
    '''
    按键时记录所按下的键
    :param key:
    :return:
    '''
    logger.debug(f'{key} :被按下了')


def on_keyboard_release(key):
    '''
    释放按键处理函数
    :param key:
    :return:
    '''
    if key == keyboard.Key.esc:
        return False


def on_mouse_click(x, y, click, pressed):
    if click == mouse.Button.left:
        logger.debug('鼠标左键按下了')
    elif click == mouse.Button.right:
        logger.debug('鼠标右键按下了')
        return False
    else:
        logger.debug('中间滚轮按下了')


def func_keyboard():
    '''
    键盘的按下/释放的监听
    :return:
    '''
    with keyboard.Listener(on_press=on_keyboard_press, on_release=on_keyboard_release) as keyboard_listener:
        keyboard_listener.join()


def func_mouse_click():
    '''
    监听鼠标
    :return:
    '''
    with mouse.Listener(on_click=on_mouse_click) as mouse_listener:
        mouse_listener.join()


if __name__ == '__main__':
    '''
    执行线程
    '''
    # 定义键盘监听线程
    thread_keyboard = Thread(target=func_keyboard)
    # 定义鼠标监听线程
    thread_mouse = Thread(target=func_mouse_click)
    # 分别启动线程
    thread_keyboard.start()
    thread_mouse.start()


