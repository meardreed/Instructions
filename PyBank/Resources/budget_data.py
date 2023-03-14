import os

import csv

file_to_save = os.path.join("PyBank\Resources", "budget_analysis.txt")

csvpath = os.path.join('Pybank\Resources', 'budget_data.csv')

# initiate variables

total_months = 0
total_pl = 0
total_changes = 0
changes = 0

# create lists to store data
change_list = []
date_list = []
greatest_inc = {}
greatest_dec = {}


#  open and read csv
with open(csvpath,encoding='utf') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    #read header row first
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    
    first_row = next(csvreader)   
    total_pl = total_pl + int(first_row[1])
    previous = int(first_row[1])
    
    # loop for total months, P/L, avg changes for each row
    for row in csvreader:
        
        total_months = total_months + 1    

        total_pl = total_pl + int(row[1])

        changes = int(row[1]) - previous

        total_changes = (total_changes + changes)/ total_months

         # save months in a list
        date_list.append(row[0])

        # save monthly changes in a list
        change_list.append(changes)

        # Find the min,max values in changes list
        greatest_inc = max(change_list)
        greatest_dec = min(change_list)

        #Assign corresponding dates to min,max changes
        increase_date = date_list[change_list.index(greatest_inc)]
        decrease_date = date_list[change_list.index(greatest_dec)]
      


    # return calculations values
    print("Financial Analysis")
    print("----------------------------------")
    print("Total Months :"  +  str(total_months))
    print("Total :"  + str(total_pl))
    print("Average Changes :"  + str(total_changes))
    print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_inc) + ")")
    print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_dec)+ ")")


# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    budget_analysis = (
                        "Financial Analysis"+ '.\n'
                         "----------------------------------"+ '.\n',
                         "Total Months :"  +  str(total_months)+ '.\n', 
                        "Total :"  + str(total_pl)+ '.\n', 
                        "Average Changes :"  + str(total_changes)+ '.\n',
    "Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_inc) + ")"+ '.\n',
    "Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_dec)+ ")"+ '.\n')
    print(budget_analysis)

    # Save the final vote count to the text file.
    txt_file.writelines(budget_analysis)



