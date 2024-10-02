import pandas as pd
import json

# Load the list of Excel files
with open("/home/marko/Desktop/arbitragepy/leagues/leagues.txt", "r") as file:
    file_content = file.read()

text_files = json.loads(file_content)
arbitrage = []
arbitrage_values = []

# Process each Excel file
for i in range(len(text_files)):
    file_path = f'/home/marko/Desktop/arbitragepy/dataxlsx/{text_files[i]}.xlsx'  # Replace with your file path
    excel_data = pd.ExcelFile(file_path)

    # Iterate through each sheet
    for sheet_name in excel_data.sheet_names:
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        
        # Ensure the necessary columns exist
        if {'1', '2', 'x'}.issubset(df.columns):
            # Extract maximum values from columns 1, 2, and x
            n = df['1'].max()
            m = df['2'].max()
            z = df['x'].max()
            
            # Calculate the sum of the inverses
            if n > 0 and m > 0 and z > 0:  # Check to avoid division by zero
                arbitrage_value = (1/n) + (1/m) + (1/z)
                if arbitrage_value < 1:
                    arbitrage.append(f"{arbitrage_value} in league({text_files[i]} sheet {sheet_name})")
                    arbitrage_values.append(arbitrage_value)
            else:
                print(f'Invalid values in sheet {sheet_name}')

# Sort the list of arbitrage opportunities
sorted_lst = sorted(arbitrage, key=lambda x: float(x.split()[0]), reverse=False)

# Save the sorted list to a text file
output_file_path = "/home/marko/Desktop/arbitragepy/arbitrage_results/arbarbitrage_opportunities.txt"
with open(output_file_path, "w") as file:
    for item in sorted_lst:
        file.write(item + "\n")

profit = 0
procent = 0
for i in arbitrage_values:
    procent = 100 - i * 100
    profit = profit + 100 / 100 * procent
    procent = 0

print(f"Total profit with 100 stake is {profit}")

print(f"Sorted arbitrage opportunities have been saved to {output_file_path}.")
