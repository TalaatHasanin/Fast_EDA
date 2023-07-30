import time
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def get_data_head(df, columns):
    if not columns:
        sub_df = df
    else:
        sub_df = df[columns].copy()
    head = sub_df.head()
    head = pd.DataFrame(head)
    return head


def get_data_tail(df, columns):
    if not columns:
        sub_df = df
    else:
        sub_df = df[columns].copy()
    tail = sub_df.tail()
    tail = pd.DataFrame(tail)
    return tail


def get_data_unique(df, columns):
    if not columns:
        sub_df = df
    else:
        sub_df = df[columns].copy()
    unique = sub_df.nunique()
    unique_df = pd.DataFrame(unique)
    unique_df.columns = ['Unique']  # Replace the label '0' with 'count'
    unique_df.index.name = 'Column'  # Add a label for the column that shows the names of dataframe columns
    return unique_df


def get_data_null(df, columns):
    if not columns:
        sub_df = df
    else:
        sub_df = df[columns].copy()

    null_count = sub_df.isnull().sum()
    total_count = len(sub_df)

    null_percentage = (null_count / total_count) * 100

    null_df = pd.DataFrame({'Null': null_count, 'Null Percentage': null_percentage})
    null_df.index.name = 'Column'

    return null_df


def get_data_summary(df, columns):
    if not columns:
        sub_df = df
    else:
        sub_df = df[columns].copy()
    summary = sub_df.describe().T
    summary = pd.DataFrame(summary)
    return summary


def get_data_info(df, column):
    if not column:
        sub_df = df
    else:
        sub_df = df[column].copy()
    # Get the data types from the DataFrame
    data_types = sub_df.dtypes.reset_index()
    data_types.columns = ['Column', 'Data Type']

    # Get the non-null count for each column
    non_null_count = sub_df.notnull().sum().reset_index()
    non_null_count.columns = ['Column', 'Non-Null Count']

    # Merge the data types and non-null count DataFrames
    columns_info_df = data_types.merge(non_null_count, on='Column')

    # Get the index as a separate column
    columns_info_df.reset_index(drop=True, inplace=True)

    return columns_info_df


def get_data_corr(df, columns):
    if not columns:
        sub_df = df
    else:
        sub_df = df[columns].copy()
    sub_df = sub_df.select_dtypes(['float', 'int'])
    corr = sub_df.corr()
    corr = pd.DataFrame(corr)
    return corr


def get_numeric(df, columns):
    if not columns:
        sub_df = df
    else:
        sub_df = df[columns].copy()
    num = list(sub_df.select_dtypes(['float', 'int']).columns)
    return num


def get_non_numeric(df, columns):
    if not columns:
        sub_df = df
    else:
        sub_df = df[columns].copy()
    non_num = list(sub_df.select_dtypes(['object']).columns)
    return non_num


def get_scatter(df, columns, x, y):
    if not columns:
        sub_df = df
    else:
        sub_df = df[columns].copy()
    sns.relplot(x=x, y=y, data=sub_df)
    st.pyplot()


def get_hist(df, columns, box, slider):
    if not columns:
        sub_df = df
    else:
        sub_df = df[columns].copy()
    sns.distplot(sub_df[box], bins=slider)
    st.pyplot()


def get_line(df, columns, x, y):
    if not columns:
        sub_df = df
    else:
        sub_df = df[columns].copy()
    sns.lineplot(x=x, y=y, data=sub_df)
    st.pyplot()


def get_box(df, columns, x, y):
    if not columns:
        sub_df = df
    else:
        sub_df = df[columns].copy()
    sns.boxplot(x=x, y=y, data=sub_df)
    st.pyplot()


def univariate(df, columns, num_cols):
    if not columns:
        data = df
    else:
        data = df[columns].copy()
    for col in num_cols:
        print(col)
        print('Skew :', round(data[col].skew(), 2))
        plt.figure(figsize=(15, 4))
        plt.subplot(1, 2, 1)
        data[col].hist(grid=False)
        plt.ylabel('count')
        plt.subplot(1, 2, 2)
        sns.boxplot(x=data[col])
        st.pyplot()


