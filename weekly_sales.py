
weekly_sales = { 
    
    "week1" : 5000,
    "week2" : 25000,
    "week3" : 6000,
    "week4" : 15000,
    "week5" : 20000,
    "week6" : 12000,
    "week7" : 22000,
    "week8" : 8500,
    }


def calculate_total(sales_dict):
   total=0
   for sales in sales_dict.values():
    total = total + sales
   return total 


def calculate_average(sales_dict):
     count = len(sales_dict)
     total = calculate_total (sales_dict)
     average = total /count
     return average 

def classify_week(sales, average):  
   
      if sales >=average:
          return "Above average"
      else:
          return "Below average"

   

print()
print(f"{'LinenLane Weekly Sales Report' : >40}")
print("----------------------------------------------")
print(f"{'week': <12} {'sales' :>12} {'Classification':<18}")
print("______________________________________________")

average = calculate_average(weekly_sales)
for week, sales in weekly_sales.items():
     classification = classify_week(sales, average)
     print( f"{week: <12} {sales :>12,} {classification:<18}")


print("________________________________________________")

print("Summary")
print("________________________________________________")
print("Total sales :",calculate_total(weekly_sales),)
print("Average     :" , calculate_average(weekly_sales))
print("Higest week :", max(weekly_sales.values()))
print("Lowest week :", min(weekly_sales.values()))

print("________________________________________________")



with open ("weekly_sales_report.txt", "w") as f:
    
    # for week, sales in weekly_sales.items():
    #     f.write(f"{week} : {sales}\n")
    f.write("\n")
    f.write("LinenLane Weekly Sales Report\n")
    f.write("-----------------------------------\n")
    average = calculate_average(weekly_sales)
    total = calculate_total(weekly_sales)
    for week, sales in weekly_sales.items():
       classification = classify_week(sales, average)
       f.write(f"{week} {sales} {classification}\n")
    
    f.write("________________________________________________\n")
    f.write("\n")
    f.write("Summary\n")
    f.write("________________________________________________\n")

    f.write(f"{"Total sales :" }{total}\n")
    f.write(f"{"Average     :"}{average}\n")
    f.write(f"{"Higest week :"}{max(weekly_sales.values())}\n")
    f.write(f"{"Lowest week :"}{min(weekly_sales.values())}\n")
    
