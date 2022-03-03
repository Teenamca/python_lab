from datetime import datetime
current_year=datetime.today().year
final_year=int(input("Enter the last year"))
print("List of leap years")
for year in range(current_year,final_year):
    if(year%4==0)and(year%100!=0)or(year%400==0):
        print(year)