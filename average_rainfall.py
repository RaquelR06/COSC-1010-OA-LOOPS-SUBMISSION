# Program 2: Average Rainfall

# Ask user for the number of years
years = int(input("Enter the number of years: "))

total_rainfall = 0.0

# Outer loop for each year
for year in range(1, years + 1):
    print(f"\n--- Year {year} ---")
    # Inner loop for 12 months
    for month in range(1, 13):
        rainfall = float(input(f"Enter inches of rainfall for month {month}: "))
        total_rainfall += rainfall

# Calculate total months and average rainfall per month
total_months = years * 12
average_rainfall = total_rainfall / total_months

# Display results
print("\n=== Summary ===")
print(f"Total months: {total_months}")
print(f"Total rainfall: {total_rainfall:.2f} inches")
print(f"Average rainfall per month: {average_rainfall:.2f} inches")
