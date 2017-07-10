prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
    }

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
    }

for x in prices:
   print "%s price: %s stock: %d" %(x,prices[x],stock[x])


total = 0
for k in prices:
    total += prices[k]*stock[k]
    print "%s %s" %(k,total)

def compute_bill(food):
        total = 0
        for item in food:
                if stock[item] > 0:
                    total += prices[item]

        print total
        return total


for x in stock:
        print stock[x]


sandeep = {
    "name":"dsaf"

}

for x in sandeep:
    print sandeep[x]
