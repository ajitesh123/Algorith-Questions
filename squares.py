def square(i):
    return (i*i)

def main():
    for i in range(10):
        print("{} squared is {}.format(i, square(i))")

if __name__=="__main__":
    main()
