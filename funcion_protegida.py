

def main():
    password = input("Write your password down: ")

    protected_func(password)


def protected(func):
    def wrapper(password):
        if password == "platzi":
            return func()
        else:
            print("Your password is incorrect.")

    return wrapper

@protected      #decorador
def protected_func():
    print("Your password es correct")

if __name__ == "__main__":
    main()
