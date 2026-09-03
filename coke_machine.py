amount = 50
print("Amount due: ", amount)
bean = True
while(bean):
    coin = input("Coin: ")
    coin = int(coin)
    if (amount - coin <= 0):
        bean = False
        print("Change owed: ", (coin - amount))
    else:
        amount = amount - coin
        print("Amount: ", amount)