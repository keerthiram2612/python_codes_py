def solve(meal_cost, tip_percent, tax_percent):
    # Write your code here

 if __name__ == '__main__':
    meal_cost =20.75

    tip_percent =10

    tax_percent =3

    solve(meal_cost, tip_percent, tax_percent)
meal_cost=20.75
tip=20.75/100*10
tax=3/100*20.75
total_cost=meal_cost+tip+tax
print(round(total_cost))
