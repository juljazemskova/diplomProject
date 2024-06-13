# :briefcase: Это дипломный проект на тему «Модель прогнозирования стоимости жилья для агентства недвижимости»

## Оглавление  
[1. Описание проекта](#Описание-проекта)  

[2. Входные данные](#Входные-данные) 

[3. Краткая информация о данных](#Краткая-информация-о-данных) 

[4. Выводы](#Выводы) 

### Описание проекта
Поставлена задача от агенства недвижимости  разработать модель, которая позволила бы агентству недвижимости обойти конкурентов по скорости и качеству совершения
сделок

### Входные данные
Предстоит работать с датасетом, в котором содержатся сведения о 377 тысячах лотах недвижимости в USA, выставленных на продажу. 


### Краткая информация о данных
- Датасет содержит данные об объектах недвижимости США на [ресурсе](https://drive.google.com/file/d/11-ZNNIdcQ7TbT8Y0nsQ3Q0eiYQP__NIW/view?usp=share_link) 
- Project_final.ipynb - Jupiter Notebook с основным проектом на [ресурсе](https://colab.research.google.com/drive/1tSu3s3X5kcgbM_Ky2Vo6oQLDaK2R5hLB?usp=sharing) 
- Project_new.ipynb - Jupiter Notebook с  несколько изменённой версией проекта (более тщательно проведён EDA, но с худшими метриками во время обучения) на [ресурсе](https://colab.research.google.com/drive/1smk0XFtpbOJS--zm6HoKDLEX3Qj36VSW?usp=sharing) 
- uscities.csv - датасет с данными по американским городам по [адрессу](https://drive.google.com/file/d/1kgmEtk9I-bHu2kz-kZ9-KjrKauvGjJ2A/view?usp=sharing)
- server.py - сервер на Flask
- client.py - клиент для тестирования
- сериализованная модель(best_model.pkl) размещена по [адресу](https://drive.google.com/file/d/1mj4t90CSEgCONQNSUWwdpOZxVpnXp8ry/view?usp=sharing)
-  сериализованная модель(diplom_pipeline.pkl) размещена по [адресу](https://drive.google.com/file/d/1QETH_4yOUgCtdTJQrlb_Y7y7xCKC2EB-/view?usp=sharing)
-  requirements.txt  - файл с необходимыми зависимостями
-  app.py - сервер в браузере
-  index.html - разметка страницы в браузере 

### Выводы:
В процесе работы над проектом был проведен базовый и разведывательный (EDA) анализ структуры исходных данных, созданы новые признаки. Протестировано несколько моделей машинного обучения. В результате была решена задача регрессии, с подобранной оптимальной моделью. После этого разработан веб-сервис, на вход которому поступают данные о выставленной на продажу недвижимости, а сервис прогнозирует её стоимость.

:arrow_up:[к оглавлению](#Оглавление)
