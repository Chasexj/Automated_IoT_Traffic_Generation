import pandas as pd


# labeling the nprint encoded csv using the recorded timestamps
df = pd.read_csv("sample.csv")

label = []
# numbers specify time when different button is pressed --------------------- modify as needed
for i in range(df.shape[0]):
    if i <= 1920: 
        label.append(0)
    elif i > 1920 and i <= 3655:
        label.append(1)
    elif i > 3655 and i <= 5411:
        label.append(2)
    else:
        label.append(3)
while(len(label)<df.shape[0]):
    label.append(3)

df['label'] = label
df.to_csv('labeled.csv',index=False)