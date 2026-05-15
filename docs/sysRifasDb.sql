
CREATE DATABASE sysrifas;
GO

USE sysrifas;
GO

CREATE TABLE Perfil (
    Id VARCHAR(3) NOT NULL,
    Descricao VARCHAR(50) NOT NULL,
    Dt_Inclusao DATETIME NOT NULL,
    Dt_Modificacao DATETIME NOT NULL,
    Usr_Inclusao VARCHAR(50) NOT NULL,
    Usr_Modificacao VARCHAR(50) NOT NULL,

    CONSTRAINT PK_Perfil PRIMARY KEY (Id)
);

CREATE INDEX IX_Perfil_Id
ON Perfil (Id);

CREATE INDEX IX_Perfil_Descricao
ON Perfil (Descricao);

CREATE TABLE Usuario (
    Id VARCHAR(3) NOT NULL,
    Nome VARCHAR(100) NOT NULL,
    DtNascimento DATE NOT NULL,
    Email VARCHAR(100) NOT NULL,
    Telefone VARCHAR(20) NOT NULL,
    Senha VARBINARY(256) NOT NULL,
    AlterarSenha CHAR(1) NOT NULL,
    Perfil VARCHAR(3) NOT NULL,
    Dt_Inclusao DATETIME NOT NULL,
    Dt_Modificacao DATETIME NOT NULL,
    Usr_Inclusao VARCHAR(50) NOT NULL,
    Usr_Modificacao VARCHAR(50) NOT NULL,

    CONSTRAINT PK_Usuario PRIMARY KEY (Id),

    CONSTRAINT FK_Usuario_Perfil FOREIGN KEY (Perfil)
    REFERENCES Perfil(Id)
);

-- Índice por ID (já é PK, mas incluído conforme pedido)
CREATE INDEX IX_Usuario_Id
ON Usuario (Id);

-- Índice único para login
CREATE UNIQUE INDEX IX_Usuario_Email
ON Usuario (Email);

-- Índice para relacionamento
CREATE INDEX IX_Usuario_Perfil
ON Usuario (Perfil);

-- Auditoria
CREATE INDEX IX_Usuario_DtInclusao
ON Usuario (Dt_Inclusao);


INSERT INTO Perfil
(Id, Descricao, Dt_Inclusao, Dt_Modificacao, Usr_Inclusao, Usr_Modificacao)
VALUES
('001', 'Admin',     GETDATE(), GETDATE(), 'System', 'System'),
('002', 'Vendedor',  GETDATE(), GETDATE(), '001', '001'),
('003', 'Usuário',   GETDATE(), GETDATE(), '001', '001');

INSERT INTO Usuario
(Id, Nome, DtNascimento, Email, Telefone, Senha, AlterarSenha, Perfil, Dt_Inclusao, Dt_Modificacao, Usr_Inclusao, Usr_Modificacao)
VALUES
('001', 'Luiz Biano',  '1986-10-04', 'luizbiano51@gmail.com', '34984244578', HASHBYTES('SHA2_256','Teste@123'), 'F', '001', GETDATE(), GETDATE(), 'System', 'System'),
('002', 'Vendedor 1',  '1989-01-04', 'vendedor1@gmail.com',   '34994224358', HASHBYTES('SHA2_256','Teste@123'), 'T', '002', GETDATE(), GETDATE(), '001', '001'),
('003', 'User 1',      '1995-05-04', 'user1@gmail.com',       '34997244588', HASHBYTES('SHA2_256','Teste@123'), 'T', '003', GETDATE(), GETDATE(), '001', '001'),
('004', 'User 2',      '1980-05-04', 'user2@gmail.com',       '34991764502', HASHBYTES('SHA2_256','Teste@123'), 'T', '003', GETDATE(), GETDATE(), '001', '001');

SELECT * FROM sysrifas..Perfil
SELECT * FROM sysrifas..Usuario