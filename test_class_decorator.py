from simple_class_decorator import SimpleClassDecorator

@SimpleClassDecorator
def add(a, b):
	print('функция 1')
	return a + b

print(add(4,5))