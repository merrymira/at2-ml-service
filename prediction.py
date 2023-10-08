def sales_prediction(date_obj, item_id, store_id):
    import pickle
    import pandas as pd
    import numpy as np

    # Load data (deserialize)
    with open('models/itemID.pickle', 'rb') as handle:
        itemID = pickle.load(handle)

    with open('models/storeID.pickle', 'rb') as handle:
        storeID = pickle.load(handle)

    # Load the trained model. (Pickle file)
    model = pickle.load(open('models/xgBoost.pkl', 'rb'))

    # Load CSV files
    calevent_df = pd.read_csv('data/calendar_events.csv')

    # Check Holiday
    is_holiday = 1 if date_obj in calevent_df['date'].values else 0


    # Convert date string to datetime and create input dataframe for a prediction
    from datetime import datetime
    date_obj = datetime.strptime(date_obj, '%Y-%m-%d')

    # Create a list of lists where each inner list represents a row of data
    data = [[date_obj.year, date_obj.month, date_obj.day,
             storeID[store_id], itemID[item_id], is_holiday]]

    # Create a DataFrame from the data list
    input_df = pd.DataFrame(data, columns=['year', 'month', 'day',
                                           'store_id_encoded', 'item_id_encoded',
                                           'is_holiday'])

    # Sale Prediction
    y_pred = model.predict(input_df)

    # Save y_pred to a file
    np.save('data/y_pred.npy', y_pred)