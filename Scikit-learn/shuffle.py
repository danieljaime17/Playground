import matplotlib.pyplot as plt
from sklearn.datasets import make_moons

# Generar datos con shuffle=True
X_shuffled, y_shuffled = make_moons(n_samples=100, noise=0.1, random_state=42, shuffle=True)

# Generar datos con shuffle=False
X_not_shuffled, y_not_shuffled = make_moons(n_samples=100, noise=0.1, random_state=42, shuffle=False)

# Crear figura y subgráficos
fig, axs = plt.subplots(1, 2, figsize=(12, 5))

# Subplot 1: Datos con shuffle=True
axs[0].scatter(X_shuffled[:50, 0], X_shuffled[:50, 1], c='blue', label='Clase 0')
axs[0].scatter(X_shuffled[50:, 0], X_shuffled[50:, 1], c='red', label='Clase 1')
axs[0].set_title('Con shuffle=True')
axs[0].legend()

# Subplot 2: Datos con shuffle=False
axs[1].scatter(X_not_shuffled[:50, 0], X_not_shuffled[:50, 1], c='blue', label='Clase 0')
axs[1].scatter(X_not_shuffled[50:, 0], X_not_shuffled[50:, 1], c='red', label='Clase 1')
axs[1].set_title('Con shuffle=False')
axs[1].legend()

# Mostrar listado de algunos datos generados con shuffle=True
print("Algunos datos generados con shuffle=True:")
for i, (x, y) in enumerate(zip(X_shuffled[:10], y_shuffled[:10])):
    print(f"Muestra {i+1}: Características: {x}, Etiqueta: {y}")

# Mostrar listado de algunos datos generados con shuffle=False
print("\nAlgunos datos generados con shuffle=False:")
for i, (x, y) in enumerate(zip(X_not_shuffled[:10], y_not_shuffled[:10])):
    print(f"Muestra {i+1}: Características: {x}, Etiqueta: {y}")

plt.show()


