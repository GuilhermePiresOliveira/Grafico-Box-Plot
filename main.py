# Imports
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np

# Massa de dados
data = [np.random.normal(0, std, 100) for std in range(1, 4)]

# Define o tamanho.
plt.figure(figsize=(4,4))

# Configurações do gráfico.
sns.boxplot(data=data)
plt.title('Box Plot')
plt.xlabel('Categoria')
plt.ylabel('Valores')
plt.show()
