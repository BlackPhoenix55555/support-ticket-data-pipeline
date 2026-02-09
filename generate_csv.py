# generate_csv.py
import pandas as pd
from datetime import datetime, timedelta
import random
import os

os.makedirs("data", exist_ok=True)

# ----------------------------
# Generate Sample Tickets
# ----------------------------
num_tickets = 50
ticket_data = {
    "Ticket_ID": range(1, num_tickets+1),
    "Created_Date": [datetime(2026,2,1) + timedelta(days=random.randint(0,30)) for _ in range(num_tickets)],
    "Resolved_Date": [datetime(2026,2,1) + timedelta(days=random.randint(1,40)) for _ in range(num_tickets)],
    "Priority": [random.choice(["Low", "Medium", "High"]) for _ in range(num_tickets)],
    "Assigned_To": [random.choice(["Alice","Bob","Charlie"]) for _ in range(num_tickets)]
}

tickets_df = pd.DataFrame(ticket_data)
tickets_df.to_csv("data/raw_tickets.csv", index=False)
print("[INFO] Sample raw_tickets.csv created in data/")

