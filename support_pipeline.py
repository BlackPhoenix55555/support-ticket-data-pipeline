# support_pipeline.py
import pandas as pd
import os

class DataPipeline:
    def __init__(self, raw_path="data/raw_tickets.csv", output_dir="data/output"):
        self.raw_path = raw_path
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)
        self.data = None

    # Step 1: Extract
    def extract(self):
        print("[INFO] Extracting data...")
        self.data = pd.read_csv(self.raw_path)
        print(f"[INFO] {len(self.data)} rows loaded.")

    # Step 2: Transform
    def transform(self):
        print("[INFO] Transforming data...")
        self.data['Created_Date'] = pd.to_datetime(self.data['Created_Date'], errors='coerce')
        self.data['Resolved_Date'] = pd.to_datetime(self.data['Resolved_Date'], errors='coerce')
        self.data['Priority'] = self.data['Priority'].fillna("Medium")
        self.data.dropna(subset=['Ticket_ID', 'Created_Date'], inplace=True)
        print("[INFO] Transformation complete.")

    # Step 3: Validate
    def validate(self):
        print("[INFO] Validating data...")
        errors = []
        if self.data['Ticket_ID'].duplicated().any():
            errors.append("Duplicate Ticket_IDs found")
        if self.data['Resolved_Date'].isnull().any():
            errors.append("Missing Resolved_Date found")
        if errors:
            print("[WARNING] Validation issues detected:")
            for err in errors:
                print(f"- {err}")
        else:
            print("[INFO] Data validation passed.")

    # Step 4: Reporting
    def report(self):
        print("[INFO] Generating reports...")

        # Monthly ticket counts by priority
        report = self.data.groupby([self.data['Created_Date'].dt.to_period('M'), 'Priority']) \
                          .size().reset_index(name='Ticket_Count')
        report.to_csv(os.path.join(self.output_dir, "tickets_report.csv"), index=False)

        # Tickets with long resolution times (>30 days)
        self.data['Resolution_Days'] = (self.data['Resolved_Date'] - self.data['Created_Date']).dt.days
        anomalies = self.data[self.data['Resolution_Days'] > 30]
        anomalies.to_csv(os.path.join(self.output_dir, "anomalous_tickets.csv"), index=False)

        print(f"[INFO] Reports saved in {self.output_dir}")

    # Run full pipeline
    def run(self):
        self.extract()
        self.transform()
        self.validate()
        self.report()
        print("[INFO] Pipeline execution complete.")

# ----------------------------
# Execute Pipeline
# ----------------------------
if __name__ == "__main__":
    pipeline = DataPipeline()
    pipeline.run()

