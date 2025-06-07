
import pandas as pd
import os

def store_user_info(username, email, role):
    df = pd.DataFrame({"Username": [username], "Email": [email], "Role": [role]})
    if os.path.exists("user_data.csv"):
        df.to_csv("user_data.csv", mode='a', header=False, index=False)
    else:
        df.to_csv("user_data.csv", index=False)
