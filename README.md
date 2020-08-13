<h1>Простое приложение Django для ведения блога</h1>

<h2>Административная часть</h2> 
<p>В административной части сайта реализованы следующие возможности:</p>
<ul>
    <li>Управление данными приложения (стандартная админка Django)</li>
    <li>Назначение прав управления контентом:
        <ul>
            <li>Одобрить (опубликовать) статью</li>
            <li>Удалить статью</li>
            <li>Отредактировать статью</li>
            <li>Одобрить (опубликовать) комментарий</li>
        </ul>
</ul>

<h2>Пользовательская часть</h2>
<p>Для посетителей сайта доступны следующие возможности:</p>
<h4>Неавторизованный посетитель</h4>
<ul>
    <li>Просматривать статьи</li>
    <li>Просматривать комментарии</li>
    <li>Авторизоваться</li>
</ul>
<h4>Авторизованный пользователь</h4>
<ul>
    <li>Просматривать статьи</li>
    <li>Просматривать комментарии</li>
    <li>Создавать статьи</li>
    <li>Редактировать свои статьи</li>
    <li>Оставлять комментарии к статьям</li>
</ul>
<h4>Авторизованный пользователь с правами администрирования</h4>
<ul>
    <li>Просматривать статьи</li>
    <li>Просматривать комментарии</li>
    <li>Создавать статьи</li>
    <li>Публиковать (одобрять) созданные статьи</li>
    <li>Редактировать свои статьи</li>
    <li>Удалять статьи</li>
    <li>Оставлять комментарии к статьям</li>
    <li>Публиковать (одобрять) комментарии к статьям</li>
</ul>
