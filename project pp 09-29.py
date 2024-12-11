item_dict={}
f=open("D:\\online cloths shop.txt","r")
while True:
    item=f.readline()
    if item=="\n":
        break
    quant=f.readline()
    Unit_Price=f.readline()
    item = item[:len(item)-1]
    quant = int(quant[:len(quant)-1])
    Unit_Price= float(Unit_Price[:len(Unit_Price)-1])

    item_dict[item]=[quant,Unit_Price]
f.close()

def present_data():
    print(30 * "=")
    print("Available Cloths and Quantity In Shop")
    print(30 * "=")
    for x in item_dict:
        print(x, (20 - len(x)) * ' ', (6 - len(str(item_dict[x][0]))) * ' ', item_dict[x][0])
    print(30 * '-')





def dec_quant(item, amount):
    item_dict[item][0] -= amount


def inc_quant(item, amount):
    item_dict[item][0] += amount


def receive_order():
    while True:
        item = input("Item (type X to stop): ")
        if item == 'X':
            break
        amount = int(input("Amount: "))
        if item not in item_dict:
            print('New item found!')
            uprice = float(input('Enter the unit price: '))
            item_dict[item] = [amount, uprice]
            continue
        inc_quant(item, amount)
    # present_data()


def process_demand():
    demand_list = []
    while True:
        item = input('Item (type X to stop): ')
        if item == 'X':
            break
        if item not in item_dict:
            print('Sorry the item is not avalable')
            continue
        amount = int(input('Amount: '))
        if amount > item_dict[item][0]:
            print(f'Total {item_dict[item][0]} pcs Available')
            continue
        dec_quant(item, amount)
        demand_list += [item, amount, item_dict[item][1], amount * item_dict[item][1]],
    print(40 * '=')
    print('** Payment Receipt **'.center(40))
    print(40 * '=')
    print('Item name', 3 * ' ', 'Quantity', 'U.Price', ' ', 'S.Total')
    print(40 * '-')
    tprice = 0
    for x in demand_list:
        tprice += x[3]
        print(x[0].title(), (14 - len(x[0])) * ' ', (5 - len(str(x[1]))) * ' ', x[1],
              (6 - len(str('%.2f' % x[2]))) * ' ', '%.2f' % x[2], (8 - len(str('%.2f' % x[3]))) * ' ', '%.2f' % x[3])
    print(40 * '-')
    tprice = '%.2f' % tprice
    print('Total Price', (27 - len(str(tprice))) * ' ', tprice)
    print(40 * ' ')
    # present_data()



while True:
    present_data()
    print('Choose an Option: ')
    print('Type "1" : To process demand ')
    print('Type "2" : To Receive Order ')
    print('Type "3" : To Exit the program ')
    choice=input('Choice: ')
    if choice=='1':
        process_demand()
    elif choice=='2':
        receive_order()
    elif choice=='3':
        break
    else:
        continue

f=open("D:\online cloths shop.txt","w")
for x in item_dict:
    f.write(x+'\n')
    f.write(str(item_dict[x][0])+'\n')
    f.write(str(item_dict[x][1])+'\n')
f.write('\n')
f.close()
