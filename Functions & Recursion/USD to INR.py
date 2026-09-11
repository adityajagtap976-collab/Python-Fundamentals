# Function to convert USD to INR
def USD_to_INR():
    # Get the amount in USD from the user
    usd_amount = float(input("Enter the amount in USD: "))

    # Conversion rate from USD to INR (as of a specific date)
    conversion_rate = 94.0  # Example conversion rate

    # Calculate the amount in INR
    inr_amount = usd_amount * conversion_rate

    # Print the result
    print(f"{usd_amount} USD is equal to {inr_amount} INR.")


# Call the function to perform the conversion
USD_to_INR()

# Why there is no return statement in the function?
# The function `USD_to_INR()` does not have a return statement because its primary purpose is to perform an action (i.e., converting USD to INR and printing the result) rather than returning a value to be used elsewhere in the program. In this case, the function takes user input, performs the conversion, and directly outputs the result to the console.
