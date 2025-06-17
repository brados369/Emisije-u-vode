import requests
import pandas as pd
import shutil
import os
from datetime import datetime

# 📌 Permalink dataset-a
dataset_url = "<div data-udata-dataset="6616c41f944f536d39de263f"></div><script src="https://data.gov.rs/static/oembed.js" async defer></script>"

# 📌 Lokalni fajlovi (prilagođeno tvom GitHub repozitorijumu)
objedinjena_baza = "emisije_vode.xlsx"
analiza_notebook = "emisije_vode.ipynb"

# 📌 Generisanje timestamp-a za verzionisanje
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# 1️⃣ Sačuvaj prethodnu verziju baze pre ažuriranja
shutil.copy(objedinjena_baza, f"emisije_vode_{timestamp}.xlsx")

# 2️⃣ Preuzmi novi dataset (CSV)
df_novi = pd.read_csv(dataset_url)

# 3️⃣ Učitaj postojeću objedinjenu bazu
df_objedinjeni = pd.read_excel(objedinjena_baza)

# 4️⃣ Dodaj nove podatke bez dupliranja
df_final = pd.concat([df_objedinjeni, df_novi]).drop_duplicates()

# 5️⃣ Sačuvaj ažuriranu bazu
df_final.to_excel(objedinjena_baza, index=False)

# 6️⃣ Pretvori analizu u HTML i PDF format sa timestamp-om
os.system(f"jupyter nbconvert --to html {analiza_notebook} --output emisije_vode_{timestamp}.html")
os.system(f"jupyter nbconvert --to pdf {analiza_notebook} --output emisije_vode_{timestamp}.pdf")

# 7️⃣ Dodaj verzije na GitHub
os.system(f"git add emisije_vode.xlsx emisije_vode_{timestamp}.xlsx emisije_vode_{timestamp}.html emisije_vode_{timestamp}.pdf")
os.system(f"git commit -m 'Ažuriranje podataka i analize - {timestamp}'")
os.system("git push origin main")

print(f"🚀 Baza i analiza su ažurirane! Verzija: {timestamp}")

