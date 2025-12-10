# sudo apt install pandas --break-system-packages
# sudo apt install odfpy --break-system-packages
import pandas as pd

df = pd.read_excel('empresa.ods', engine='odf')
data = df.to_dict(orient='records')
print(data)
