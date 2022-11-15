# Slash commands
* `\c` - показывает в какой бд мы находимся и через какого юзера
* `\c name_of_db` - переключаемся к этой бд
* `\l` - показывает все бд
* `\dt` - показывает все таблицы в бд, к которой мы подключились
* `\du` - показывает всех юзеров
* `\q` - выход

# Создание бд и таблиц
```sql
CREATE DATABASE name_of_db;
-- создает базу данных
```

```sql
CREATE TABLE name_of_table (
    name_of_column1 data_type constraint,
    name_of_column2 data_type constraint,
    ...
);
-- создает таблицу с полями
```

# Заполнение таблиц
```sql
INSERT INTO name_of_table (name_of_column1, name_of_column2) 
VALUES (val1, val2);
-- добавляет запись в таблицу
```

# Вывод данных из таблицы
```sql
SELECT * FROM name_of_table;
-- достает все поля и все записи из таблицы
```

```sql
SELECT name_of_column1, name_of_column2 FROM name_of_table;
-- достает только указанные столбцы из таблицы (все записи)
```

```sql
SELECT * FROM name_of_table WHERE name_of_column2 = 'hello';
-- достает все записи из таблицы у которых name_of_column2 со значением 'hello'
```

# Связи
## pk fk
> primary key (pk) - первичный ключ
> это ограничение, которое мы указваем на те поля, которые должны быть уникальными для того, чтобы потом их использовать в связях (создает btree)

> foreign key (fk) - внешний ключ
> это ограничение, которое мы указываем на те поля, которые будут ссылаться на поле с pk в другой таблице, для создания связи

```sql
CREATE TABLE author (
    id serial primary key,
    first_name varchar(50),
    last_name varchar(50)
);

CREATE TABLE book (
    id serial,
    title varchar(100),
    published year,
    author_id int,
    CONSTRAINT fk_author_book
    FOREIGN KEY (author_id)
    REFERENCES author (id)
);
```

## Виды связей (теория)
> One to one - (один к одному)
Например:

* Один флаг - одна страна
* Один человек - одно сердце
* Один автор - одна автобиография
* Один человек - один ИНН

> One to many - (один ко многим)
Например:

* Один Оомат - много поздравлений
* Одна страна - много городов
* Один пост - много комментариев
* Одна скамейка - много людей
* Один диктатор - много рабов

> Many to many - (многие ко многим)
Например:

* У студента много менторов - и у ментора много студентов
* У пользователя много социальных сетей и у одной соцсети много пользователей
* У одного доктора много пациентов и у одного пациента много докторов


## Виды связей (практика)
### One to one
```sql
CREATE TABLE flag (
    id serial primary key,
    photo text
);

CREATE TABLE country (
    id serial primary key,
    title varchar(50),
    flag_id int unique,
    CONSTRAINT fk_country_flag
    FOREIGN KEY (flag_id)
    REFERENCES flag (id)
);
```

### One to many
```sql
CREATE TABLE post (
    id serial primary key,
    title varchar(100),
    body text
);

CREATE TABLE comment (
    id serial primary key,
    body text,
    created_at datetime,
    post_id int,

    CONSTRAINT fk_post_comment
    FOREIGN KEY post_id
    REFERENCES post (id)
);
```

### Many to many
```sql
CREATE TABLE student (
    id serial primary key,
    first_name varchar(50),
    age int
);

CREATE TABLE mentor (
    id serial primary key,
    first_name varchar(50),
    age int
);

CREATE TABLE student_mentor (
    student_id int,
    mentor_id int,

    CONSTRAINT fk_student
    FOREIGN KEY (student_id)
    REFERENCES student (id),

    CONSTRAINT fk_mentor
    FOREIGN KEY (mentor_id)
    REFERENCES mentor (id)
);
```

## Join (теория)
> JOIN - инструкция, которая позволяет в запросах SELECT брать данные из нескольких связанных таблиц

> INNER JOIN (JOIN) - когда достаются только те записи, у которых есть полная связь

> FULL JOIN - когда достаются абсолютно все записи со всех таблиц (не важно есть ли свять у записи)

> LEFT JOIN - когда достаются все записи с 'левой' таблицы и так же записи с полной связью

> RIGHT JOIN - когда достаются все записи с 'правой' таблицы и так же записи с полной связью

## join (практика)
### one to one
```sql
SELECT country.title, flag.photo
FROM country
JOIN flag
ON country.flag_id = flag.id;
```

### one to many
```sql
SELECT post.title, comment.body, comment.created_at
FROM post
JOIN comment
ON post.id = comment.post_id;
```

### many to many
```sql
SELECT mentor.first_name as mentor_name, student.first_name as student_name
FROM mentor

JOIN student_mentor
ON mentor.id = student_mentor.mentor_id

JOIN student
ON student.id = student_mentor.student_id;
```

# Import / export данных
write from file to db
```bash
psql db_name < file.sql
```
write from db to file
```bash
pg_dump db_name > file.sql
```


# Агрегатные функции

> **ARRAY_AGG** - обьединяет значения в массив

