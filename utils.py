
import pandas as pd
import os

def store_user_info(username, email, role):
    df = pd.DataFrame({"Username": [username], "Email": [email], "Role": [role]})
    if os.path.exists("user_data.csv"):
        df.to_csv("user_data.csv", mode='a', header=False, index=False)
    else:
        df.to_csv("user_data.csv", index=False)

import json

def store_user_info(username, email, role):
    user_info = {
        "username": username,
        "email": email,
        "role": role,
        "plan": "Free"  # default, can update later from Plans & Billing page
    }

    with open("user_info.json", "w") as f:
        json.dump(user_info, f)

