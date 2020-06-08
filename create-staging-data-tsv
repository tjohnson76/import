# import re - the Python Regular Expressions library
# import csv - the Python Comma-Separated Values library
import csv

from pymarc import MARCReader

# create a CSV file - note tab delimiter would be '/t'
csv_out = csv.writer(open('marc_record.tsv', 'w'), delimiter='\t')

# write a header row in your CSV file
csv_out.writerow(['bibkey','location', 'owning_lib', 'callnum_prefix', 'callnum', 'callnum_suffix', 'barcode', 'item_type'])

# trim OCLC number prefixes (ocn, ocm, OCoLC)
with open('marc_record.mrc', 'rb') as fh:
    reader = MARCReader(fh)
    for record in reader:

        # Get bibkey (035 |a)
        if record['035']['b'] is not None:
                # bibkey = record['035']['a']
                bibkey = record['035']['b']

        # Get location (852 |c)
        if record['852'] is not None:
            if record['852']['c'] is not None:
                # location = record['852']['c']
                location = record['852']['c']
            else:
                location = '\\N'
        else:
            location = '\\N'


        owning_lib = 'SBPL'

            # callnum_prefix
        if record['852'] is not None:
            if record['852']['k'] is not None:
                callnum_prefix = record['852']['k']
            # if no 852|k, skip
            else:
                callnum_prefix = '\\N'
        # if no 852, skip
        else:
            callnum_prefix = "\\N"

            # callnum
        if record['852'] is not None:
            if record['852']['j'] is not None:
                    callnum = record['852']['j']
                # if no 852|j, skip
            else:
                    callnum = "\\N"
            # if no 852, skip
        else:
                callnum = '\\N'


            # callnum_suffix
        if record['852'] is not None:
            if record['852']['h'] is not None:
                callnum_suffix = record['852']['h']
                # if no 852|h, skip
            else:
                callnum_suffix = '\\N'
            # if no 852, skip
        else:
           callnum_suffix = '\\N'

              # barcode
        if record['852'] is not None:
            if record['852']['p'] is not None:
                barcode = record['852']['p']
                    # if no 852|p, skip
            else:
                barcode = '\\N'
                # if no 852, skip
        else:
            barcode = '\\N'

        if record['852'] is not None:
            if record['852']['g'] is not None:
                item_type = record['852']['g']
                    # if no 852|g, skip
            else:
                item_type = '\\N'
                # if no 852, skip
        else:
            item_type = '\\N'

        # print(staging materials)
        csv_out.writerow([bibkey, location, owning_lib, callnum_prefix, callnum, callnum_suffix, barcode, item_type])

