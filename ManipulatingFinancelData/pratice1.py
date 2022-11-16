import pandas as pd
import matplotlib.pyplot as plt

def test_run():
    df = pd.read_csv("../data/Stocks/AAPL_data.csv")
    print(df['Close'])
    df["Close"].plot()
    plt.show()

if __name__ == "__main__":
    test_run()