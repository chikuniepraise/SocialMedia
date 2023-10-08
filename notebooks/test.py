import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.multioutput import MultiOutputRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

def predict_metrics(content_type, network):
    # Load the model
    model = joblib.load("models/model.joblib")

    # Create a DataFrame with the provided content_type and network
    new_post = pd.DataFrame({
        'content_type': [content_type],
        'network': [network],
    })

    # Make predictions using the loaded model
    predictions = model.predict(new_post)
    predictions=predictions[0]
    # Create a dictionary with the predicted values
    predic = {
        'engagements': int(predictions[0]),
        'impressions': int(predictions[1]),
        'reactions': int(predictions[2]),
        'likes': int(predictions[3]),
        'engaged_users': int(predictions[4]),
        'subscribers': int(predictions[5]),
        "shares": int(predictions[6])
    }
    
    return predic

def main():
    while True:
        print("Instructions:")
        print("Content Type Options: Photo: 1, Video: 2, Text: 3, Link: 4, Carousel: 5, Document: 6")
        print("Network Options: Twitter: 1, Facebook: 2, Instagram: 3, LinkedIn: 4")

        content_type = int(input("Enter Content Type: "))
        network = int(input("Enter Network: "))

        try:
            predictions = predict_metrics(content_type, network)
            print(predictions)
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
