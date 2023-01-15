## Целью данного задания является изучение изменения уровня CpG метилирования ДНК при раннем эмбриональном развитии мыши.

[Ссылка на README на русском](README.ru.md)

Ожидается, что на ранних стадиях CpG метилирование находится на уровне минимума (25%), после чего увеличивается до 90% и остаётся таким на протяжении жизни.
Тут рассматриваются три стадии развития мыши в течение первой недели после оплодотворения:
8cell - 8-клеточный эмбрион (SRR5836473)
ICM - Inner cell mass (SRR5836475)
Epiblast - стадия эпибласта (SRR3824222)

Все команды были выполнены в терминале Linux.
Скриншоты и текст этого - в папке proof.

Статистика по числу ридов:
|Число ридов в области|8 cell|Epiblast|ICM|
|---|---|---|---|
|11347700-11367700|1090|2328|1456|
|40185800-40195800|464|1062|630|

Статистика по дупликациям:
|Дупликации|8 cell|Epiblast|ICM|
|---|---|---|---|
|Число|521904|205258|377882|
|Процент|18.31%|2.92%|9.08%|

Bismark отчёты:

# Для стадии 8 cell:

![Screenshot from 2022-02-21 23-19-23](https://user-images.githubusercontent.com/60808642/155021722-6951c6c3-5e32-4967-9657-dfedfcc57a30.png)
![Screenshot from 2022-02-21 23-19-35](https://user-images.githubusercontent.com/60808642/155021789-77457d7c-aa6a-4645-8de5-8dee04d1b039.png)
![Screenshot from 2022-02-21 23-19-46](https://user-images.githubusercontent.com/60808642/155022644-3ae240da-5446-48ee-a86e-d1e87ed416e8.png)
![8 cell](https://user-images.githubusercontent.com/60808642/154995957-dc9efa1d-071c-4730-b5c7-944dfc09734d.png)

# Для стадии ICM:
![Screenshot from 2022-02-21 23-25-40](https://user-images.githubusercontent.com/60808642/155022349-1d4dc970-862b-42d6-ae3d-9bf1ad4eb421.png)
![Screenshot from 2022-02-21 23-25-44](https://user-images.githubusercontent.com/60808642/155022395-92853f91-ae9d-4c02-9215-f27e2c8121a7.png)
![Screenshot from 2022-02-21 23-23-28](https://user-images.githubusercontent.com/60808642/155022558-b09e6244-bddb-41c1-8672-bd488f7f9bf6.png)
![ICM](https://user-images.githubusercontent.com/60808642/154996003-66df01e7-bf5b-44d6-8954-4b69a1369f98.png)

# Для стадии Epiblast:
![Screenshot from 2022-02-21 23-23-21](https://user-images.githubusercontent.com/60808642/155022052-902b45c4-9fb2-42ac-9e80-533176be13ae.png)
![Screenshot from 2022-02-21 23-23-25](https://user-images.githubusercontent.com/60808642/155022061-513f568a-6754-4123-bacb-6dfa764424ba.png)
![Screenshot from 2022-02-21 23-23-28](https://user-images.githubusercontent.com/60808642/155022071-cc8e424b-6c6d-4bda-997b-7ddbe56238a0.png)
![Epiblast](https://user-images.githubusercontent.com/60808642/154995981-bb2dd211-e909-40a8-a5da-a3fbc257a0e0.png)

Как видно, максимальный уровень CpG метилирования наблюдается на стадии эпибласта. Чуть ниже на стадии 8 клеток и совсем низкая на стадии между ними, что в целом соответствует ожиданиям.

# Гистограммы метилированных цитозинов

Были построены с помощью скрипта на python (папке src).
По оси X указан процент метилированных цитозинов, по оси Y - частота метилирования.

![hw1_eight_cell](https://user-images.githubusercontent.com/60808642/195834753-ddbf1012-3528-40c0-aea5-52bbf1cb9cb8.png)
![hw1_icm](https://user-images.githubusercontent.com/60808642/195834777-7944f5a7-b90c-468f-8c9a-c97b76ef05ae.png)
![hw1_epiblast](https://user-images.githubusercontent.com/60808642/195834791-d17f723d-4748-4ac0-bbaf-9d75b209d301.png)

Из этих диаграмм видно, что неметилированных участков чуть больше, чем метилированных на первой стадии (8 cell), значительно больше на второй стадии (icm) и совсем мало на третьей стадии (epiblast). Процент частично метилированных участков не столь высок для всех образцов.

Наконец, визуализировали уровень метилирования и покрытия для каждого образца (папка methylation) с помощью pyGenomeTracks.
Получили 6 диаграмм следующего вида:

![epiblast_11327700-11367700_met](https://user-images.githubusercontent.com/60808642/195835635-53ba3c3b-2ac1-4395-826b-90482be2f3ab.png)
