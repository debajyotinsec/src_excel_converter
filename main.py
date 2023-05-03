
#
# Concat multiple sheets into one text file. You can easily dump it to spreadsheet as well.
#

import pandas as pd

input_file = 'input/EDW Components.xlsx'
xlsx = pd.ExcelFile(input_file)
sheets = xlsx.sheet_names
out_file = open('output/Combined_file.txt', 'w')

# print (sheets)
# print (len(sheets))

for each_sheet in sheets:
    # each_sheet = 'VEHICLE_MAKE_MODEL'
    print ("Processing sheet - {}".format(each_sheet))
    excel_df = pd.read_excel(input_file, sheet_name=each_sheet)
    # print (excel_df.head)
    line_counter = 0
    for each_line in excel_df.itertuples():
        line_counter = line_counter + 1
        # print (each_line)
        index, data = each_line
        if line_counter > 2:
            data_line = each_sheet + "~" + data.strip()
            print (data_line, file=out_file, end='\n')
        else:
            #
            # First 3 lines had header, bypassing them
            #
            if (each_sheet in data) or ("SCHEMA" in data) or ("Columns Name" in data):
                pass
            else:
                print ("Issue with processing tab - {} - {}".format(each_sheet, data))
                exit(0)
    # if each_sheet == 'EIS_FACT':
    #     break

    


