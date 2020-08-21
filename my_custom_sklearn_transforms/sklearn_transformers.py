from sklearn.base import BaseEstimator, TransformerMixin


# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data.drop(labels=self.columns, axis='columns')

# Instanciando uma transformação DropColumns\n",
rm_columns = DropColumns(
    columns=["NOTA_GO"]  # Essa transformação recebe como parâmetro uma lista com os nomes das colunas indesejadas
)

# Aplicando a transformação ``DropColumns`` ao conjunto de dados base
rm_columns.fit(X=df_data_1)

# Reconstruindo um DataFrame Pandas com o resultado da transformação
df_data_2 = pd.DataFrame.from_records(
    data=rm_columns.transform(
        X=df_data_1
    )
)

# Instanciando uma transformação DropColumns
rm_columns = DropColumns(
    columns=["INGLES"]  # Essa transformação recebe como parâmetro uma lista com os nomes das colunas indesejadas
)

# Aplicando a transformação ``DropColumns`` ao conjunto de dados base
rm_columns.fit(X=df_data_2)

# Reconstruindo um DataFrame Pandas com o resultado da transformação
df_data_3 = pd.DataFrame.from_records(
    data=rm_columns.transform(
        X=df_data_2
    )
)