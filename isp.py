import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import cv2
import threading
import os
import shutil


# Функция вычисления остроты изображения
def calculate_sharpness(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    laplacian_var = cv2.Laplacian(gray, cv2.CV_64F).var()
    return laplacian_var


# Функция обработки изображений в отдельном потоке
def process_images_threaded(folder_path, threshold, recursive):
    global blurred_folder_path

    # Подсчет общего количества изображений для прогрессбара
    total_files = 0
    for root, _, files in os.walk(folder_path):
        if root == blurred_folder_path:
            continue
        total_files += sum(1 for file in files if file.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif')))
        if not recursive:
            break

    app.progress['maximum'] = total_files
    processed_files = 0

    for root, _, files in os.walk(folder_path):
        if root == blurred_folder_path:
            continue
        for file in files:
            if file.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif')):
                image_path = os.path.join(root, file)
                try:
                    image = cv2.imread(image_path)
                    if image is not None:
                        sharpness = calculate_sharpness(image)
                        log_message(f"Processing {image_path} - Sharpness: {sharpness}")

                        if sharpness < threshold:
                            blurred_image_path = os.path.join(blurred_folder_path, file)
                            shutil.move(image_path, blurred_image_path)  # Move and delete from original folder
                            log_message(f"Moved blurred image to {blurred_image_path}")
                    processed_files += 1
                    app.progress['value'] = processed_files
                except Exception as e:
                    log_message(f"Error processing {image_path}: {e}")
        if not recursive:
            break

    log_message("Processing completed successfully.")


# Функция логирования сообщений
def log_message(message):
    app.log_text.config(state='normal')
    app.log_text.insert('end', message + '\n')
    app.log_text.see('end')
    app.log_text.config(state='disabled')


# Функция запуска обработки
def start_processing():
    global blurred_folder_path
    folder_path = app.photos_folder.get()
    threshold = sharpness_threshold
    recursive = bool(app.recursive_search_var.get())

    if not os.path.exists(folder_path):
        log_message("The specified directory does not exist.")
        return

    blurred_folder_path = os.path.join(folder_path, "blurred_images")
    if not os.path.exists(blurred_folder_path):
        os.makedirs(blurred_folder_path)

    threading.Thread(target=process_images_threaded, args=(folder_path, threshold, recursive)).start()


# Параметры по умолчанию
sharpness_threshold = 100
recursive_search_default = 1


# Создание и запуск приложения
class ImageProcessorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Image Processor")

        # Виджеты для выбора директории
        tk.Label(self, text="Directory:").grid(row=0, column=0, padx=10, pady=5)
        self.photos_folder = tk.Entry(self, width=60)
        self.photos_folder.grid(row=0, column=1, padx=10, pady=5)
        browse_button = tk.Button(self, text="Browse", command=self.browse_folder)
        browse_button.grid(row=0, column=2, padx=10, pady=5)

        # Виджет для выбора порогового значения остроты
        tk.Label(self, text="Sharpness Threshold:").grid(row=1, column=0, padx=10, pady=5)
        self.sharpness_entry = tk.Entry(self, width=20)
        self.sharpness_entry.grid(row=1, column=1, padx=10, pady=5)
        self.sharpness_entry.insert(0, str(sharpness_threshold))

        # Виджет для выбора рекурсивного поиска
        self.recursive_search_var = tk.IntVar(value=recursive_search_default)
        recursive_checkbutton = tk.Checkbutton(self, text="Recursive Search", variable=self.recursive_search_var)
        recursive_checkbutton.grid(row=2, column=1, padx=10, pady=5)

        # Кнопка запуска обработки
        start_button = tk.Button(self, text="Start Processing", command=start_processing)
        start_button.grid(row=3, column=1, pady=10)

        # Прогрессбар
        self.progress = ttk.Progressbar(self, orient='horizontal', length=450, mode='determinate')
        self.progress.grid(row=4, column=0, columnspan=3, padx=10, pady=5)

        # Журнал логов с прокруткой
        log_frame = tk.Frame(self)
        log_frame.grid(row=5, column=0, columnspan=3, padx=10, pady=5)

        scrollbar = tk.Scrollbar(log_frame, orient='vertical')
        self.log_text = tk.Text(log_frame, height=12, width=80, yscrollcommand=scrollbar.set, wrap='word',
                                font=('Arial', 10))
        scrollbar.config(command=self.log_text.yview)

        self.log_text.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')
        scrollbar.grid(row=0, column=1, sticky='ns')

        log_frame.grid_rowconfigure(0, weight=1)
        log_frame.grid_columnconfigure(0, weight=1)

    # Функция выбора папки через диалоговое окно
    def browse_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.photos_folder.delete(0, tk.END)
            self.photos_folder.insert(0, folder_path)


# Создание и запуск приложения
app = ImageProcessorApp()
app.mainloop()