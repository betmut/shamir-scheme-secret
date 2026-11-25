from random import sample
from pathlib import Path
import modules.shamir_secret_sharing as shamir
import matplotlib.pyplot as plt
import seaborn as sns

secret = 76
n = 40
threshold = 20
chosen_share_points = 21

# Create Polynomial
polynomial = shamir.create_polynomial(secret, threshold)

# Create n shares
point_of_shares = shamir.create_shares(n, polynomial)
points, shares = zip(*point_of_shares)

# Pick sample of share points 
picked_point_of_shares = sample(point_of_shares, k = chosen_share_points)
picked_points, picked_share_value = zip(*picked_point_of_shares)

# interpolation
recovered_secret = shamir.lagrange_interpolation(0, picked_points, picked_share_value)

# Plot the scatterplot
sns.scatterplot(x=points, y=shares, label="Generated Shares")
sns.scatterplot(x=picked_points, y=picked_share_value, label=f"Picked Shares (k = {chosen_share_points})")
sns.scatterplot(x=[0], y=[recovered_secret], label="Recovered Secret")
plt.suptitle(f"Shamir Secret Sharing (n = {n}, k = {threshold}, Secret = {secret})")
plt.title(f"GF({shamir.PRIME})")
plt.xlabel("Points")
plt.ylabel("Shares")
plt.legend()

plt.annotate(
        f"({0}, {recovered_secret})",
        xy=(0, recovered_secret),       # point to label
        xytext=(8, 8),                 # label offset in points
        textcoords="offset points",
        color="green"
)

# Define the folder and create it if it doesn't exist
output_dir = Path("plots") / "figs"
output_dir.mkdir(parents=True, exist_ok=True)

plt.savefig(output_dir / "shamir.png", dpi=300, bbox_inches="tight")
plt.show()


