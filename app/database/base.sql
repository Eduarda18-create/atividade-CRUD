CREATE TABLE materia (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    professor TEXT NOT NULL,
    descricao TEXT
);

CREATE TABLE prova (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data DATE NOT NULL,
    peso REAL NOT NULL,
    materia_id INTEGER NOT NULL,
    FOREIGN KEY (materia_id) REFERENCES materia (id) ON DELETE CASCADE
);
