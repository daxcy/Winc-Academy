# Do not modify these lines
__winc_id__ = '62311a1767294e058dc13c953e8690a4'
__human_name__ = 'casting'

# Add your code after this line

leek_price = 2
leek = 'Leek is ' + str(leek_price) +' euro per kilo.'
print(leek)

leek = 'leek 4'
leek_len = len(leek) - 1
leek_num_order = leek[leek_len:]
sum_total = int(leek_num_order) * leek_price
# print(leek_price)
# print(leek_num_order)
print(sum_total)

broccoli_price = 2.34
broccoli = 'broccoli 1.6'
broccoli_len = len(broccoli) - 3
sum_total = broccoli_price * float(broccoli[broccoli_len:])

print(str(broccoli[broccoli_len:]) +'kg broccoli costs ' + str(round(sum_total, 2)) + 'e')