```sql
-- пример из blog
SELECT blogger.name, ARRAY_AGG(post.body) AS posts FROM blogger JOIN post ON blogger.id = post.blogger_id GROUP BY blogger.name;
--    name    |                           posts                           
-- -----------+-----------------------------------------------------------
--  blogger 2 | {"my first post","some post"}
--  blogger 1 | {"my first blog","today is a good day","it is my b-day!"}
--  blogger 3 | {"i am not a blogger"}
```

> **MAX** - выводит максимальное значение

```sql
-- пример из blog
SELECT blogger.name, MAX(post.created_at) AS last_post FROM blogger JOIN post ON blogger.id = post.blogger_id GROUP BY blogger.name;
--    name    | last_post  
-- -----------+------------
--  blogger 2 | 2022-06-23
--  blogger 1 | 2021-09-30
--  blogger 3 | 2022-08-15

```

> **MIN** - выводит минимальное значение

```sql
-- пример из blog
SELECT blogger.name, MIN(post.created_at) AS first_post FROM blogger JOIN post ON blogger.id = post.blogger_id GROUP BY blogger.name;
--    name    | first_post 
-- -----------+------------
--  blogger 2 | 2013-05-10
--  blogger 1 | 2020-08-01
--  blogger 3 | 2022-08-15
```

> **COUNT** - считает кол-во записей

```sql
-- пример из blog
SELECT blogger.name, COUNT(post.id) AS posts_count FROM blogger JOIN post ON blogger.id = post.blogger_id GROUP BY blogger.name;
--    name    | posts_count 
-- -----------+-------------
--  blogger 2 |           2
--  blogger 1 |           3
--  blogger 3 |           1
```

> **AVG** - выводит среднее значение

```sql
-- пример из shop
SELECT product.title, AVG(rating.value) AS avg_rating 
FROM product JOIN rating ON rating.product_id = product.id GROUP BY (product.id);
--    title   |     avg_rating     
-- -----------+--------------------
--  product 5 | 3.3333333333333333
--  product 4 | 5.0000000000000000
--  product 2 | 5.0000000000000000
--  product 1 | 4.5000000000000000
--  product 3 | 4.3333333333333333
```

> **SUM** - выводит сумму значений

```sql
-- пример из shop
SELECT customer.name, SUM(product.price) AS total_price FROM customer JOIN cart ON customer.id = cart.customer_id JOIN product ON product.id = cart.product_id GROUP BY (customer.id);
--     name    | total_price 
-- ------------+-------------
--  customer 2 |         470
--  customer 3 |         688
--  customer 1 |        1079
```

# Создание бд blog
```sql
CREATE TABLE blogger (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50)
);

CREATE TABLE post (
    id SERIAL PRIMARY KEY,
    blogger_id INT,
    body TEXT,
    created_at DATE,

    CONSTRAINT fk_post_blogger FOREIGN KEY (blogger_id) REFERENCES blogger (id)
);
```

```sql
INSERT INTO blogger (name) VALUES ('blogger 1'), ('blogger 2'), ('blogger 3'); 

INSERT INTO post (blogger_id, body, created_at) VALUES
(1, 'my first blog', '01.08.2020'),
(1, 'today is a good day', '02.09.2020'),
(1, 'it is my b-day!', '30.09.2021');

INSERT INTO post (blogger_id, body, created_at) VALUES
(2, 'my first post', '10.05.2013'),
(2, 'some post', '23.06.2022');

INSERT INTO post (blogger_id, body, created_at) VALUES
(3, 'i am not a blogger', '15.08.2022');
```

# Создание бд shop
```sql
CREATE TABLE customer (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50)
);

CREATE TABLE product (
    id SERIAL PRIMARY KEY,
    title VARCHAR(50),
    price DECIMAL
);

CREATE TABLE rating (
    id SERIAL PRIMARY KEY,
    customer_id INT,
    product_id INT,
    value INT CHECK (value IN (1,2,3,4,5)),
    
    CONSTRAINT rating_customer FOREIGN KEY (customer_id) REFERENCES customer (id),
    CONSTRAINT rating_product FOREIGN KEY (product_id) REFERENCES product (id)
);

CREATE TABLE cart (
    id SERIAL PRIMARY KEY,
    customer_id INT,
    product_id INT,

    CONSTRAINT cart_customer FOREIGN KEY (customer_id) REFERENCES customer (id), 
    CONSTRAINT cart_product FOREIGN KEY (product_id) REFERENCES product (id)
);
```

```sql
INSERT INTO customer (name) VALUES ('customer 1'), ('customer 2'), ('customer 3'); 

INSERT INTO product (title, price) VALUES
('product 1', 340),
('product 2', 503),
('product 3', 470),
('product 4', 236),
('product 5', 452);

INSERT INTO rating (customer_id, product_id, value) VALUES
(1, 1, 5), (1, 2, 5), (1, 3, 5), (1, 4, 5), (1, 5, 5),
(2, 3, 4), (2, 4, 5), (2, 5, 2),
(3, 1, 4), (3, 2, 5), (3, 3, 4), (3, 5, 3);

INSERT INTO cart (customer_id, product_id) VALUES
(1, 1), (1, 2), (1, 4),
(2, 3),
(3, 4), (3, 5);
```