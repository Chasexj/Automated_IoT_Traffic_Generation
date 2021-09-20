import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
import sklearn
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn import datasets, model_selection, preprocessing, svm, metrics, decomposition
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import fbeta_score, make_scorer

from sklearn.model_selection import cross_validate
from sklearn.metrics import accuracy_score
from statistics import mean, variance

np.random.seed(0) # set random seed so everyone gets same results


class WeatherPipeline:

    def __init__(self):
        #self.ordinal = sklearn.preprocessing.OrdinalEncoder()
        #self.ordinal_features = ["RainToday"] # List of ordinal features
        # generate one hot encode object
        self.encode = preprocessing.OneHotEncoder(sparse=False) # we want a non-sparse matrix for concatenation
        self.onehot_features = ['src_ip','rts'] #List of the column names with nominal features that should be one-hot encoded

    def pprocess(self, dataf):
        # fill missing values
        for feature in dataf:
            if dataf[feature].dtype == "float64":
                dataf[feature].fillna(dataf[feature].mean(), inplace = True) 
            else:
                dataf[feature].fillna(dataf[feature].mode()[0], inplace = True)
        #ordinal encoding data
        #dataf[self.ordinal_features] = self.ordinal.fit_transform(dataf[self.ordinal_features])
        # one hot encoding data
        encoded = self.encode.fit_transform(dataf[self.onehot_features])
        encoded = pd.DataFrame(encoded) # the output of the encoding is a NumPy array, but we want it as a Pandas DataFrame
        dataf.drop(self.onehot_features, axis=1, inplace=True)
        dataf = pd.concat([dataf, encoded], axis=1)

    def fit(self):
        train_data = pd.read_csv("labeled.csv")
        y = train_data["label"]
        train_data.drop(["label"], axis=1, inplace=True)
        #pre processing data
        self.pprocess(train_data)
        
        micro_precision = []
        micro_recall = []
        micro_f1 = []
        macro_precision = []
        macro_recall = []
        macro_f1 = []
        weighted_precision = []
        weighted_recall = []
        weighted_f1 = []
        for i in range(50):
            print("Iteration "+ str(i))
            X_train, X_test, y_train, y_test = train_test_split(train_data, y, test_size = 0.25)

            # ###### grid search for best hyperparameters
            # #Cross-validation folds
            # k = 10
            # #Hyperparameters to tune:
            # params = {
            #    'criterion': ('gini', 'entropy'),
            #    'max_depth': (20, 40, 80),
            #    'min_samples_split': (2, 5, 10),
            #    'n_estimators': (200, 400, 800)
            # }
            # scoring = {'accuracy': make_scorer(accuracy_score),
            #    'precision': make_scorer(precision_score, average = 'micro'),
            #    'recall': make_scorer(recall_score, average = 'micro')}
            # #Initialize GridSearchCV object with decision tree classifier and hyperparameters
            # grid_tree = GridSearchCV(estimator=RandomForestClassifier(random_state=0),
            #                         param_grid=params,
            #                         cv=k,
            #                         return_train_score=True,
            #                         scoring=scoring,
            #                         refit='accuracy',
            #                         verbose=10) 
            # grid_tree.fit(X_train, y_train)
            # self.best_tree = grid_tree.best_estimator_
            # print(pd.Series(self.best_tree.feature_importances_, train_data.columns).sort_values(ascending=False))
            # print(self.best_tree.get_params())
            # #results:
            # #ipv4_id_5       0.012734
            # # tcp_opt_68      0.011163
            # # ipv4_id_6       0.010253
            # # tcp_opt_36      0.009777
            # # tcp_opt_70      0.009651
            # #                 ...   
            # # ipv4_opt_183    0.000000
            # # ipv4_opt_184    0.000000
            # # ipv4_opt_185    0.000000
            # # ipv4_opt_186    0.000000
            # # ipv4_opt_227    0.000000
            # # Length: 1120, dtype: float64
            # # {'bootstrap': True, 'ccp_alpha': 0.0, 'class_weight': None, 'criterion': 'entropy', 'max_depth': 40, 'max_features': 'auto', 'max_leaf_nodes': None, 'max_samples': None, 'min_impurity_decrease': 0.0, 'min_impurity_split': None, 'min_samples_leaf': 1, 'min_samples_split': 2, 'min_weight_fraction_leaf': 0.0, 'n_estimators': 800, 'n_jobs': None, 'oob_score': False, 'random_state': 0, 'verbose': 0, 'warm_start': False}
            # ###########




            ######## with pre set hyperparameters
            clf = RandomForestClassifier(bootstrap= True, ccp_alpha= 0.0, class_weight= None, criterion= 'entropy', max_depth= 40, max_features= 'auto', max_leaf_nodes= None, max_samples= None, min_impurity_decrease= 0.0, min_impurity_split= None, min_samples_leaf= 1, min_samples_split= 2, min_weight_fraction_leaf= 0.0, n_estimators= 800, n_jobs= None, oob_score= False, random_state= 0, verbose= 0, warm_start= False)
            self.best_tree = clf
            #cv = cross_validate(self.best_tree, X_train, y_train, cv=10)
            #print(cv['test_score'])
            #print(cv['test_score'].mean())
            #######
            
            # Make predictions for the test set
            self.best_tree.fit(X_train, y_train)
            y_pred_test = self.best_tree.predict(X_test)
            # View individual score
            print()
            print("Micro")
            
            micro_precision_score = precision_score(y_test, y_pred_test,average = "micro")
            micro_recall_score = recall_score(y_test, y_pred_test, average = "micro")
            micro_f1_score = f1_score(y_test, y_pred_test, average = "micro")
            print("precision score: "+str(micro_precision_score))
            print("recall score: "+str(micro_recall_score))
            print("f1 score: "+str(micro_f1_score))
            micro_precision.append(micro_precision_score)
            micro_recall.append(micro_recall_score)
            micro_f1.append(micro_f1_score)
            
            print()
            print("Macro")

            macro_precision_score = precision_score(y_test, y_pred_test,average = "macro")
            macro_recall_score = recall_score(y_test, y_pred_test, average = "macro")
            macro_f1_score = f1_score(y_test, y_pred_test, average = "macro")
            print("precision score: "+str(macro_precision_score))
            print("recall score: "+str(macro_recall_score))
            print("f1 score: "+str(macro_f1_score))
            macro_precision.append(macro_precision_score)
            macro_recall.append(macro_recall_score)
            macro_f1.append(macro_f1_score)
            
            print()
            print("Weighted")

            weighted_precision_score = precision_score(y_test, y_pred_test,average = "weighted")
            weighted_recall_score = recall_score(y_test, y_pred_test, average = "weighted")
            weighted_f1_score = f1_score(y_test, y_pred_test, average = "weighted")
            print("precision score: "+str(weighted_precision_score))
            print("recall score: "+str(weighted_recall_score))
            print("f1 score: "+str(weighted_f1_score))
            weighted_precision.append(weighted_precision_score)
            weighted_recall.append(weighted_recall_score)
            weighted_f1.append(weighted_f1_score)


        # View average score
        print()
        print("Micro Averaging")
        
        print("mean precision score: "+str(mean(micro_precision)))
        print("mean recall score: "+str(mean(micro_recall)))
        print("mean f1 score: "+str(mean(micro_f1)))
        print("var precision score: "+str(variance(micro_precision)))
        print("var recall score: "+str(variance(micro_recall)))
        print("var f1 score: "+str(variance(micro_f1)))

        
        print()
        print("Macro Averaging")

        print("mean precision score: "+str(mean(macro_precision)))
        print("mean recall score: "+str(mean(macro_recall)))
        print("mean f1 score: "+str(mean(macro_f1)))
        print("var precision score: "+str(variance(macro_precision)))
        print("var recall score: "+str(variance(macro_recall)))
        print("var f1 score: "+str(variance(macro_f1)))
        
        print()
        print("Weighted Averaging")

        print("mean precision score: "+str(mean(weighted_precision)))
        print("mean recall score: "+str(mean(weighted_recall)))
        print("mean f1 score: "+str(mean(weighted_f1)))
        print("var precision score: "+str(variance(weighted_precision)))
        print("var recall score: "+str(variance(weighted_recall)))
        print("var f1 score: "+str(variance(weighted_f1)))
        

    def predict(self):
        test_data = pd.read_csv("Lab3_test.csv")
        test_data.drop('Unnamed: 0', axis=1, inplace=True)
        #pre processing data
        self.pprocess(test_data)
        predictions = self.best_tree.predict(test_data)
        #print(predictions)
        return predictions
                

obj = WeatherPipeline()
obj.fit()
#obj.predict()
