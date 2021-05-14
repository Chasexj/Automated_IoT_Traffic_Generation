import pandas as pd

df = pd.read_csv("sample.csv")

#number of buttons
# label = []
# num_b = 4
# ins_per_b = int(df.shape[0]/4)
# for i in range(num_b):
#     for j in range(ins_per_b):
#         label.append(i)
# while(len(label)<df.shape[0]):
#     label.append(num_b-1)

# df['label'] = label
# df.to_csv('labeled.csv',index=False)

label = []
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