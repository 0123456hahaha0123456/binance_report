import csv, os, glob
import constant

# use to save total amount and total exectued
# after all, we loop through dict and calculate avarage
buy_data = {}
sell_data = {}
# process pairs with USDT/BUSD only
def process_pairs(pair, side, executed, amount):
    print(f'{pair}, {side}, {executed}, {amount}')
    if side==constant.  BUY:
        if pair in buy_data:
            values = buy_data[pair]
            new_amount = values[1] + amount
            new_executed = values[0] + executed
            buy_data[pair] = (new_executed, new_amount)
            
        else:
            buy_data[pair] = (executed, amount)
    else:
        if pair in sell_data:
            values = sell_data[pair]
            new_amount = values[1] + amount
            new_executed = values[0] + executed
            sell_data[pair] = (new_executed, new_amount)
            
        else:
            sell_data[pair] = (executed, amount)

for filename in glob.glob(os.path.join(constant.PATH, '*.csv')):
    with open(os.path.join(os.getcwd(), filename), 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        # line_count = 0
        for row in csv_reader:
            num_char = len(row[constant.PAIR]) - constant.LEN 
            executed = row[constant.EXECUTED].replace(',','')
            amount = row[constant.AMOUNT].replace(',','')
            process_pairs(row[constant.PAIR][:-constant.LEN], row[constant.SIDE], float(executed[:-num_char]), float(amount[:-constant.LEN]))
            # if line_count == 0:
            #     print(f'Column names are {", ".join(row)}')
            # print(f'\t{row[constant.DATE]}, {row[constant.PAIR]}, {row[constant.SIDE]}, {row[constant.PRICE]}, {row[constant.EXECUTED]}, {row[constant.AMOUNT]}, {row[constant.FEE]}.')
            # line_count+=1
     

print("-------------\n")
for pair, values in buy_data.items():
    print(f'\t{pair}:{values[1]/values[0]}')

print("-------------\n")
for pair, values in sell_data.items():
    print(f'\t{pair}:{values[1]/values[0]}')