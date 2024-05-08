# Define the polynomial function
def polynomial(x):
    return 3*x**3 - 5*x**2 - 16*x + 12

# Define the derivative of the polynomial function
def derivative_polynomial(x):
    return 9*x**2 - 10*x - 16

# Implement the Newton-Raphson method for root finding
def newton_raphson(initial_guess):
    x0 = initial_guess
    iteration = 0
    while True:
        fx = polynomial(x0)
        f_prime_x = derivative_polynomial(x0)
        x1 = x0 - fx / f_prime_x
        iteration += 1
        print("Iteration:", iteration, "x:", x1, "|p(x)|:", abs(polynomial(x1)))
        if abs(polynomial(x1)) < 1e-6:
            return x1
        x0 = x1

# Main function to get initial guess from user and find the root
def main():
    # Get initial guess from the user
    x0 = float(input("Enter initial guess (x0): "))
    
    # Find the root using Newton-Raphson method
    root = newton_raphson(x0)
    
    # Print the root
    print("Root found at:", root)

# Execute the main function if this script is run directly
if __name__ == "__main__":
    main()
