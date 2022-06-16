import torch

class Perceptron:

    def __init__(self, learning_rate=0.01, epochs=480):
        """_summary_

        Args:
            learning_rate (float, optional): _description_. Defaults to 0.01.
            epochs (int, optional): _description_. Defaults to 480.

        Returns:
            _type_: _description_
        """
        return None

    def fit(self, X, y):
        """_summary_

        Args:
            X (_type_): _description_
            y (_type_): _description_

        Returns:
            _type_: _description_
        """
        return None

    def perceptronInput(self, X):
        """Calculates the value of the net input to be given to the perceptron for prediction

        Args:
            X: The feature matrix from the data

        Returns:
            int: The net input that the perceptron receives before it predicts the class
        """
        return None

    def predict(self, X):
        """_summary_

        Args:
            X (_type_): _description_

        Returns:
            _type_: _description_
        """
        return None

# def main():
#     print("Works")

# if __name__ == "__main__":
#     main()
