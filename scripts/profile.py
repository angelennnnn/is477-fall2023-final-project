

import pandas as pd
from ydata_profiling import ProfileReport

csv_file_path = r'C:\Users\Angel\Desktop\IS477-finalproject\data\breast_cancer_wisconsin\breast_cancer_wisconsin.csv'

df = pd.read_csv(r'C:\Users\Angel\Desktop\IS477-finalproject\data\breast_cancer_wisconsin\breast_cancer_wisconsin.csv')

profile = ProfileReport(df, title="Breast Cancer Wisconsin Profiling Report")

profile.to_file(r'C:\Users\Angel\Desktop\IS477-finalproject\profiling\report.html')
