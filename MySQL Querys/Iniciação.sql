create database teste_busca;
use teste_busca;

create table clientes (
id int primary key auto_increment,
nome varchar(100),
email varchar(100),
telefone varchar(20)
);

select * from clientes;clientes

insert into clientes (nome, email, telefone)
values
('Gabi', 'gabi@email.com', '11111'),
('Victor', 'victoremail.com', '22222'),
('Cecilia', 'cecilia@email.com', '33333');

SELECT * 
FROM clientes
WHERE nome = 'Gabi';

SELECT * 
FROM clientes
WHERE email LIKE '%@email.com';

UPDATE clientes
SET nome = 'Vitinho'
WHERE email = 'victoremail.com';

DELETE FROM clientes
WHERE nome = 'Cecilia';



