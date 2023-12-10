import pandas as pd

# 加載CSV文件
df1 = pd.read_csv('./facebook-recruiting-iv-human-or-bot/.csv')
df2 = pd.read_csv('file2.csv')

# 根據ID合併這兩個DataFrame
merged_df = pd.merge(df1, df2, on='id', how='inner')

# 檢查合併後的DataFrame
print(merged_df.head())
