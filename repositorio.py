import os
import sqlite3
from http import HTTPStatus

OK = HTTPStatus.OK
BAD_REQUEST = HTTPStatus.BAD_REQUEST
NOT_FOUND = HTTPStatus.NOT_FOUND
CONFLICT = HTTPStatus.CONFLICT
CREATED = HTTPStatus.CREATED

class RepositorioDeArte(object):

    NOME_BANCO = 'artemoderna.sqlite'
    FOREIGN_KEY_SQL = 'PRAGMA foreign_keys=ON;'
    LINHAS_AFETADAS_SQL = 'SELECT changes();'

    @staticmethod
    def obra_dict(id, titulo, autor, ano, estilo, material, url_imagem):
        return {
            'Id':  id,
            'Titulo':  titulo,
            'Autor':  autor,
            'Ano':  ano,
            'Estilo':  estilo,
            'Material':  material,
            'UrlImagem':  url_imagem,
        }
    
    @staticmethod
    def autor_dict(id, nome, ano_nascimento, ano_falecimento, pais_origem, url_imagem):
        return {
            'Id':  id,
            'Nome':  nome,
            'AnoNascimento':  ano_nascimento,
            'AnoFalecimento':  ano_falecimento,
            'PaisOrigem':  pais_origem,
            'UrlImagem':  url_imagem,
        }

    @staticmethod
    def estilo_dict(id, nome):
        return {
            'Id':  id,
            'Nome':  nome,
        }
    
    @classmethod
    def conectar(cls):
        banco = sqlite3.connect(cls.NOME_BANCO, check_same_thread=False)
        cursor = banco.cursor()
        cursor.execute(cls.FOREIGN_KEY_SQL)
        return (banco, cursor)

    @classmethod
    def listar_todas_obras(cls):
        COMANDO_SQL = r'SELECT O.Id,O.Titulo,A.Nome AS Autor,O.Ano,E.Nome AS Estilo,O.Material,O.UrlImagem FROM Obra AS O INNER JOIN Autor AS A ON O.Autor = A.Id INNER JOIN Estilo AS E ON O.Estilo = E.Id;' 
        (_,conexao) = cls.conectar()
        resultado = conexao.execute(COMANDO_SQL)
        lista_tuplas = resultado.fetchall()
        return [cls.obra_dict(*tupla) for tupla in lista_tuplas]

    @classmethod
    def obter_obra_por_id(cls, id):
        COMANDO_SQL = r'SELECT O.Id,O.Titulo,A.Nome AS Autor,O.Ano,E.Nome AS Estilo,O.Material,O.UrlImagem FROM Obra AS O INNER JOIN Autor AS A ON O.Autor = A.Id INNER JOIN Estilo AS E ON O.Estilo = E.Id WHERE O.Id = :Id;' 
        (_,conexao) = cls.conectar()
        resultado = conexao.execute(COMANDO_SQL, {'Id': id})
        tupla = resultado.fetchone()
        return cls.obra_dict(*tupla) if tupla else None

    @classmethod
    def obter_obras_por_titulo(cls, titulo):
        COMANDO_SQL = r'SELECT O.Id,O.Titulo,A.Nome AS Autor,O.Ano,E.Nome AS Estilo,O.Material,O.UrlImagem FROM Obra AS O INNER JOIN Autor AS A ON O.Autor = A.Id INNER JOIN Estilo AS E ON O.Estilo = E.Id WHERE O.Titulo = :Titulo;' 
        (_,conexao) = cls.conectar()
        resultado = conexao.execute(COMANDO_SQL, {'Titulo': titulo})
        lista_tuplas = resultado.fetchall()
        return [cls.obra_dict(*tupla) for tupla in lista_tuplas]

    @classmethod
    def listar_obras_por_periodo(cls, ano_inicial, ano_final):
        COMANDO_SQL = r'SELECT O.Id,O.Titulo,A.Nome AS Autor,O.Ano,E.Nome AS Estilo,O.Material,O.UrlImagem FROM Obra AS O INNER JOIN Autor AS A ON O.Autor = A.Id INNER JOIN Estilo AS E ON O.Estilo = E.Id WHERE O.Ano >= :AnoInicial AND O.Ano <= :AnoFinal;' 
        (_,conexao) = cls.conectar()
        resultado = conexao.execute(COMANDO_SQL, {'AnoInicial': ano_inicial, 'AnoFinal': ano_final})
        lista_tuplas = resultado.fetchall()
        return [cls.obra_dict(*tupla) for tupla in lista_tuplas]

    @classmethod
    def listar_todos_autores(cls):
        COMANDO_SQL = r'SELECT Id,Nome,AnoNascimento,AnoFalecimento,PaisOrigem,UrlImagem FROM Autor;' 
        (_,conexao) = cls.conectar()
        resultado = conexao.execute(COMANDO_SQL)
        lista_tuplas = resultado.fetchall()
        return [cls.autor_dict(*tupla) for tupla in lista_tuplas]

    @classmethod
    def obter_autor_por_id(cls, id):
        COMANDO_SQL = r'SELECT Id,Nome,AnoNascimento,AnoFalecimento,PaisOrigem,UrlImagem FROM Autor WHERE Id = :Id;' 
        (_,conexao) = cls.conectar()
        resultado = conexao.execute(COMANDO_SQL, {'Id': id})
        tupla = resultado.fetchone()
        return cls.autor_dict(*tupla) if tupla else None

    @classmethod
    def obter_autor_por_nome(cls, nome):
        COMANDO_SQL = r'SELECT Id,Nome,AnoNascimento,AnoFalecimento,PaisOrigem,UrlImagem FROM Autor WHERE Nome = :Nome;' 
        (_,conexao) = cls.conectar()
        resultado = conexao.execute(COMANDO_SQL, {'Nome': nome})
        tupla = resultado.fetchone()
        return cls.autor_dict(*tupla) if tupla else None

    @classmethod
    def listar_todos_estilos(cls):
        COMANDO_SQL = r'SELECT Id,Nome FROM Estilo;' 
        (_,conexao) = cls.conectar()
        resultado = conexao.execute(COMANDO_SQL)
        lista_tuplas = resultado.fetchall()
        return [cls.estilo_dict(*tupla) for tupla in lista_tuplas]

    @classmethod
    def obter_estilo_por_id(cls, id):
        COMANDO_SQL = r'SELECT Id,Nome FROM Estilo WHERE Id = :Id;' 
        (_,conexao) = cls.conectar()
        resultado = conexao.execute(COMANDO_SQL, {'Id': id})
        tupla = resultado.fetchone()
        return cls.estilo_dict(*tupla) if tupla else None

    @classmethod
    def obter_estilo_por_nome(cls, nome):
        COMANDO_SQL = r'SELECT Id,Nome FROM Estilo WHERE Nome = :Nome;' 
        (_,conexao) = cls.conectar()
        resultado = conexao.execute(COMANDO_SQL, {'Nome': nome})
        tupla = resultado.fetchone()
        return cls.estilo_dict(*tupla) if tupla else None

    @classmethod
    def listar_obras_por_nome_autor(cls, nome_autor):
        COMANDO_SQL = r'SELECT O.Id,O.Titulo,A.Nome AS Autor,O.Ano,E.Nome AS Estilo,O.Material,O.UrlImagem FROM Obra AS O INNER JOIN Autor AS A ON O.Autor = A.Id INNER JOIN Estilo AS E ON O.Estilo = E.Id WHERE A.Nome = :NomeAutor;' 
        (_,conexao) = cls.conectar()
        resultado = conexao.execute(COMANDO_SQL, {'NomeAutor': nome_autor})
        lista_tuplas = resultado.fetchall()
        return [cls.obra_dict(*tupla) for tupla in lista_tuplas]

    @classmethod
    def listar_obras_por_id_autor(cls, id_autor):
        COMANDO_SQL = r'SELECT O.Id,O.Titulo,A.Nome AS Autor,O.Ano,E.Nome AS Estilo,O.Material,O.UrlImagem FROM Obra AS O INNER JOIN Autor AS A ON O.Autor = A.Id INNER JOIN Estilo AS E ON O.Estilo = E.Id WHERE A.Id = :IdAutor;' 
        (_,conexao) = cls.conectar()
        resultado = conexao.execute(COMANDO_SQL, {'IdAutor': id_autor})
        lista_tuplas = resultado.fetchall()
        return [cls.obra_dict(*tupla) for tupla in lista_tuplas]

    @classmethod
    def listar_obras_por_nome_estilo(cls, nome_estilo):
        COMANDO_SQL = r'SELECT O.Id,O.Titulo,A.Nome AS Autor,O.Ano,E.Nome AS Estilo,O.Material,O.UrlImagem FROM Obra AS O INNER JOIN Autor AS A ON O.Autor = A.Id INNER JOIN Estilo AS E ON O.Estilo = E.Id WHERE E.Nome = :NomeEstilo;' 
        (_,conexao) = cls.conectar()
        resultado = conexao.execute(COMANDO_SQL, {'NomeEstilo': nome_estilo})
        lista_tuplas = resultado.fetchall()
        return [cls.obra_dict(*tupla) for tupla in lista_tuplas]

    @classmethod
    def listar_obras_por_id_estilo(cls, id_estilo):
        COMANDO_SQL = r'SELECT O.Id,O.Titulo,A.Nome AS Autor,O.Ano,E.Nome AS Estilo,O.Material,O.UrlImagem FROM Obra AS O INNER JOIN Autor AS A ON O.Autor = A.Id INNER JOIN Estilo AS E ON O.Estilo = E.Id WHERE E.Id = :IdEstilo;' 
        (_,conexao) = cls.conectar()
        resultado = conexao.execute(COMANDO_SQL, {'IdEstilo': id_estilo})
        lista_tuplas = resultado.fetchall()
        return [cls.obra_dict(*tupla) for tupla in lista_tuplas]

    @classmethod
    def inserir_estilo(cls, nome):
        COMANDO_SQL = r'INSERT OR IGNORE INTO Estilo (Nome) VALUES (:Nome);'
        (banco, conexao) = cls.conectar()
        conexao.execute(COMANDO_SQL, {'Nome': nome})
        resultado = conexao.execute(cls.LINHAS_AFETADAS_SQL)
        afetadas = resultado.fetchone()[0]
        banco.commit()
        return (afetadas > 0)

    @classmethod
    def inserir_autor(cls, nome, ano_nascimento, ano_falecimento, pais_origem, url_imagem):
        COMANDO_SQL = r'INSERT OR IGNORE INTO Autor (Nome,AnoNascimento,AnoFalecimento,PaisOrigem,UrlImagem) VALUES (:Nome,:AnoNascimento,:AnoFalecimento,:PaisOrigem,:UrlImagem);'
        (banco, conexao) = cls.conectar()
        conexao.execute(COMANDO_SQL, {'Nome': nome, 'AnoNascimento': ano_nascimento, 'AnoFalecimento': ano_falecimento, 'PaisOrigem': pais_origem, 'UrlImagem': url_imagem})
        resultado = conexao.execute(cls.LINHAS_AFETADAS_SQL)
        afetadas = resultado.fetchone()[0]
        banco.commit()
        return (afetadas > 0)
    
    @classmethod
    def inserir_obra(cls, titulo, autor, ano, estilo, material, url_imagem):
        COMANDO_SQL = r'INSERT OR IGNORE INTO Obra (Titulo,Autor,Ano,Estilo,Material,UrlImagem) VALUES (:Titulo,:Autor,:Ano,:Estilo,:Material,:UrlImagem);'
        (banco, conexao) = cls.conectar()
        try:
            conexao.execute(COMANDO_SQL, {'Titulo': titulo, 'Autor': autor, 'Ano': ano, 'Estilo': estilo, 'Material': material, 'UrlImagem': url_imagem})
            resultado = conexao.execute(cls.LINHAS_AFETADAS_SQL)
            afetadas = resultado.fetchone()[0]
            banco.commit()
            return (afetadas > 0)
        except sqlite3.IntegrityError:
            return False

    @classmethod
    def editar_estilo_por_id(cls, id, nome):
        COMANDO_SQL = r'UPDATE OR IGNORE Estilo SET Nome = :Nome WHERE Id = :Id;'
        (banco, conexao) = cls.conectar()
        conexao.execute(COMANDO_SQL, {'Id': id, 'Nome': nome})
        resultado = conexao.execute(cls.LINHAS_AFETADAS_SQL)
        afetadas = resultado.fetchone()[0]
        banco.commit()
        return (afetadas > 0)
    
    @classmethod
    def editar_estilo_por_nome(cls, nome_antigo, novo_nome):
        COMANDO_SQL = r'UPDATE OR IGNORE Estilo SET Nome = :NovoNome WHERE Nome = :NomeAntigo;'
        (banco, conexao) = cls.conectar()
        conexao.execute(COMANDO_SQL, {'NomeAntigo': nome_antigo, 'NovoNome': novo_nome})
        resultado = conexao.execute(cls.LINHAS_AFETADAS_SQL)
        afetadas = resultado.fetchone()[0]
        banco.commit()
        return (afetadas > 0)

    @classmethod
    def editar_autor_por_id(cls, id, nome, ano_nascimento, ano_falecimento, pais_origem, url_imagem):
        COMANDO_SQL = r'UPDATE OR IGNORE Autor SET Nome=:Nome,AnoNascimento=:AnoNascimento,AnoFalecimento=:AnoFalecimento,PaisOrigem=:PaisOrigem,UrlImagem=:UrlImagem WHERE Id = :Id;'
        (banco, conexao) = cls.conectar()
        conexao.execute(COMANDO_SQL, {'Id': id, 'Nome': nome, 'AnoNascimento': ano_nascimento, 'AnoFalecimento': ano_falecimento, 'PaisOrigem': pais_origem, 'UrlImagem': url_imagem})
        resultado = conexao.execute(cls.LINHAS_AFETADAS_SQL)
        afetadas = resultado.fetchone()[0]
        banco.commit()
        return (afetadas > 0)

    @classmethod
    def editar_autor_por_nome(cls, nome_antigo, novo_nome, ano_nascimento, ano_falecimento, pais_origem, url_imagem):
        COMANDO_SQL = r'UPDATE OR IGNORE Autor SET Nome=:NovoNome,AnoNascimento=:AnoNascimento,AnoFalecimento=:AnoFalecimento,PaisOrigem=:PaisOrigem,UrlImagem=:UrlImagem WHERE Nome = :NomeAntigo;'
        (banco, conexao) = cls.conectar()
        conexao.execute(COMANDO_SQL, {'Id': id, 'NomeAntigo': nome_antigo, 'NovoNome': novo_nome, 'AnoNascimento': ano_nascimento, 'AnoFalecimento': ano_falecimento, 'PaisOrigem': pais_origem, 'UrlImagem': url_imagem})
        resultado = conexao.execute(cls.LINHAS_AFETADAS_SQL)
        afetadas = resultado.fetchone()[0]
        banco.commit()
        return (afetadas > 0)

    @classmethod
    def editar_obra_por_id(cls, id, titulo, autor, ano, estilo, material, url_imagem):
        COMANDO_SQL = r'UPDATE OR IGNORE Obra SET Titulo=:Titulo,Autor=:Autor,Ano=:Ano,Estilo=:Estilo,Material=:Material,UrlImagem=:UrlImagem WHERE Id = :Id;'
        (banco, conexao) = cls.conectar()
        try:
            conexao.execute(COMANDO_SQL, {'Id': id, 'Titulo': titulo, 'Autor': autor, 'Ano': ano, 'Estilo': estilo, 'Material': material, 'UrlImagem': url_imagem})
            resultado = conexao.execute(cls.LINHAS_AFETADAS_SQL)
            afetadas = resultado.fetchone()[0]
            banco.commit()
            return (afetadas > 0)
        except sqlite3.IntegrityError:
            return False

    @classmethod
    def remover_estilo_por_id(cls, id):
        COMANDO_SQL = r'DELETE FROM Estilo WHERE Id = :Id;'
        (banco, conexao) = cls.conectar()
        try:
            conexao.execute(COMANDO_SQL, {'Id': id})
            resultado = conexao.execute(cls.LINHAS_AFETADAS_SQL)
            afetadas = resultado.fetchone()[0]
            banco.commit()
            return (afetadas > 0)
        except sqlite3.IntegrityError:
            return False

    @classmethod
    def remover_estilo_por_nome(cls, nome):
        COMANDO_SQL = r'DELETE FROM Estilo WHERE Nome = :Nome;'
        (banco, conexao) = cls.conectar()
        try:
            conexao.execute(COMANDO_SQL, {'Nome': nome})
            resultado = conexao.execute(cls.LINHAS_AFETADAS_SQL)
            afetadas = resultado.fetchone()[0]
            banco.commit()
            return (afetadas > 0)
        except sqlite3.IntegrityError:
            return False

    @classmethod
    def remover_autor_por_id(cls, id):
        COMANDO_SQL = r'DELETE FROM Autor WHERE Id = :Id;'
        (banco, conexao) = cls.conectar()
        try:
            conexao.execute(COMANDO_SQL, {'Id': id})
            resultado = conexao.execute(cls.LINHAS_AFETADAS_SQL)
            afetadas = resultado.fetchone()[0]
            banco.commit()
            return (afetadas > 0)
        except sqlite3.IntegrityError:
            return False

    @classmethod
    def remover_autor_por_nome(cls, nome):
        COMANDO_SQL = r'DELETE FROM Autor WHERE Nome = :Nome;'
        (banco, conexao) = cls.conectar()
        try:
            conexao.execute(COMANDO_SQL, {'Nome': nome})
            resultado = conexao.execute(cls.LINHAS_AFETADAS_SQL)
            afetadas = resultado.fetchone()[0]
            banco.commit()
            return (afetadas > 0)
        except sqlite3.IntegrityError:
            return False

    @classmethod
    def remover_obra_por_id(cls, id):
        COMANDO_SQL = r'DELETE FROM Obra WHERE Id = :Id;'
        (banco, conexao) = cls.conectar()
        conexao.execute(COMANDO_SQL, {'Id': id})
        resultado = conexao.execute(cls.LINHAS_AFETADAS_SQL)
        afetadas = resultado.fetchone()[0]
        banco.commit()
        return (afetadas > 0)

    @classmethod
    def alterar_imagem_autor_por_id(cls, id, url_imagem):
        COMANDO_SQL = r'UPDATE OR IGNORE Autor SET UrlImagem=:UrlImagem WHERE Id = :Id;'
        (banco, conexao) = cls.conectar()
        conexao.execute(COMANDO_SQL, {'Id': id, 'UrlImagem': url_imagem})
        resultado = conexao.execute(cls.LINHAS_AFETADAS_SQL)
        afetadas = resultado.fetchone()[0]
        banco.commit()
        return (afetadas > 0)

    @classmethod
    def alterar_imagem_autor_por_nome(cls, nome, url_imagem):
        COMANDO_SQL = r'UPDATE OR IGNORE Autor SET UrlImagem=:UrlImagem WHERE Nome = :Nome;'
        (banco, conexao) = cls.conectar()
        conexao.execute(COMANDO_SQL, {'Nome': nome, 'UrlImagem': url_imagem})
        resultado = conexao.execute(cls.LINHAS_AFETADAS_SQL)
        afetadas = resultado.fetchone()[0]
        banco.commit()
        return (afetadas > 0)

    @classmethod
    def alterar_imagem_obra_por_id(cls, id, url_imagem):
        COMANDO_SQL = r'UPDATE OR IGNORE Obra SET UrlImagem=:UrlImagem WHERE Id = :Id;'
        (banco, conexao) = cls.conectar()
        conexao.execute(COMANDO_SQL, {'Id': id, 'UrlImagem': url_imagem})
        resultado = conexao.execute(cls.LINHAS_AFETADAS_SQL)
        afetadas = resultado.fetchone()[0]
        banco.commit()
        return (afetadas > 0)

if __name__ == '__main__':

    def checar_ou_criar_banco():
        if not os.path.isfile(RepositorioDeArte.NOME_BANCO):
            print('Banco de dados não encontrado, novo banco será criado com valores iniciais.')
            with open('artemoderna.sql', 'r', encoding='utf8') as arquivo_sql:
                script_sql = arquivo_sql.read()
            (_,conexao) = RepositorioDeArte.conectar()
            conexao.executescript(script_sql)
            print('Banco de dados inicial criado.')
        else:
            print('Banco de dados encontrado.')

    checar_ou_criar_banco()