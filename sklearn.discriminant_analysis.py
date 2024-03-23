from sklearn.datasets import load_iris
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

# Cargar el conjunto de datos Iris
iris = load_iris()
X = iris.data
y = iris.target

# Utilizar solo la primera característica para simplificar el ejemplo
X_simple = X[:, 0].reshape(-1, 1)

# Inicializar y ajustar el modelo LDA
lda = LinearDiscriminantAnalysis()
lda.fit(X_simple, y)

# Hacer una predicción para un nuevo valor de la característica
nueva_caracteristica = 5.0
prediccion = lda.predict([[nueva_caracteristica]])
print("Predicción para la nueva característica:", prediccion)
