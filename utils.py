import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_mood_data():
    return pd.read_csv("mood_log.csv", parse_dates=["timestamp"])

def export_csv():
    return "mood_log.csv"

def plot_mood_trend():
    df = load_mood_data()
    df['day'] = df['timestamp'].dt.date
    mood_counts = df.groupby('day').size().reset_index(name='mood_entries')

    plt.figure(figsize=(10,5))
    sns.lineplot(x='day', y='mood_entries', data=mood_counts, marker='o')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("plot.png")