import pandas as pd
from mlaide import MLAideClient, ConnectionOptions, ModelStage
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline

# create connection
options = ConnectionOptions(
    server_url='http://localhost:9000/api/v1',
    api_key='YXV0aDB8NWY1M2FiNjc0MmUzNDUwMDZkYjJiOGQyOjB3wrdNeuKAoVfigLnigrbigrDigqDigKE='
)
mlaide_client = MLAideClient(project_key='usa-housing', options=options)

# read dummy data to predict some values
housing_data: pd.DataFrame = pd.read_csv('data/housing.csv')
X = housing_data[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
                  'Avg. Area Number of Bedrooms', 'Area Population']]
X = X.head(5)

# load pipeline (standard scaler) with a specific version
pipeline: Pipeline = mlaide_client.load_model('pipeline', 1)

# load model without a specific version (latest version will be used)
lin_reg: LinearRegression = mlaide_client.load_model('linear regression', stage=ModelStage.PRODUCTION)

# transform and predict
X = pipeline.transform(X)
y = lin_reg.predict(X)

print(y)
