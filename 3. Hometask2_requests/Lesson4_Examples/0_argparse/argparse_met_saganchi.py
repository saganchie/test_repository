import argparse

parser = argparse.ArgumentParser()

# Тип схемы для адресации запросов
parser.add_argument('-s', '--schema',
                    help='schema of the URL',
                    type=str,
                    required=False,
                    default='https',
                    choices=['http', 'https'])

# Указание хоста, к которому обращаемся
parser.add_argument('--host',
                    help='host',
                    type=str,
                    default="localhost")

# Если параметр передан, то True, иначе False
parser.add_argument('--path',
                    default='/',
                    type=str,
                    help='True or False param',
                    required=False)


# Функция
def url_maker(schema, host, path):
    return schema + "://" + host + path


arguments = parser.parse_args()

print(url_maker(arguments.schema, arguments.host, arguments.path))
