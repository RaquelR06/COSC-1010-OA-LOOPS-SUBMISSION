# Program 1: Bug Collector

total_bugs = 0  # Initialize running total

# Loop for 5 days
for day in range(1, 6):
    bugs = int(input(f"Enter the number of bugs collected on day {day}: "))
    total_bugs += bugs  # Add daily bugs to running total

# Display the final total
print(f"\nTotal bugs collected over 5 days: {total_bugs}")
