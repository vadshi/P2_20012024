# # Version 1 with error
# def func_info(func):
#     def wrapper(*args, **kwargs):
#         print('Function name:', func.__name__)
#         print('Function docstring:', func.__doc__)
#         result = func(*args, **kwargs)
#         return result
#     return wrapper


# # Так не отработает
# @func_info(5)
# def mul_two(number):
#     """ func for returning triple result """
#     return number * 3
#
#
# print(mul_two(5))

# Version 2 without error
# def func_info(arg1, arg2):
#     print(f'Decorator arg1 = {arg1}')
#     print(f'Decorator arg2 = {arg2}')
# 
#     def real_decorator(function):
#         print('From real_decorator.')
# 
#         def wrapper(*args, **kwargs):
#             print(f'Function {function.__name__} args: {args} kwargs: {kwargs}')
#             coef = 1 if arg2 == 'work' else 1.5
#             return coef * function(*args, **kwargs) * arg1
# 
#         return wrapper
#
#     return real_decorator


# @func_info(3, 'weekend')
# def mul_two(number):
#     return number * 10


# print(mul_two(5))


# Вариант без сахара
# def mul_no_sugar(number):
#     return number * 10


# без сахара (@)
# res_func_info = func_info(2, 'weekend')  # ссылка на функцию real_decorator
# print(res_func_info, type(res_func_info))
# chg_no_sugar = res_func_info(mul_no_sugar)  # ссылка на wrapper
# print(type(chg_no_sugar))
# print(chg_no_sugar)
# print(chg_no_sugar(5))

