import pymysql.cursors

conexao = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='interpy',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)
x = ('create table cadastro(nome varchar(20),'
     'endereco varchar(100));')
y = ('drop table cadastro')

with conexao.cursor() as cursor:
    cursor.execute(x)
    #cursor.execute(y)

print("sucesso!")
