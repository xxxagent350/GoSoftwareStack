import sys
from gui.app import DarkApp

# Включаем поддержку высокого разрешения (DPI Awareness) для четкости на 4K
if sys.platform == 'win32':
    try:
        import ctypes
        ctypes.windll.shcore.SetProcessDpiAwareness(1)
    except Exception:
        try:
            ctypes.windll.user32.SetProcessDPIAware()
        except Exception:
            pass

if __name__ == "__main__":
    app = DarkApp()
    app.mainloop()
