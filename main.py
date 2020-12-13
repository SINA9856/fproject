def main():
    weight = int(input("How much is the weight? "))
    density = int(input("How much is the density? "))
    volume = weight / density
    print("The Volume is: ", volume, "L^3")

if __name__ == '__main__':
    main()
