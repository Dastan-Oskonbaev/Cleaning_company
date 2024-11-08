# Указывает Docker использовать официальный образ python 3 с dockerhub в качестве базового образа
FROM python:3.11
# Устанавливает переменную окружения, которая гарантирует, что вывод из python будет отправлен прямо в терминал без предварительной буферизации
ENV PYTHONUNBUFFERED 1
# Устанавливает рабочий каталог контейнера — "app"
WORKDIR /app
# Копирует все файлы из нашего локального проекта в контейнер
ADD . /app
# Запускает команду pip install для всех библиотек, перечисленных в requirements.txt
RUN pip install -r requirements.txt
# Установка Gunicorn
RUN pip install gunicorn
# Запускает команду makemigrations для создания файлов миграции на основе изменений в моделях
RUN python manage.py makemigrations
# Команда для запуска Gunicorn
CMD ["gunicorn", "--workers=4", "congig.wsgi:application", "--bind", "0.0.0.0:8000"]
