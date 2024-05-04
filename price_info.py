
#price_list={'apple' : 1.20, 'orange':1.40, 'watermelon': 6.50, 'pineapple': 2.70, 'pear' : 0.90, 'papaya': 2.95, 'pomegranate': 4.95 }
#price_list={'guava' : 2.20, 'orange':1.50, 'watermelon': 9.24, 'pineapple': 2.71, 'pear' : 1.90, 'papaya': 9.95, 'pomegranate': 8.95, 'passionfruit': 11.32}
#quantity_list= {'apple': 5, 'orange':5, 'watermelon': 1, 'pineapple': 2, 'pear' : 10, 'papaya': 1, 'pomegranate': 2}
#quantity_list={'guava' : 7, 'orange':9, 'watermelon':12, 'pineapple':5, 'pear' :3, 'papaya':6, 'pomegranate':1, 'passionfruit':12}

def total_cost_shopping(price_list, quality_list):
    total_cost = 0
    for key in price_list.keys():
        if key in quality_list:
            # complete the implementation below:
            total_cost += price_list[key]*quality_list[key]

    return total_cost

def cost_of_fruits(fruit, quantity, price_list):
    for key in price_list.keys():
        if key == fruit:
            cost = quantity*price_list[key]
            break

    return cost

def main():

    #cost_of_fruits('passionfruit', 10)
    total_cost1 = total_cost_shopping(input(), input())
    print("Total cost = "+ str(total_cost1))
    cost_of = cost_of_fruits(input(), input(), input())
    print("Cost of fruits = " + str(cost_of))



if __name__ == "__main__":
    main()