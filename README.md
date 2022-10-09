![Header](header.png)

## Команда
- [Никита Мастинен](https://t.me/AccNFR) - бэкенд
- [Павел Курочкин](https://t.me/curlink19) - бэкенд
- [Анна Хайтина](https://t.me/anna_khaytina) - дизайн
- [Платон Лапп](https://t.me/SeamMiner) - фронтенд
- [Александр Щеблыкин](https://t.me/greeneboy) - десигн

## О проекте

**ВТБ.Коллеги** — это сервис который помогает руководителям и их сотрудникам участвовать во внутрикорпоративных активностостях в простой и понятной форме.

### Ключевые особенности
- Сотрудникам начисляются цифровые рубли за участие в мероприятиях, таких как менторинг, прохождение обязательных курсов, митапов, фокус-групп, исследований.
- Чем больше мероприятий посещает сотрудник, тем выше его коэффициент и размер награды в цифровых рублях.
- Выданные сотрудникам NFT карточки можно обменять на мерч в маркетплейсе
- ВТБ коллеги использует PWA архитектуру, которая позволяет уменьшить затраты на разработку, при этом давая пользователю возможность взаимодействовать сервисом как с компьютера, так и с телефона в виде мобильного приложения.


## Технологический стэк

- [Fast API](https://fastapi.tiangolo.com/) -  веб-фреймворк для создания API на языке Python
- [Vue 3](https://v3.ru.vuejs.org/) - прогрессивный JavaScript-фреймворк для создания фронтенда веб-приложения
- [Vuex](https://vuex.vuejs.org/ru/) - официальный менеджер состояний для VueJS
- [Router](https://router.vuejs.org/ru/) - официальный маршрутизатор для VueJS
- [TypeScript](https://www.typescriptlang.org/) - типизированный JavaScript, позволяющий отлавливать ошибки до запуска кода


## Демо

[Ссылка на видео](https://drive.google.com/file/d/18p5yCJzgwyBo9lMYQ1ArEuaAi56l-TSg/view)

## Локальный запуск

```bash
git clone https://github.com/nmbits-hackathons/vtbhack.git && cd vtbhack

# Start API
cd backend
python3 -m venv env
source ./env/bin/activate  # WIN: "env\Scripts\activate"
pip install -r requirements.txt
python manage.py runserver

# Start frontend
cd ../frontend
yarn && yarn serve
```

