import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

df=pd.read_csv("data/TrafficVolumeData.csv")

df["date_time"]=pd.to_datetime(df["date_time"])
df["hour"]=df["date_time"].dt.hour

print(df[["date_time","hour"]].head())
print("shape:",df.shape)

print("\ncolumns:")
for c in df.columns:
    print(c)

print("\nfirst rows:")
print(df.head())

weather_cols=[
"air_pollution_index",
"humidity",
"wind_speed",
"wind_direction",
"visibility_in_miles",
"dew_point",
"temperature",
"rain_p_h",
"snow_p_h",
"clouds_all"
]

print("\nWeather columns used for PCA:")
print(weather_cols)

print("\nPreview of weather data:")
print(df[weather_cols].head())



X=df[weather_cols]

scaler=StandardScaler()
X_scaled=scaler.fit_transform(X)

print("\nScaled weather sample:")
print(X_scaled[:5])

pca=PCA(n_components=1)
pc1=pca.fit_transform(X_scaled)

df["weather_index"]=pc1

print("\nWeather index (PC1) sample:")
print(df["weather_index"].head())

M=20

df["weather_bin"]=pd.cut(df["weather_index"],bins=M,labels=False)

print("\nWeather bins sample:")
print(df[["weather_index","weather_bin"]].head())

grid=df.groupby(["hour","weather_bin"])["traffic_volume"].mean().unstack(fill_value=0)

print("\nGrid shape:")
print(grid.shape)

print("\nGrid sample:")
print(grid.head())

grid.to_csv("results/grid.csv",header=False,index=False)

print("\nGrid saved to results/grid.csv")