def main():
    # configuration
    st.set_page_config(page_title="Fast Exploratory Data Analysis",
                       page_icon=":bar_chart:",
                       layout='wide')

    st.set_option('deprecation.showPyplotGlobalUse', False)

    # page title
    st.title("Exploratory Data Analysis for your Data :bar_chart:")

    # global variables
    global selected_columns, numeric, non_numeric
    df = None
    box1 = None
    box2 = None
    box3 = None
    box4 = None
    box5 = None
    box6 = None
    box7 = None

    # sidebar
    with st.sidebar:

        # sidebar title
        st.title("Data Elements")
        # sidebar header
        st.subheader("Upload your csv file")
        # upload .csv files
        file = st.file_uploader("Upload your files",
                                accept_multiple_files=False,
                                type=['csv'])
        if file is not None:
            # convert to pandas dataframe
            df = pd.read_csv(file, encoding='utf-8', encoding_errors='ignore')

            columns = df.columns

            st.subheader("Selected columns")
            selected_columns = st.multiselect("Select columns to include in process", options=columns)

            numeric = get_numeric(df, selected_columns)
            non_numeric = get_non_numeric(df, selected_columns)

            st.subheader("Scatter plot")
            box1 = st.selectbox('X axis', options=numeric, key="box1")
            box2 = st.selectbox('Y axis', options=numeric, key="box2")

            st.subheader("Histogram")
            box3 = st.selectbox(label="Column", options=numeric, key="box3")
            histogram_slider = st.slider(label="Number of Bins", min_value=5, max_value=100, value=15)

            st.subheader("Line plot")
            box4 = st.selectbox('X axis', options=numeric, key="box4")
            box5 = st.selectbox('Y axis', options=numeric, key="box5")

            st.subheader("Box plot")
            box6 = st.selectbox('X axis', options=numeric, key="box6")
            box7 = st.selectbox('Y axis', options=numeric, key="box7")

    # 'Process' button to start processing
    st.write("\n")
    st.markdown("**:red[NOTE]** : you have to click on 'Process' each time you change data elements, so be sure about "
                "your settings before processing.")

    process = st.button("Process")

    if process:
        if df is None:
            with st.sidebar:
                st.error("Please select a file", icon='⚠️')
        else:
            with st.spinner("Processing..."):
                time.sleep(1)

            st.write("#### Head")
            head = get_data_head(df, selected_columns)
            st.dataframe(head)

            st.write("#### Tail")
            tail = get_data_tail(df, selected_columns)
            st.dataframe(tail)

            col1, col2, col3 = st.columns(3, gap='large')
            col1.write("#### Info")
            info = get_data_info(df, selected_columns)
            col1.dataframe(info)

            col2.write("#### Unique Values")
            unique = get_data_unique(df, selected_columns)
            col2.dataframe(unique.style.highlight_max(axis=0))

            col3.write("#### Null Values")
            null = get_data_null(df, selected_columns)
            col3.dataframe(null)

            st.write("#### Summary Statistics")
            summary = get_data_summary(df, selected_columns)
            st.dataframe(summary)

            st.write("#### Correlation")
            corr = get_data_corr(df, selected_columns)
            st.dataframe(corr.style.highlight_max(axis=0))

            st.write("#### Correlation Heatmap")
            corr_fig = plt.figure(figsize=(10, 4))
            sns.heatmap(corr, annot=True, vmin=-1, vmax=1)
            st.pyplot(corr_fig)

            st.write("#### Univariate Analysis")
            univariate(df, selected_columns, numeric)

            st.write("#### Scatter plot")
            if box1 and box2 is None:
                st.write("Please select X and Y")
            else:
                get_scatter(df, selected_columns, box1, box2)

            st.write("#### Histogram")
            if box3 is None:
                st.write("Please select a column")
            else:
                get_hist(df, selected_columns, box3, histogram_slider)

            st.write("#### Line plot")
            if box4 and box5 is None:
                st.write("Please select X and Y")
            else:
                get_line(df, selected_columns, box4, box5)

            st.write("#### Box plot")
            if box6 and box7 is None:
                st.write("Please select X and Y")
            else:
                get_box(df, selected_columns, box6, box7)


if __name__ == '__main__':
    main()
