"""
Пример работы с декоратором для логирования данных
при выполнении какой-либо функции
"""
import functools

def logger(filename):
    def decorator(func):
        #позволяет сохранить имя декорируемой функции
        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            with open(filename, 'a', encoding='utf-8') as file:
                file.write("Query was executed!\n")
        return wrapped
    return decorator

@logger('log.txt')
def printer():
    print("Select * from table")


printer()
printer()
printer()