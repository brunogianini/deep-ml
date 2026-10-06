import numpy as np

def train(X_train, y_train, X_val, y_val):
    # Pesos e bias
    w = np.zeros(X_train.shape[1])
    b = 0.0

    learning_rate = 0.01
    epochs = 2000

    def sigmoid(z):
        z = np.clip(z, -500, 500)
        return 1 / (1 + np.exp(-z))

    # Gradient Descent
    for _ in range(epochs):
        # Forward pass
        z = X_train @ w + b
        predictions = sigmoid(z)

        # Gradientes
        error = predictions - y_train

        dw = (X_train.T @ error) / len(X_train)
        db = np.mean(error)

        # Atualização
        w -= learning_rate * dw
        b -= learning_rate * db

    def predict(X):
        probabilities = sigmoid(X @ w + b)
        return (probabilities >= 0.5).astype(int)

    return predict