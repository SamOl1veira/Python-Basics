import pymysql.cursors

conexao = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='interpy',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

x = input("digite seu nome: ")
y = input("digite seu endereco: ")

with conexao.cursor() as cursors:
    cursors.execute('insert into cadastro(nome, endereco) values("{}", "{}");'.format(x, y))
    conexao.commit()