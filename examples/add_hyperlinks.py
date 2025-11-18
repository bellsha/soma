#!/usr/bin/env python3
import csv

input_file = "measurement_class_attributes.csv"
output_file = "measurement_class_attributes_with_links.csv"
base_url = "https://ehs-data-standards.github.io/outcomes-working-group/elements/"

basic_types = {"string", "uriorcurie"}

with open(input_file, 'r', encoding='utf-8') as infile, \
     open(output_file, 'w', encoding='utf-8', newline='') as outfile:
    
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    
    for row_num, row in enumerate(reader):
        if row_num == 0:
            writer.writerow(row)
            continue
        
        if len(row) >= 4:
            measurement_class = row[0]
            attribute_name = row[1]
            range_type = row[3]
            
            measurement_class_link = f'=HYPERLINK("{base_url}{measurement_class}/","{measurement_class}")'
            row[0] = measurement_class_link
            
            attribute_link = f'=HYPERLINK("{base_url}{attribute_name}/","{attribute_name}")'
            row[1] = attribute_link
            
            if range_type not in basic_types and not range_type.startswith('=HYPERLINK'):
                range_link = f'=HYPERLINK("{base_url}{range_type}/","{range_type}")'
                row[3] = range_link
        
        writer.writerow(row)

print(f"Done! Output written to {output_file}")