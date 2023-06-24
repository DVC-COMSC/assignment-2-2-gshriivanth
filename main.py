def main():
    
    celcius = int(input("Enter the temperature in Celsius: "))
    fahrenheit = ((9/5) * celcius) + 32

    print(f"The temperature in Fahrenheit is:\t", format(fahrenheit, '.2f')) 

    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return celcius, fahrenheit


if __name__ == '__main__':
    main()
