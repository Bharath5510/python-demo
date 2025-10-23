def add(a, b):
    return a + b

def sub(a, b):
    return a - b

if __name__ == "__main__":
    with open("output.txt", "w") as f:
        f.write(f"Addition: {add(10, 5)}\n")
        f.write(f"Subtraction: {sub(10, 5)}\n")
