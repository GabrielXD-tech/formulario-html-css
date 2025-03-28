USE clientes;

SELECT * from clientes;

CREATE TABLE clientes (
    id INT PRIMARY KEY,
    nome varchar(100) NOT NULL,
    email varchar(100)  NOT NULL UNIQUE,
    senha varchar(100)  NOT NULL
);

select * from clientes;

ALTER TABLE clientes ADD COLUMN telefone int;
ALTER TABLE clientes ADD COLUMN genero varchar(20);
ALTER TABLE clientes ADD COLUMN data_nascimento date;
ALTER TABLE clientes ADD COLUMN cidade varchar(20);
ALTER TABLE clientes ADD COLUMN estado varchar(20);
ALTER TABLE clientes ADD COLUMN endereco varchar(50);
