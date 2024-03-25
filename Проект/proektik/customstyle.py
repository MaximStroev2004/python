# customstyle.py
from tkinter import ttk


class CustomStyle:
    def configure_styles(self, master):
        style = ttk.Style(master)
    @staticmethod
    def configure_styles(root):
        # Настройка цветов и шрифтов для приложения
        root.configure(bg='#8A2BE2')
        root.option_add('*TCombobox*Listbox*Background', '#2F4F4F')
        root.option_add('*TCombobox*Listbox*Foreground', '#2F4F4F')
        root.option_add('*TCombobox*Listbox*Font', ('123Marker', 13))

        # Настройка стилей для ttk виджетов
        style = ttk.Style(root)

        # Основные цвета
        style.theme_create("custom_theme", parent="clam", settings={
            "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0]}},
            "TNotebook.Tab": {"configure": {"padding": [10, 5], "background": "#4CAF50"},
                              "map": {"background": [("selected", "#4CAF50")],
                                      "foreground": [("selected", "#2F4F4F")]}}
        })
        style.theme_use("custom_theme")

        # Настройка цветов для отдельных виджетов
        style.configure("Treeview", background="#9370DB", foreground="#FAEBD7")
        style.configure("TButton", background="#9370DB", foreground="#FAEBD7", font=('Gothic', 13))
        style.configure("TLabel", background="#9370DB", foreground="#FAEBD7", font=('Gothic', 13))
        style.configure("TEntry", background="#9370DB", foreground="#FAEBD7", font=('Gothic', 13))
