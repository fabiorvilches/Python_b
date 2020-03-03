import psycopg2
import psycopg2.extras


connection = psycopg2.connect(
    user='admin',
    password='4linux',
    host='localhost',
    port=5432,
    database='projeto'
)
cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

email = input('Digite seu email: ')
password = input('Digite sua senha: ')

print('\n\n###### SOLUÇÃO 2 \n\n')

def get_authenticated_user(email, password):
    cursor.execute('''

        SELECT * FROM users

        WHERE users.email = \'{}\'
        AND users.password = \'{}\';

    '''.format(email, password))
    return cursor.fetchone()

user = get_authenticated_user(email, password)

if user:
    print('Autenticado')
else:
    print('Algo de errado aconteceu'