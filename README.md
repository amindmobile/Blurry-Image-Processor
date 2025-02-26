## Image Processor

### Описание

Image Processor — это простое приложение, написанное на Python с использованием библиотеки Tkinter для графического интерфейса и стандартной библиотеки os для работы с файловой системой. Приложение позволяет обрабатывать изображения в указанной директории, определяя их резкость и перемещая размытые изображения в отдельную папку.

Установка
Для запуска приложения убедитесь, что у вас установлен Python версии 3.x. Приложение не требует дополнительных библиотек помимо стандартной библиотеки Python и Tkinter, который обычно доступен в стандартном дистрибутиве.

### Функциональность
Выбор директории: Пользователь может выбрать директорию с изображениями через графический интерфейс.
Порог остроты: Можно задать пороговое значение для определения размытых изображений. Изображения, которые не соответствуют этому критерию, перемещаются в папку blurred_images внутри выбранной директории.
Рекурсивный поиск: Приложение может выполнять рекурсивный поиск по всем поддиректориям для обработки всех изображений.
### Использование
Запустите приложение, дважды кликнув на файл script.py.
Выберите директорию с изображениями через графический интерфейс.
Установите пороговое значение остроты (по умолчанию 100).
Выберите опцию рекурсивного поиска, если необходимо.
Нажмите кнопку "Start Processing" для начала обработки изображений.
### Пример
python script.py

### Image Processor

### Description
Image Processor is a simple application written in Python using the Tkinter library for the graphical interface and standard os library for file system operations. The application allows processing images in a specified directory, determining their sharpness and moving blurry images to a separate folder.

### Installation
To run the application, ensure you have Python version 3.x installed. The application does not require additional libraries beyond the standard Python library and Tkinter, which is usually available in the standard distribution.

### Functionality
Directory selection: Users can select an image directory through the graphical interface.
Sharpness threshold: You can set a threshold value to determine blurry images. Images that do not meet this criterion are moved to the blurred_images folder inside the selected directory.
Recursive search: The application can perform recursive searches in all subdirectories to process all images.
### Usage
Start the application by double-clicking on the script.py file.
Select an image directory through the graphical interface.
Set the sharpness threshold (default is 100).
Select the recursive search option if necessary.
Click the "Start Processing" button to begin processing images.
### Example
python script.py
