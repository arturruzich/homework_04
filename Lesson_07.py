int_list: list[int] = [1, 0]

result: bool = all(int_list)

result_2: bool = any(int_list)

print(result)
print(result_2)

byte_array = bytearray(b'Hello, World!')
print(byte_array)
print(byte_array[0])
byte_array[0] = 37
print(byte_array.decode('utf-8'))

is_callable: bool = callable(print())

print(is_callable)


code = '''
def greet(name):
    print("Hello, " + name)

greet("World")
'''
compiled_code = compile(code, '<string>', 'exec')
exec(compiled_code)