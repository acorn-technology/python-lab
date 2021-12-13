# Data processing and visualization

In this lab, we will showcase some data mangling and visualization.

Python is heavily used in the ML/AI space and has some excellent tooling for exploratory data analysis. The widely used cornerstones are [Numpy](https://numpy.org/), [Matplotlib](https://matplotlib.org/) and [Pandas](https://pandas.pydata.org/). All three are available through `pip`.

Note: These libraries expose quite a bit of top-level names. To keep your working namespace clean, it is conventional to import these modules with shorthand names like this:

```
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
```

## 1 Processing

We use Pandas to load and perform some data cleaning.

### 1.1 Loading

Start by reading the `electricity.csv` file with the `pd.read_csv` function. This creates a DataFrame object with lots of useful functions.

Explore the data for a bit, try the following:

- View a summary of the dataframe with `print(electricity_frame)`
- View the start/end of the frame with `electricity_frame.head(n)` or `tail(n)` (Remember to print the result)
- View the column names with `electricity_frame.columns`
- View details about a column by indexing the dataframe with the columns name: `electricity_frame['col_name']`

Answer the following questions:

- What are the names and datatypes of our columns?
- How many unique values exist in the third column? What are the values?
- What are the maximum, minimum and mean values of the second column?

### 1.2 Cleaning

As you probably have noticed by now, _someone_ shuffled all the rows! Let's fix that!

Use the `pd.to_datetime` function to parse the datetime column and replace the old column
```
df['col_name'] = pd.to_datetime(df['col_name'])
```
Sort the data by the new datetime column
```
df.sort_values(by='col_name', axis=0, inplace=True)
```
_Note: Many member functions of DataFrame objects avoid modifying self and default to returning a new DataFrame. The_ `inplace` _flag is available on many functions to explicitly modify self._

The Price column doesn't really make sense, as the values in it are from different areas shuffled together.

We want to be able to compare the electricity prices by area. To do this, we need to conditionally extract the correct rows.

```
new_frame = electricity_frame[electricity_frame['col_name'] == 'value']
```

This creates a new dataframe. Do this for each area and rename the respective price columns to unique names. If you want you can drop the area column now, since it's no longer useful to us.

We are almost ready to merge the Dataframes into one again. First, we want to set the index of each Dataframe to the datetime column with the `set_index` method. This will allow us to easily merge the Dataframes:

```
joined = pd.concat([df1, df2, df3, df4], axis=1)
```

We now have a wellshaped Dataframe with the following structure:

Tidsperiod | Pris Norra | Pris Norra Mellan | Pris Södra Mellan | Pris Södra
--- | --- | --- | --- | ---
2021-11-29 00:00:00 | 123.45 | 234.56 | 345.67 | 567.89
2021-11-29 01:00:00 | 123.45 | 234.56 | 345.67 | 567.89
... | ... | ... | ... | ... 

We can easily make a simple line plot of the data!

```
electricity_frame.plot()
plt.show()
```

## 2 Visualizing

### 2.1 Basic Plotting

The [Matplotlib example page](https://matplotlib.org/stable/plot_types/index.html) has plenty of example functionality. Copy one of the examples and spend a few minutes modifying the looks and explore the syntax.

### 2.2 Plotting the price

Pick an idea for visualizing our price data:

- (Easy) Show the data in a single plot or multiple subplots
- Plot the distribution of the prices in histograms, can we draw any conclusions?
- A color coded Scatter plot might show interesting correlations
- Any of your own ideas

## 3 Bonus: Jupyter Notebooks

A common tool used in exploratory data analysis is [Jupyter Notebooks](https://jupyter.org/). It's a cell-based interactive Python interpreter which allows you to quickly try out different calculations without rerunning your entire program.

## 4 Bonus: What about numpy?

Pandas is built on Numpy, which offers a great Mathematics library for (surprisingly) high-performance calculations. It has seamless integrations to Pandas, Matplotlib, SkLearn and many other libraries. 