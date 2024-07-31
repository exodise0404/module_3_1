calls = 0
def count_calls():
    global calls
    calls += 1
    return calls


def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())

print(string_info('Capybara'))
print(string_info('Armageddon'))


def is_contains(string, list_to_search):
    count_calls()
    if str.lower(string) in (item.lower() for item in list_to_search):
        return True
    else:
        return False

print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))


print(calls)
