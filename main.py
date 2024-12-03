import os
import platform
import time

import pyautogui

# Словарь путей к изображениям кнопок
os_choice = {
    'Windows': {'10': './windows10/', '11': './windows11/'},
    'Darwin': './macos/',
    'Linux': './linux/',
}


def open_calculator(system: str) -> None:
    """Открывает приложение 'Калькулятор' в зависимости от операционной системы."""

    if system == 'Windows':
        os.system('start calc')
    elif system == 'Darwin':
        os.system('open -a Calculator')
    elif system == 'Linux':
        os.system('gnome-calculator')
    else:
        raise Exception('Операционная система не поддерживается.')
    print(f'ОС: {platform.system()}, версия: {platform.release()}')
    time.sleep(2)


def get_image_directory(system: str, release: str) -> str:
    """Возвращает директорию для изображений кнопок в зависимости от ОС."""

    if system == 'Windows':
        if '10' in release:
            return os_choice['Windows']['10']
        elif '11' in release:
            return os_choice['Windows']['11']
        else:
            raise Exception(f'Версия Windows {release} не поддерживается.')
    elif system in os_choice:
        return os_choice[system]
    else:
        raise Exception(f'Операционная система {system} не поддерживается.')


def click_button(image_path: str) -> None:
    """Ищет на экране кнопку с изображением и кликает по ней."""

    try:
        location = pyautogui.locateOnScreen(
            image_path, confidence=0.9, grayscale=True
            )
        if location is None:
            raise Exception(f'Кнопка {image_path} не найдена на экране.')
        pyautogui.click(pyautogui.center(location))
    except pyautogui.ImageNotFoundException:
        raise Exception(f'Ошибка поиска изображения: {image_path}')


def main():
    """Открывает приложение 'калькулятор' и нажимает соответствующие кнопки."""
    system = platform.system()
    release = platform.release()

    open_calculator(system)

    button_dir = get_image_directory(system, release)

    click_button(f'{button_dir}1.png')  # Кнопка '1'
    click_button(f'{button_dir}2.png')  # Кнопка '2'
    click_button(f'{button_dir}+.png')  # Кнопка '+'
    click_button(f'{button_dir}7.png')  # Кнопка '7'
    click_button(f'{button_dir}=.png')  # Кнопка '='


if __name__ == '__main__':
    main()
