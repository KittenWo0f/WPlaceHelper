import time
from pynput import mouse, keyboard
from pynput.mouse import Button

class WPlaceHelper:
    def __init__(self):
        self.mouse_controller = mouse.Controller()
        self.keyboard_controller = keyboard.Controller()
        
    def setup_wplace_distance(self):
        """Настройка отдаления камеры wplace"""
        # Максимальное приближение
        for _ in range(50):
            self.mouse_controller.scroll(0, 1)
            time.sleep(0.01)
        # Отдаление на 14 шагов
        for _ in range(14):
            self.mouse_controller.scroll(0, -1)
            time.sleep(0.1)

    def paint_wplace(self, x, y):
        """Рисование на wplace с перемещением курсора"""
        self.keyboard_controller.press('i')
        time.sleep(0.06)
        self.mouse_controller.press(Button.left)
        time.sleep(0.06)
        self.mouse_controller.release(Button.left)
        time.sleep(0.06)
        self.mouse_controller.press(Button.left)
        time.sleep(0.06)
        self.mouse_controller.release(Button.left)
        time.sleep(0.06)
        self.mouse_controller.move(x, y)

    def paint_up(self):
        """Рисование вверх"""
        self.paint_wplace(0, -41)
        
    def paint_left(self):
        """Рисование влево"""
        self.paint_wplace(-41, 0)
        
    def paint_down(self):
        """Рисование вниз"""
        self.paint_wplace(0, 41)
        
    def paint_right(self):
        """Рисование вправо"""
        self.paint_wplace(41, 0)

def main():
    wplace_helper = WPlaceHelper()
    
    print("=" * 50)
    print("🎨 WPLACE HELPER")
    print("=" * 50)
    print("• Q - настроить отдаление камеры wplace")
    print("• W - рисовать вверх")
    print("• A - рисовать влево")
    print("• S - рисовать вниз")
    print("• D - рисовать вправо")
    print("• Ctrl + C - Выход")
    print("=" * 50)
    print("⏳ Ожидание команд...")
    
    # Настройка горячих клавиш
    with keyboard.GlobalHotKeys({
        'q': wplace_helper.setup_wplace_distance,
        'w': wplace_helper.paint_up,
        'a': wplace_helper.paint_left,
        's': wplace_helper.paint_down,
        'd': wplace_helper.paint_right,
    }):
        try:
            # Основной цикл программы
            while True:
                time.sleep(0.1)
        except KeyboardInterrupt:
            print("\n👋 Завершение программы...")
            time.sleep(0.5)

if __name__ == "__main__":
    main()