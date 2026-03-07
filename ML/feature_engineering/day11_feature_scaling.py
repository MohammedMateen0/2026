from sklearn.preprocessing import StandardScaler, MinMaxScaler
import numpy as np


class FeatureScaling:

    def standard_scaling(self, X_train, X_test):
        """
        Applies StandardScaler while preventing data leakage.
        """
        scaler = StandardScaler()

        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)

        return X_train_scaled, X_test_scaled

    def minmax_scaling(self, X_train, X_test):
        """
        Applies MinMaxScaler (0–1 normalization).
        """
        scaler = MinMaxScaler()

        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)

        return X_train_scaled, X_test_scaled


if __name__ == "__main__":

    # Example dataset
    X_train = np.array([[25, 50000],
                        [40, 120000],
                        [35, 80000]])

    X_test = np.array([[30, 60000],
                       [50, 150000]])

    scaler = FeatureScaling()

    train_scaled, test_scaled = scaler.standard_scaling(X_train, X_test)

    print("Scaled Training Data:\n", train_scaled)
    print("Scaled Test Data:\n", test_scaled)