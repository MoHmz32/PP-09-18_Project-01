item_dict={}
f=open("D:\Hamza's Hardware Shop.txt","r")
while True:
    item=f.readline()
    if item=="\n":
        break
    qntt=f.readline()
    uprc=f.readline()
    item=item[:len(item)-1]
    qntt=int(qntt[:len(qntt)-1])
    uprc=float(uprc[:len(uprc)-1])
    item_dict[item]=[qntt,uprc]
f.close()

def present_data():
  print(32*"=")
  print("Available Items and Quantity :")
  print(32*"=")
  for x in item_dict:
    print(x,(20-len(x))*" ",
    (8-len(str(item_dict[x][0])))*" ",item_dict[x][0])
  print(32*"-")

def dec_quant(item,amount):
  item_dict[item][0]-=amount

def inc_quant(item,amount):
  item_dict[item][0]+=amount

def receive_order():
  while True:
    item=input("Item (Type 'x' to finish):")
    if item=="x":
      break
    amnt=int(input("Amount :"))
    if item not in item_dict:
      print("New item found!")
      uprice=float(input("Enter the unit price:"))
      item_dict[item]=[amnt,uprice]
      continue
    inc_quant(item,amnt)

def process_demand():
  demand_list=[]
  while True:
    item=input("Item (Type 'x' to finish):")
    if item=="x":
      break
    if item not in item_dict:
      print("Sorry! Item is not available.")
      continue
    amnt=int(input("Amount :"))
    if amnt>item_dict[item][0]:
      print(f"Total {item_dict[item][0]} pcs available!")
      continue
    dec_quant(item,amnt)
    demand_list+=[item,amnt,item_dict[item][1],amnt*item_dict[item][1]],
  print(40*"=")
  print("Hamza's Hardware Shop".center(40))
  print("~ Payment Receipt ~".center(40))
  print(40*"=")
  print("Item Name",3*" ","Quant.","U.Price",2*" ","S.Total")
  print(40*"-")
  tprice=0
  for x in demand_list:
    tprice+=x[3]
    print(x[0].title(),(12-len(x[0]))*" ",
    (5-len(str(x[1])))*" ",x[1],
    (6-len(str("%.2f"%x[2])))*" ","%.2f"%x[2],
    (9-len(str("%.2f"%x[3])))*" ","%.2f"%x[3])
  print(40*"-")
  tprice="%.2f"%tprice
  print("Total Price:",(25-len(str(tprice)))*" ",tprice)
  print(40*"=")
mylist = []
mylist
mylist += ["item",50],
mylist
mylist += ["item2", 150]
mylist

while True:
  present_data()
  print("Choose an option :")
  print("Type '1' to process demand.")
  print("Type '2' to receive order.")
  print("Type '3' to exit.")
  choice=input("Enter your choice :")
  if choice=="1":
    process_demand()
  elif choice=="2":
    receive_order()
  elif choice=="3":
    break
  else:
    continue

f=open("D:\Hamza's Hardware Shop.txt","w")
for x in item_dict:
    f.write(x+"\n")
    f.write(str(item_dict[x][0])+"\n")
    f.write(str(item_dict[x][1])+"\n")
f.write("\n")
f.close()
