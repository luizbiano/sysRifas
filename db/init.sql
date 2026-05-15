CREATE TABLE Perfil (
    Id VARCHAR(3) PRIMARY KEY,
    Descricao VARCHAR(50) NOT NULL,
    Dt_Inclusao TIMESTAMP NOT NULL,
    Dt_Modificacao TIMESTAMP NOT NULL,
    Usr_Inclusao VARCHAR(50) NOT NULL,
    Usr_Modificacao VARCHAR(50) NOT NULL
);

CREATE TABLE Usuario (
    Id VARCHAR(3) PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    DtNascimento DATE NOT NULL,
    Email VARCHAR(100) NOT NULL UNIQUE,
    Telefone VARCHAR(20) NOT NULL,
    Senha VARCHAR(256) NOT NULL,
    AlterarSenha CHAR(1) NOT NULL,
    Perfil VARCHAR(3) NOT NULL,

    Dt_Inclusao TIMESTAMP NOT NULL,
    Dt_Modificacao TIMESTAMP NOT NULL,
    Usr_Inclusao VARCHAR(50) NOT NULL,
    Usr_Modificacao VARCHAR(50) NOT NULL,

    CONSTRAINT FK_Usuario_Perfil
        FOREIGN KEY (Perfil)
        REFERENCES Perfil(Id)
);