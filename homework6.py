salary = int(input("Enter your salary amount: "))
max_terms = 365
depo_terms = 182
rate = 0.10

deposit = salary / 100 * rate / max_terms * depo_terms
print (deposit)

half_deposit = (salary * rate / max_terms) * 2
print(deposit + half_deposit)
