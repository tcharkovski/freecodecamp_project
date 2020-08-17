import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date')

# Clean data
df = df[df['value']> 20000]
df.index = pd.to_datetime(df.index)

def draw_line_plot():
    # Draw line plot
    
    df.plot();
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019');
    plt.xlabel('date');
    plt.ylabel('page views');
    plt.xticks(rotation = 90);




    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = None

    # Draw bar plot

    sns.barplot(x = df.index.year, y= df.value, hue=df.index.month, ci= None)
    plt.ylabel('Average Page View')
    plt.xlabel('Year')
    plt.legend(('January','February',  'March','April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'), loc= 'upper left');




    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)

fig, ax = plt.subplots(1, 2, figsize = (14, 4))

sns.boxplot(x = df.year, y = df.values.ravel(), ax = ax[0])
ax[0].set_xlabel('Year')
ax[0].set_ylabel('Page Views')
ax[0].set_title('Year-wise Box Plot (Trend)')
sns.boxplot(x = df.month, y = df.values.ravel(),ax= ax[1])
ax[1].set_xlabel('Months')
ax[1].set_ylabel('Page Views')
ax[1].set_title("Month-wise Box Plot (Seasonality)")
ax[1].set_xticklabels(('Jan','Feb',  'Mar','Apr', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec'), rotation = 90);




    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
