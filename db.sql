CREATE TYPE position_category AS ENUM ('руководитель', 'специалист', 'служащий', 'рабочий');

CREATE TYPE employee_sex AS ENUM ('мужской', 'женский');

CREATE TABLE positions (
    id SERIAL PRIMARY KEY,
    post VARCHAR(255) NOT NULL UNIQUE,
    category position_category NOT NULL
);


    CREATE TABLE employees (
        id SERIAL PRIMARY KEY,
        last_name VARCHAR(100) NOT NULL,
        first_name VARCHAR(100) NOT NULL,
        patronymic VARCHAR(100) NOT NULL,
        sex employee_sex NOT NULL,
        age INTEGER NOT NULL CHECK (employees.age >= 18 AND employees.age < 65),
        position_id INTEGER NOT NULL,
        FOREIGN KEY (position_id) REFERENCES positions(id) ON DELETE CASCADE
    );

insert into employees (first_name, last_name, patronymic, sex, age, position_id) values
('Иван', 'Иванов', 'Иванович', 'мужской', 40, 1),
('Юлия', 'Кузнецова', 'Владимировна', 'женский', 30, 2),
('Виктор', 'Петров', 'Витальевич', 'мужской', 35, 3),
('Александр', 'Геннадиев', 'Олегович', 'мужской', 25, 4);

INSERT INTO positions (post, category) VALUES
    ('Директор', 'руководитель'),
    ('Менеджер', 'специалист'),
    ('Секретарь', 'служащий'),
    ('Рабочий', 'рабочий');

insert into employees (fio, sex, age, position_id) values 
('Иванов Иван Иванович', 'мужской', 40,1),
('Кузнецова Юлия Владимировна', 'женский', 30,2),
('Петров Виктор Витальевич', 'мужской', 35, 3),
('Геннадиев Александр Олегович', 'мужской', 25, 4);

SELECT id, post, category
FROM public.positions;