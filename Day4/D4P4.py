import csv
from pathlib import Path

CATALOG = Path("products.csv")
IN_STOCK_REPORT = Path("in_stock_report.csv")

SAMPLE_ROWS = [
    {"id":"101","name":"Iphone 200","price":"499999","in_stock":"no"},
    {"id":"102","name":"Mysore Pak","price":"499","in_stock":"yes"},
    {"id":"103","name":"Smart Phone","price":"99999","in_stock":"yes"},
    {"id":"104","name":"Charger 100w","price":"499999","in_stock":"no"},
]

def write_catalog(rows:list[dict[str,str]],path:Path = CATALOG)->None:
    fieldnames = ["id","name","price","in_stock"]

    with path.open("w",newline="",encoding="utf-8") as handle:
        writer = csv.DictWriter(handle,fieldnames)
        writer.writeheader() #add column names as first row
        writer.writerows(rows)

def read_catlog(path:Path = CATALOG)->list[dict[str,str]]:
    if not path.exists():
        return []
    
    with path.open("r",newline="",encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def filter_in_stock(rows:list[dict[str,str]])->list[dict[str,str]]:
    result = []
    for row in rows:
        if row["in_stock"].strip().lower() == "yes":
            result.append({**row,"price":float(row["price"])}) 

    return result

def write_report(rows: list[dict[str,str]], path: Path = IN_STOCK_REPORT)->None:
    if not rows:
        return

    with path.open("w",newline="",encoding="utf-8") as handle:
        writer = csv.DictWriter(handle,fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    write_catalog(SAMPLE_ROWS)
    catalog = read_catlog() #all products
    available = filter_in_stock(catalog) #filtered products
    write_report(available)
    print(f"Total Products: {len(catalog)}")
    print(f"Available Products: {len(available)}")

    for item in available:
        print(f"{item['name']}: INR {item['price']:,.2f}")

