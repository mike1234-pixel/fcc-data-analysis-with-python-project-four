import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.) 
df = pd.read_csv(
    'fcc-forum-pageviews.csv',
    parse_dates=['date']).set_index('date')

# Clean data - filter out the top 2.5% and bottom 2.5% of the dataset 
df = df[(df['value'] >= df['value'].quantile(0.025))
    & (df['value'] <= df['value'].quantile(0.975))]

def draw_line_plot():
    # Draw line plot ✓
    line_plot = plt.figure(figsize=(30,10))
    plt.plot(
      df.index,
      df.value, 
    )
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019', fontsize='xx-large')
    plt.ylabel('Page Views', fontsize='xx-large')
    plt.xlabel('Date', fontsize='xx-large')

    fig = line_plot

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    # group months by year
    # group daily page views by month
    # find the average of daily page views per month
    bar_df = df.groupby(by=[df.index.year, df.index.month]).mean()
    # rename multiindex cols
        # rename multiindex colsvalues col
    bar_df.index.set_names(["Year", "Month"], inplace=True)
    bar_df.columns = ['Average Daily Page Views']
    bar_df = bar_df.unstack()

    # draw multiindex bar plot
    fig = bar_df.plot(kind='bar', legend=True, figsize=(10,7)).figure
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.legend(fontsize = 10, labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])

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
    box_df = df.copy()
    box_df.reset_index(inplace=True)
    box_df['year'] = [d.year for d in box_df.date]
    box_df['month'] = [d.strftime('%b') for d in box_df.date]

    fig, axes = plt.subplots(nrows=1, ncols=2, figsize = (10,5))

    Months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    axes[0] = sns.boxplot(x=df_box["year"], y=df_box["value"], ax = axes[0])
    axes[1] = sns.boxplot(x=df_box["month"], y=df_box["value"], ax = axes[1], order=Months)

    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
