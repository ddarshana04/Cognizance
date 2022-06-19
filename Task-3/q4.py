import pandas as pd
ser = pd.Series(['amrita', 'school', 'of', 'engineering', 'chennai' , 'campus'])
print("Given Series: ")
print(ser)
new_ser = ser.map(lambda x: x[0].upper() + x[1:])
print("\nResulting Series :")
print(new_ser)