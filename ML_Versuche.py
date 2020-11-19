from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report,confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB


def ML_try(df, test_size, state, target, X):

    test = df.copy()

    Y = test[target]
    X = test[X]
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=test_size, random_state=state)

    Classifier = [RandomForestClassifier(), LogisticRegression(), LinearSVC(), KNeighborsClassifier(n_neighbors=5),
                  GaussianNB()]
    Predictions = []

    for classifier in Classifier:
        cl = classifier
        cl.fit(X_train, y_train)
        Predictions.append(cl.predict(X_test))
        print(cl.score(X_test, y_test))
        print(classification_report(y_test, cl.predict(X_test)))
        print(confusion_matrix(y_test, cl.predict(X_test)))

    Vorhersage = test.loc[y_test.index]
    Vorhersage["RF"]= Predictions[0]
    Vorhersage["LR"]= Predictions[1]
    Vorhersage["SVC"]= Predictions[2]
    Vorhersage["KNN"]= Predictions[3]
    Vorhersage["GN"]= Predictions[4]

    Columns = ["RF", "LR", "SVC", "KNN", "GN"]

    Gewinne = []
    for column in Columns:
        Gewinn = Vorhersage.loc[Vorhersage["FTR"] == Vorhersage[column]]
        Gewinn.loc[Gewinn["FTR"] == "D", "Gewinn_{}".format(column)] = Gewinn["B365D"]
        Gewinn.loc[Gewinn["FTR"] == "A", "Gewinn_{}".format(column)] = Gewinn["B365A"]
        Gewinn.loc[Gewinn["FTR"] == "H", "Gewinn_{}".format(column)] = Gewinn["B365H"]
        Gewinne.append(Gewinn["Gewinn_{}".format(column)].sum() - len(Vorhersage))

    dict_wins = dict(zip(Columns, Gewinne))

    return dict_wins

