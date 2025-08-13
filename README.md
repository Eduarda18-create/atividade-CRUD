# Sistema de Marcação de Provas

## 📌 Descrição
Sistema web para gerenciar matérias e provas. Permite cadastrar, listar, editar e excluir matérias e provas, além de vincular provas a matérias.

## 📂 Estrutura do Banco de Dados
- **Matéria**
  - `id` (int, PK)
  - `nome` (str, obrigatório)
  - `professor` (str, obrigatório)
  - `descricao` (str, obrigatório)
- **Prova**
  - `id` (int, PK)
  - `data` (date, obrigatório)
  - `peso` (float, obrigatório)
  - `materia_id` (int, FK → Matéria)

Relacionamento: 1:N (uma matéria pode ter várias provas).

## Como executar:

1. Criar ambiente virtual
    ```
    python -m venv venv
    ```
2. Ativar ambiente virtual
    ```
    source venv\Scripts\activate
    ```
   2.1. Atualizar o pip
    ```
    pip install --upgrade pip
    ```
3. Instalar o Flask
    ```
    pip install Flask
    ```
4. Execute o servidor
    ```
    python run.py
    ```