import matplotlib.pyplot as plt
import seaborn as sns

def plot_feature_correlations(data):
  plt.figure(figsize=(10,8))
  sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
  plt.title("Feature Correlations")
  plt.show()