import requests
import json
import tkinter as tk
from tkinter import messagebox

def fetch_github_data():
    input_text = entry.get().strip()
    if not input_text:
        messagebox.showwarning("Ошибка", "Введите owner/repo")
        return
    

    owner, repo = input_text.split('/', 1)
    url = f"https://api.github.com/repos/{owner}/{repo}"

    response = requests.get(url)
    response.raise_for_status()
    user_data = response.json()
    required_fields = ['company', 'created_at', 'email', 'id', 'name', 'url']
    filtered_data = {field: user_data.get(field) for field in required_fields}
    
    #сохранение
    output_filename = f"github_{input_text.replace('/', '_')}_data.json"
    with open(output_filename, 'w', encoding='utf-8') as f:
        json.dump(filtered_data, f, indent=4, ensure_ascii=False)

    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, json.dumps(filtered_data, indent=4, ensure_ascii=False))
    messagebox.showinfo("Успех", f"Данные сохранены в файл: {output_filename}")

# графический интерфейс
root = tk.Tk()

label = tk.Label(root, text="Введите имя репозитория (например: apache/spark):", 
                 wraplength=550)
label.pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack(pady=5)

fetch_button = tk.Button(root, text="Получить данные", command=fetch_github_data)
fetch_button.pack(pady=10)

result_label = tk.Label(root, text="Результат:")
result_label.pack(pady=10)

result_text = tk.Text(root, height=15, width=70)
result_text.pack(pady=10)


root.mainloop()