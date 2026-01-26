library_inventory={"One Hundred Years of Solitude":{"price":10,
                                                    "stock": 2
                                                    },
                   "Rich Dad Poor Dad":{"price":8,
                                        "stock": 5
                                        },
                   "The Prophet":{"price":6,
                                  "stock": 9
                                  }
                   }
def calculate_total(price,quantity,tax=0.05):
    n=price*quantity
    c=n*tax
    return n+c
storage_grid=[
    [2,5,3],
    [2,9,7],
    [6,7,5]
    ]
for i in storage_grid:
    for m in i:
        print (m,end=(' '))
    print ()
for i,x in library_inventory.items():
    print(i)
    for m ,n in x.items():
        print(m,n)
    print ()
library_inventory["One Hundred Years of Solitude"]["rating"] = 4.5
