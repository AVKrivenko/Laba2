def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
    
def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 1) == -1
if __name__ == "__main__":
    print("Addition:", add(5, 3))
    print("Subtraction:", subtract(5, 3))
    print("Multiplication:", multiply(5, 3))
