Exc_Rate = {
    "USD" : 1.0,
    "INR": 83.2,
    "EUR": 0.93,
    "GBP": 0.79,
    "JPY": 157.2,
    "AUD": 1.51
}
def currency_convert(from_curr, to_curr, amt):
    if from_curr not in Exc_Rate or to_curr not in Exc_Rate:
        print("Error")
    std = amt / Exc_Rate[from_curr]
    convt = std * Exc_Rate[to_curr]
    return convt

# Example
#from_curr = "INR"
#to_curr = "EUR"
#amt = 1000

from_curr = input("Enter from curr: ")
to_curr = input("Enter to Curr: ")
amt = int(input("amt"))

result = currency_convert(from_curr, to_curr, amt)
print(f"{amt} {from_curr} = {result} {to_curr}")
