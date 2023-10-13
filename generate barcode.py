# pip install python-barcode

import barcode
from barcode import Code128

def generate_barcode(data):
    code=Code128(data)
    code.save("barcode")
    print("Barcode generated.")

data="1234-5678-9012"
generate_barcode(data)
