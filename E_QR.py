import qrcode as qr
import pandas as pd

df = pd.read_excel('Book1.xlsx', header=None)
df.columns = ['Name', 'Link']  # Rename columns
print(df)
for index, row in df.iterrows():
    try:
        image_name = row['Name'] 
        link = row['Link']       
        img = qr.make(link)
        img.save(f"{image_name}.png")
        print(f"Saved {image_name}.png for link {index+1} : {link}")

    except Exception as e:
        print(f"Failed to generate QR code for {row['A']} with link {row['B']}: {e}")

print("QR Code images have been generated and saved.")
