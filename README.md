# python_web-review

- проект пока что лежит в ветки web-review т.к. это MVP
- проект выполняет скрапинг сайта: https://animestars.org
- поднятие: bash build.sh
- после остановки нужно выполнить: docker-compose down
	
## Скрапинг
- При запуске выполняется скрапинг первых двух страниц сайта. 
- После каждые 3 минуты база обновляется на данные рандомно выбранных двух страниц  (на сайте всего 76 страниц)
>p.s. пока есть проблема с тем что при запуске в базе создаются записи с данными с первых двух страниц, соответственно при перезапуске данные начинают накапливаться, но я придумаю что с этим делать

## Сервис
- Веб представляет собой мини-сайт на flask. 
- Все иконки работают и перенаправляют на страницы с подробной информацией о представленных анимэ.
	
## Хранение данных
- Данные хранятся в sqlite. 
- При запуске build.sh создается файл базы и таблица в ней, если еще не существуют.
- Также база данных на локальном хосте соединена с базой в докере, поэтому при отключение докера данные в базе остаются.
>p.s. попробую переписать на PostgresSQL, но пока только так
