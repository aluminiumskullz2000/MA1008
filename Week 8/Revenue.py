revenue = {"Jurong":1620.55, "Bedok":2598.60, "Sengkang":1886.40}

def add_income (revenue,shop,income):
    if shop in revenue:
        revenue[shop] += income
    else:
        revenue[shop] = income
