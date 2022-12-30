
from sklearn.ensemble import GradientBoostingRegressor
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

df = pd.read_excel('./KDZD1.xlsx')
#print(df)
X = df.drop(columns='EXPRESS_DELIVERY_STATION')
y = df['EXPRESS_DELIVERY_STATION']
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2, random_state=10)
model = GradientBoostingRegressor(learning_rate = 0.01, max_depth=15,
                                  max_leaf_nodes=600, random_state=10,
                                  n_estimators=100, criterion="friedman_mse", loss='ls')
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

acc = model.score(X_test,y_test)
print('acc:')
print(acc)
print('r:')
print(r2_score(y_test,y_pred))
a = pd.DataFrame()
a['feature'] = X.columns
a['feature_importance'] = model.feature_importances_
a.sort_values(by='feature_importance',ascending=False)
print(a)