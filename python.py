import os
from datetime import datetime

def save_to_vault(data, filename, base_folder='/Users/your_username/Documents/vault_data'):
   date_folder = datetime.now().strftime('%Y-%m-%d')
  
   folder_path = os.path.join(base_folder, date_folder)
   if not os.path.exists(folder_path):
       os.makedirs(folder_path)
     
   full_path = os.path.join(folder_path, filename)
       file.write(data)

   print(f"Data saved to {full_path}")
