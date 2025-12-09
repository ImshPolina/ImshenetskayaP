import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from tkinter import scrolledtext

class GUIApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Имшенецкая Полина Алексеевна")
        self.root.geometry("700x500")
        
        # Создаем вкладки
        self.tab_control = ttk.Notebook(root)
        
        # Вкладка 1: Калькулятор
        self.tab1 = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab1, text='Калькулятор')
        self.create_calculator_tab()
        
        # Вкладка 2: Чекбоксы
        self.tab2 = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab2, text='Выбор варианта')
        self.create_checkbox_tab()
        
        # Вкладка 3: Работа с текстом
        self.tab3 = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab3, text='Текст из файла')
        self.create_text_tab()
        
        self.tab_control.pack(expand=1, fill='both')
    
    def create_calculator_tab(self):
        # Ввод первого числа
        tk.Label(self.tab1, text="Первое число:").grid(row=0, column=0, padx=10, pady=10)
        self.num1_entry = tk.Entry(self.tab1)
        self.num1_entry.grid(row=0, column=1, padx=10, pady=10)
        
        # Выбор операции
        tk.Label(self.tab1, text="Операция:").grid(row=1, column=0, padx=10, pady=10)
        self.operation_var = tk.StringVar(value="+")
        operations = ["+", "-", "*", "/"]
        self.operation_menu = ttk.Combobox(self.tab1, textvariable=self.operation_var, values=operations, state="readonly")
        self.operation_menu.grid(row=1, column=1, padx=10, pady=10)
        
        # Ввод второго числа
        tk.Label(self.tab1, text="Второе число:").grid(row=2, column=0, padx=10, pady=10)
        self.num2_entry = tk.Entry(self.tab1)
        self.num2_entry.grid(row=2, column=1, padx=10, pady=10)
        
        # Кнопка вычисления
        calc_button = tk.Button(self.tab1, text="Вычислить", command=self.calculate)
        calc_button.grid(row=3, column=0, columnspan=2, pady=20)
        
        # Поле результата
        self.result_label = tk.Label(self.tab1, text="Результат: ")
        self.result_label.grid(row=4, column=0, columnspan=2, pady=10)
    
    def calculate(self):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            op = self.operation_var.get()
            
            if op == "+":
                result = num1 + num2
            elif op == "-":
                result = num1 - num2
            elif op == "*":
                result = num1 * num2
            elif op == "/":
                if num2 == 0:
                    raise ZeroDivisionError
                result = num1 / num2
            else:
                result = "Неизвестная операция"
            
            self.result_label.config(text=f"Результат: {result}")
        except ValueError:
            messagebox.showerror("Ошибка", "Введите числа")
        except ZeroDivisionError:
            messagebox.showerror("Ошибка", "Деление на ноль")
    
    def create_checkbox_tab(self):
        self.check_vars = []
        options = ["Первый", "Второй", "Третий"]
        
        for i, option in enumerate(options):
            var = tk.BooleanVar()
            chk = tk.Checkbutton(self.tab2, text=option, variable=var)
            chk.grid(row=i, column=0, padx=20, pady=10, sticky='w')
            self.check_vars.append((option, var))
        
        # Кнопка выбора
        select_button = tk.Button(self.tab2, text="Показать выбор", command=self.show_selection)
        select_button.grid(row=len(options), column=0, pady=20)
    
    def show_selection(self):
        selected = [option for option, var in self.check_vars if var.get()]
        if selected:
            messagebox.showinfo("Выбор", f"Вы выбрали: {', '.join(selected)}")
        else:
            messagebox.showinfo("Выбор", "Вы ничего не выбрали")
    
    def create_text_tab(self):
        # Меню
        menubar = tk.Menu(self.tab3)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Загрузить файл", command=self.load_file)
        menubar.add_cascade(label="Файл", menu=file_menu)
    
        self.root.config(menu=menubar)
        
        # Текстовое поле с прокруткой
        self.text_area = scrolledtext.ScrolledText(self.tab3, wrap=tk.WORD, width=70, height=20)
        self.text_area.pack(padx=10, pady=10, fill='both', expand=True)
    
    def load_file(self):
        file_path = filedialog.askopenfilename(
            title="Выберите файл",
            filetypes=(("Текстовые файлы", "*.txt"), ("Все файлы", "*.*"))
        )
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, content)
            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось загрузить файл:\n{e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = GUIApp(root)
    root.mainloop()