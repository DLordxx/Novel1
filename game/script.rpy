# Определение персонажей игры.
define d = Character('Денис', color="#5a11ad")
define t = Character('Александр', color="#1ab85e")
define e = Character('Элина', color="#c4149b")
define s = Character('Станислав', color="#1a21eb")
define u = Character('Ян', color="#ba1125")

#Выбор, который влияет на сюжет
define koncovka = False
# Задаётся изначальная позиция персонажей
init:
    $ left = Position(xalign=0.4)
    $ right = Position(xalign=0.8)
# Игра начинается здесь:
label start:
# Первая сцена в аудитории
    scene bg class
# Резкое появление/исчезновение
    with fade
    '''
    Авторское повествование для погружения в мир игры

    Люблю чипсики

    Рофл
    '''

    show an
# Постепенное появление/исчезновение
    with dissolve
    u "Рассказывает про 19 век"
    hide an with dissolve
# Слова автора (добавить шум,
    "Начало перемены"

    show den at right
    show alek:
        xalign 0.35
    with dissolve
    d "Привет, мои друзья, как у вас дела?"
    t "Хорошо, у меня сегодня прилив энергии, может куда-нибудь сходим?"
    d "Говорю что иду в библиотеку"
    t "Что-то говорит напоследок"
    hide den with dissolve

# Перемещение в коридор вуза
    scene bg corridor
    with fade
    show lina at right
    with dissolve
    e "Замечательно, так как сегодня будет мой любимый предмет - литература (говорит о своём)"
    show den at left
    with easeinleft
    e "Говорит Денису"
    d "Соглашаюсь пойти в библиотеку"
    hide den with dissolve

# Перемещение в библиотеку
    scene bg library
    with fade
    show den
    with dissolve
# Я один иду? - вопрос Элине
    d "Мб что-то говорю"
    "Слышится грохот"

# Смена сцены - перенос в прошлое (поезд) (слево и справа сидим-стоим)
    scene bg koridor p2
    with pixellate
# Слова автора
    '''
    Он открыл глаза, когда весь поезд был уже в овраге, под насыпью.

    Дико выли, стонали люди, обломки вагонов громоздились над мертвыми и еще живыми, и над всем свистели метели, и снег летел в небо, как дым
    '''

    show den
    with dissolve
    d "Где я? Я не понимаю, меня сильно мажет"
    hide den with dissolve
# ГГ проходит дальше по коридору и встречает Стаса (поменять фон)
    scene bg koridor p
    with fade
    show boy at right
    with dissolve
    s "Пытается поговорить с машинистом, но тот не отвечает"
    show den at left
    with dissolve
    d "Спрашиваю где я нахожусь"
    s "Рассказывает о подробностях, год"
    hide boy with dissolve

#Основной выбор
# 1) Когда гг выпрыгивает из поезда, умирает в госпитале - просыпается в библиотеке
    scene bg jd
    with moveoutleft
    with hpunch
    '''
    {w=1}Проходит мгновение

    {w=1}Витте находит гг

    {w=1}Он отвозит его в больницу-госпиталь
    '''

    scene bg hospital
    with fade
    show den
    with dissolve
    d "Возможная реплика"
# ГГ умирает в прошлом и переносимся в библиотеку
    scene bg library
    with pixellate
    show den
    with dissolve
    d "Кто-то меня спрашивает, почему я так надолго отключился - отшучиваюсь, что это был сон"
# 2) Когда гг пытаеся всех спасти - остаётся в прошлом

# Тестовый выбор

    scene bg class
    with fade
    show lina
    with dissolve
#Выбор, который влияет и игра запоминает его
    e "Предлагаю тебе выбор влияющий на сюжет"
    menu:
        "Любишь фильмы?"

        "Да, обожаю":

            "Вы красавчик"

            $ koncovka = True

        "Нет":

            "Вы были исключены из классной беседы"

#Выбор, который влияет на ход событий, но игра это не запомнит (развилка)
    menu:
        "Выбери что-нибудь"

        "Вариант 1":
            jump vibor1

        "Вариант 2":
            jump vibor2

    return

label vibor1:

    "Вы выбрали первый вариант"

    return

label vibor2:


    if koncovka:
        "Охаё"
    else:
        "Доброе утро"
    return
