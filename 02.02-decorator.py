def decorator(f):
    def wrapper():
        print("Going to run the function..")
        f()
        print("Finished running the function.")
    return wrapper

@decorator
def hello():
    print("Hello All!!!")

hello()
