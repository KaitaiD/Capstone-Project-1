{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import featuretools as ft\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "from featuretools.primitives import (Day, Hour, Max, Mean, Min, Minute, Month,\n",
    "                                     Skew, Std, Week, Weekday, Weekend)\n",
    "from sklearn.cluster import KMeans\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.preprocessing import Imputer\n",
    "\n",
    "# set global random seed\n",
    "np.random.seed(40)\n",
    "\n",
    "\n",
    "####################\n",
    "# Case Study Utils #\n",
    "####################\n",
    "\n",
    "def preview(df, n=5):\n",
    "    \"\"\"return n rows that have fewest number of nulls\"\"\"\n",
    "    order = df.isnull().sum(axis=1).sort_values(kind='mergesort').head(n).index\n",
    "    return df.loc[order]\n",
    "\n",
    "\n",
    "def feature_importances(model, feature_names, n=10):\n",
    "    importances = model.feature_importances_\n",
    "    zipped = sorted(zip(feature_names, importances), key=lambda x: -x[1])\n",
    "    for i, f in enumerate(zipped[:n]):\n",
    "        print(\"%d: Feature: %s, %.3f\" % (i + 1, f[0], f[1]))\n",
    "\n",
    "\n",
    "def get_train_test_fm(feature_matrix, percentage):\n",
    "    nrows = feature_matrix.shape[0]\n",
    "    head = int(nrows * percentage)\n",
    "    tail = nrows - head\n",
    "    X_train = feature_matrix.head(head)\n",
    "    y_train = X_train['trip_duration']\n",
    "    X_train = X_train.drop(['trip_duration'], axis=1)\n",
    "    imp = Imputer()\n",
    "    X_train = imp.fit_transform(X_train)\n",
    "    X_test = feature_matrix.tail(tail)\n",
    "    y_test = X_test['trip_duration']\n",
    "    X_test = X_test.drop(['trip_duration'], axis=1)\n",
    "    X_test = imp.transform(X_test)\n",
    "\n",
    "    return (X_train, y_train, X_test, y_test)\n",
    "\n",
    "\n",
    "##################\n",
    "# Case Study 6.1 #\n",
    "##################\n",
    "\n",
    "def column_string(n):\n",
    "    string = \"\"\n",
    "    while n > 0:\n",
    "        n, remainder = divmod(n - 1, 26)\n",
    "        string = chr(65 + remainder) + string\n",
    "    return string\n",
    "\n",
    "\n",
    "def load_nyc_taxi_data():\n",
    "    trips = pd.read_pickle('trips.pkl')\n",
    "    trips[\"payment_type\"] = trips[\"payment_type\"].apply(str)\n",
    "    trips = trips.dropna(axis=0, how='any', subset=['trip_duration'])\n",
    "\n",
    "    pickup_neighborhoods = pd.read_csv(\n",
    "        \"pickup_neighborhoods.csv\", encoding='utf-8')\n",
    "    dropoff_neighborhoods = pd.read_csv(\n",
    "        \"dropoff_neighborhoods.csv\", encoding='utf-8')\n",
    "\n",
    "    return trips, pickup_neighborhoods, dropoff_neighborhoods\n",
    "\n",
    "\n",
    "def compute_features(features, cutoff_time):\n",
    "    # shuffle so we don't see encoded features in the front or backs\n",
    "\n",
    "    np.random.shuffle(features)\n",
    "    feature_matrix = ft.calculate_feature_matrix(features,\n",
    "                                                 cutoff_time=cutoff_time,\n",
    "                                                 approximate='36d',\n",
    "                                                 verbose=True)\n",
    "    print(\"Finishing computing...\")\n",
    "    feature_matrix, features = ft.encode_features(feature_matrix, features,\n",
    "                                                  to_encode=[\n",
    "                                                      \"pickup_neighborhood\",\n",
    "                                                      \"dropoff_neighborhood\"],\n",
    "                                                  include_unknown=False)\n",
    "    return feature_matrix\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
