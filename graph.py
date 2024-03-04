import matplotlib.pyplot as plt
import numpy as np

# Data from your experiments
bit_sizes = [8, 10, 12, 14, 16, 18, 20, 22]

# Data for preimage attack
avg_attempts_preimage = [129.1, 458.16, 1592.38, 7675.5, 32840.4, 129764.24, 592091.88, 2564566]

# Data for collision attack
avg_attempts_collision = [245.3, 906.42, 3188.77, 15432.1, 65680.8, 259638.12, 1180145.44, 5129122]

theoretical_preimage = 2 ** (np.array(bit_sizes) / 2 - 1)  # Theoretical preimage difficulty
theoretical_collision = 2 ** (np.array(bit_sizes) / 2 - 1)  # Theoretical collision difficulty

# Create a single figure with two subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 12))

# Preimage attack graph
ax1.plot(bit_sizes, avg_attempts_preimage, marker='o', label='Average Attempts (Preimage)')
ax1.plot(bit_sizes, theoretical_preimage, 'r--', label='Theoretical Difficulty (Preimage)')
ax1.set_title('Preimage Attack Difficulty at Different Bit Sizes')
ax1.set_xlabel('Bit Size')
ax1.set_ylabel('Average Number of Attempts')
ax1.legend()
ax1.grid(True)

# Collision attack graph
ax2.plot(bit_sizes, avg_attempts_collision, marker='o', label='Average Attempts (Collision)')
ax2.plot(bit_sizes, theoretical_collision, 'r--', label='Theoretical Difficulty (Collision)')
ax2.set_title('Collision Attack Difficulty at Different Bit Sizes')
ax2.set_xlabel('Bit Size')
ax2.set_ylabel('Average Number of Attempts')
ax2.legend()
ax2.grid(True)

# Adjust layout to prevent overlapping
plt.tight_layout()

# Show the combined figure
plt.show()

print()
