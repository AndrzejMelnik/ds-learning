import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, roc_curve, auc


class HoneyVisualizer:
    @staticmethod
    def plot_diagnostics(y_test, y_pred, y_proba, feature_names, model):
        plt.figure(figsize=(15, 5))

        # 1. Macierz pomyłek
        plt.subplot(1, 3, 1)
        sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d', cmap='YlGnBu')
        plt.title("Macierz Pomyłek")

        # 2. Krzywa ROC
        plt.subplot(1, 3, 2)
        fpr, tpr, _ = roc_curve(y_test, y_proba)
        plt.plot(fpr, tpr, label=f"AUC: {auc(fpr, tpr):.2f}")
        plt.plot([2], 'r--')
        plt.legend()
        plt.title("Krzywa ROC")

        # 3. ROZWIĄZANIE BŁĘDU: Spłaszczenie model.coef
        plt.subplot(1, 3, 3)
        sns.barplot(x=model.coef_.flatten(), y=feature_names)
        plt.title("Wpływ parametrów na czystość")

        plt.tight_layout()
        plt.savefig("reports/figures/diagnostic_plots.png")
        plt.show()