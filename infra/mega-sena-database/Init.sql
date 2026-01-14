-- Create database

CREATE DATABASe IF NOT EXISTS megasena;

-- Resultados definition

CREATE TABLE Resultados (
    Concurso INTEGER PRIMARY KEY NOT NULL,.
    Data_Sorteio DATE NOT NULL,
    Coluna1 INTEGER (2) NOT NULL,
    Coluna2 INTEGER (2) NOT NULL,
    Coluna3 INTEGER (2) NOT NULL,
    Coluna4 INTEGER (2) NOT NULL,
    Coluna5 INTEGER (2) NOT NULL,
    Coluna6 INTEGER (2) NOT NULL,
    Ganhadores INTEGER NOT NULL,
    Premio DECIMAL (18,2) NOT NULL
);

CREATE INDEX IX_Resultado_Concurso ON Resultados(Concurso);
CREATE INDEX IX_Resultado_Data ON Resultados(Data_Sorteio);
CREATE INDEX IX_Resultado_C1 ON Resultados(Coluna1);
CREATE INDEX IX_Resultado_C2 ON Resultados(Coluna2);
CREATE INDEX IX_Resultado_C3 ON Resultados(Coluna3);
CREATE INDEX IX_Resultado_C4 ON Resultados(Coluna4);
CREATE INDEX IX_Resultado_C5 ON Resultados(Coluna5);
CREATE INDEX IX_Resultado_C6 ON Resultados(Coluna6);

-- Apostas_Candidatas definition

CREATE TABLE Apostas_Candidatas (
	Id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
	Coluna1 INTEGER NOT NULL,
	Coluna2 INTEGER,
	Coluna3 INTEGER,
	Coluna4 INTEGER,
	Coluna5 INTEGER,
	Coluna6 INTEGER,
    Previsao DECIMAL(3,3) DEFAULT 0 NOT NULL
);
