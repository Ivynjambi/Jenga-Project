print("This is a Jenga Project")
print()

print("The project explores one of the datasets provided by openAfrica; Selected")
print("Food Prices Watch in Nigeria. The data provided in form of a CSV file.")
print()

print("The file contains prices of food items from January 2017 to April 2020,")
print("with an entry for each month, towns with highest and lowest priced food items and more.")
print()

print("The main objective of this project is plotting and data visualization.")
print("That is plotting different food prices over time and comparing different")
print("food items.")
print()

print("Required Python packages are imported. Pandas and Matplotlib are used.")
print()
print("Since from our objective we know we need the food prices from 2017-2020,")
print("we source the dataset from openAfrica and review it.")
print("Since we have limited knowledge on cleaning using Pandas, it is agreed")
print("that most of the cleaning process and modifications are to be done using excel.")
print()
print("Columns that don't involve the food item labels and monthly prices are deleted,")
print("as they are not needed for our objective. The new csv file is saved as,")
print(" 'foods nigeria.csv'.")
print()

print("The next step we take, is to read data from the CSV file and viewing part")
print("of the data by looking at the first and last 5 rows in transpose format")
print("to give us an idea of what the data contains.")
print()
print("To understand the data better 'info' and 'describe' are used.")
print("The next step is to get into visualizing the data.")
print("Since the item labels are long, we shorten them by modifying the CSV file")
print("as F(n-1) with 'F' standing for food and (n-1) the position of the item")
print("from the original item labels list that is defined.")
print()

print("Since the CSV file is modified, we save the new file as 'prices'")
print("From the objective, we need plots to visualize the data, Matplotlib is used here.")
print("The effective plots we'll use are bar, scatter and line plots, and a histogram for better understanding.")
print()
print("We get the average of the prices over the years and get a bar plot of the")
print("different food items against the average of the food prices from 2017-2020")
print("From this we can clearly view items with the highest and lowest prices and more.")
print()

print("Next, we look into a scatter plot of the prices of different food items")
print("during April 2017 and Aprl 2020, to look into whether there is much change within 3 years.")
print("From this we note that there is not much change between the prices of different")
print("food items within 3 years, and there is a strong, positive, linear association")
print("between the prices from April 2017 and April 2020, with a few outliers above 1500 Naira")
print("Right after we get the food items whose prices were constantly above 1500 Naira.")
print()

print("A histogram of the average prices is plotted to understand the distribution of the data.")
print("From this we learn that it has a right-skewed distribution, with mean as the")
print("largest of the measures of central tendancy, located to the right and mode")
print("as the smallest of the measures of central tendancy located to the left.")
print()

print("We look into plotting the data yearly, and have the file modified using excel")
print("and the new CSV file is 'foods-yr'")
print("We view part of the data by looking at the first 5 rows with the label 'Years' as the set index.")
print()

print("We look into some line graphs of different food items over the years")
print("2017-2020, to study whether there are any noticable patterns.")
print("From this we note that there is a pattern where prices increase after 2019")
print("Looking into this further, we note that the central bank in Nigeria was")
print("ordered to stop providing foreign exchange for food and fertilizer imports,")
print("in an effort to boost local farming production, which in turn has had great effects.")
print()

print("Finally, our objectives have been met, plots have been made and the data better understood.")
print("In time, this project can be made better and efficient.")

