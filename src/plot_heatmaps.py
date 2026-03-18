import pandas as pd
import matplotlib.pyplot as plt

z=pd.read_csv("results/grid.csv",header=None)
zp=pd.read_csv("results/seq_output.csv",header=None)

plt.figure(figsize=(8,5))
plt.imshow(z,aspect="auto")
plt.colorbar(label="traffic_volume")
plt.xlabel("weather_bin")
plt.ylabel("hour")
plt.title("Original grid Z(x,y)")
plt.tight_layout()
plt.savefig("plots/grid_heatmap.png",dpi=200)
plt.close()

plt.figure(figsize=(8,5))
plt.imshow(zp,aspect="auto")
plt.colorbar(label="traffic_volume")
plt.xlabel("weather_bin")
plt.ylabel("hour")
plt.title("Smoothed grid Z'(x,y)")
plt.tight_layout()
plt.savefig("plots/smoothed_heatmap.png",dpi=200)
plt.close()

print("saved plots/grid_heatmap.png")
print("saved plots/smoothed_heatmap.png")
