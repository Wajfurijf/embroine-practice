while True:
    try:
        user_amount=float(input("Enter the amount to be converted:"))
        user_currency=input("Enter your current currency:")
        target_currency=input("Enter the currency you want it converted to:")
        if user_currency=='rupee' and target_currency=='dollar':
            new_user_currency1=user_amount*0.010
            print(f"{user_amount} rupees is equal to {new_user_currency1} dollars")
        elif user_currency=='dollar' and target_currency=='rupee':
            new_user_currency2=user_amount*100
            print(f"{user_amount} dollars is equal to {new_user_currency2} rupees")
        if user_currency=='rupee' and target_currency=='pound':
            new_user_currency3=user_amount*0.0078
            print(f"{user_amount} rupees is equal to {new_user_currency3} pound")
        elif user_currency=='pound' and target_currency=='rupee':
            new_user_currency4=user_amount*127.96
            print(f"{user_amount} pounds is equal to {new_user_currency4} rupees")
            break
        if user_currency=='rupee' and target_currency=='euro':
            new_user_currency5=user_amount*0.0091
            print(f"{user_amount} rupees is equal to {new_user_currency5} euro")
        elif user_currency=='euro' and target_currency=='rupee':
            new_user_currency6=user_amount*109.79
            print(f"{user_amount} euros is equal to {new_user_currency6} rupees")
        break
    except ValueError:
        print("Please enter a valid amount")


