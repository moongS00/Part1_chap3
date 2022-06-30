import random
def lottery():
    lucky = random.sample(range(1, 46), 6)

    return lucky

def reverse(str):
    reverse_str = ''
    for c in str:
        reverse_str = c + reverse_str

    return reverse_str
