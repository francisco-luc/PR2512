import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import seaborn as sns
import plotly.graph_objects as go

st.set_page_config(page_title="MUSIC DATASET ANALYSIS", layout="wide")

def load_data(uploaded_file):
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            df['duration_min'] = df['duration_in min/ms'] / 60000
            df['decade'] = (df['release_year'] // 10) * 10
            df['decade_label'] = df['decade'].astype(str) + 's'

            def categorize_era(year):
                if year < 1980:
                    return 'Classic (1960-1979)'
                elif year < 2000:
                    return 'Modern (1980-1999)'
                else:
                    return 'Contemporary (2000+)'
            df['era'] = df['release_year'].apply(categorize_era)

            df['key'] = df['key'].astype('category')
            df['mode'] = df['mode'].astype('category')
            df['time_signature'] = df['time_signature'].astype('category')

            for col in df.select_dtypes(include=[np.number]).columns:
                df[col].fillna(df[col].median(), inplace=True)
            for col in df.select_dtypes(include=['object']).columns:
                df[col].fillna(df[col].mode()[0], inplace=True)

            return df
        except Exception as e:
            st.error(f"Error reading CSV file: {e}")
            return None
    else:
        return None

def plot_stats_by_decade(df):
    st.header("MEAN FEATURES BY DECADE (NORMALIZED)")
    numeric_features = df.select_dtypes(include=[np.number]).columns.tolist()
    selected_features = st.multiselect("Select features for mean features by decade", numeric_features, default=numeric_features)

    if len(selected_features) < 1:
        st.warning("Select at least one feature to plot.")
        return

    decade_means = df.groupby('decade')[selected_features].mean()
    norm_means = (decade_means - decade_means.min()) / (decade_means.max() - decade_means.min())

    fig, ax = plt.subplots(figsize=(12, 6))
    norm_means.plot(kind='bar', ax=ax)
    ax.set_title("Normalized mean Features by decade")
    ax.set_xlabel("Decade")
    ax.set_ylabel("Normalized mean (0-1)")
    ax.legend(title="Features")
    plt.xticks(rotation=45)
    st.pyplot(fig)

    st.subheader("RADAR CHART BY DECADE (NORMALIZED)")
    radar_features = st.multiselect("Select features for radar chart", selected_features, default=selected_features)

    if len(radar_features) < 2:
        st.info("Select at least two features for radar chart.")
        return

    radar_means = norm_means[radar_features]
    decades = radar_means.index.astype(str).tolist()
    categories = radar_features

    fig_radar = go.Figure()
    for decade in decades:
        values = radar_means.loc[int(decade)].tolist()
        values += values[:1]
        fig_radar.add_trace(go.Scatterpolar(
            r=values,
            theta=categories + [categories[0]],
            fill='toself',
            name=decade + 's'
        ))

    fig_radar.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0,1])),
        showlegend=True,
        height=600
    )
    st.plotly_chart(fig_radar, use_container_width=True)

def scatter_plot(df):
    st.header("SCATTER PLOT")
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    if len(numeric_cols) < 2:
        st.warning("Not enough numeric columns for scatter plot.")
        return

    x_axis = st.selectbox("Select X-axis", numeric_cols, index=0)
    y_axis = st.selectbox("Select Y-axis", numeric_cols, index=1)

    fig, ax = plt.subplots(figsize=(8, 6))
    sns.scatterplot(data=df, x=x_axis, y=y_axis, hue='era', ax=ax)
    ax.set_title(f"Scatter Plot: {x_axis} vs {y_axis}")
    st.pyplot(fig)

def correlation_heatmap(df):
    st.header("CORRELATION HEATMAP")
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    corr = df[numeric_cols].corr()

    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
    ax.set_title("Correlation Heatmap")
    st.pyplot(fig)

def interactive_clustering(df):
    st.header("KMEANS CLUSTERING")
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    if len(numeric_cols) < 2:
        st.warning("Not enough numeric columns for clustering.")
        return

    selected_features = st.multiselect("Select features for clustering", numeric_cols, default=numeric_cols[:3])
    if len(selected_features) < 2:
        st.info("Select at least two features for clustering.")
        return

    k = st.slider("Number of clusters (k)", 2, 10, 3)

    X = df[selected_features].copy()
    X = (X - X.mean()) / X.std()

    kmeans = KMeans(n_clusters=k, random_state=42)
    clusters = kmeans.fit_predict(X)
    df['cluster'] = clusters.astype(str)

    pca = PCA(n_components=2)
    components = pca.fit_transform(X)

    fig, ax = plt.subplots(figsize=(8, 6))
    scatter = ax.scatter(components[:, 0], components[:, 1], c=clusters, cmap='tab10', alpha=0.7)
    legend1 = ax.legend(*scatter.legend_elements(), title="Clusters")
    ax.add_artist(legend1)
    ax.set_title(f"KMeans Clustering (k={k}) PCA Projection")
    ax.set_xlabel("PC1")
    ax.set_ylabel("PC2")
    st.pyplot(fig)

st.title(" MUSIC DATA ANALYSIS")

uploaded_file = st.file_uploader("Upload CSV", type=['csv'])

if uploaded_file is not None:
    df = load_data(uploaded_file)
    if df is not None:
        st.write("### Data Preview")
        st.dataframe(df.head())

        st.sidebar.header("Filters")

        year_min, year_max = int(df['release_year'].min()), int(df['release_year'].max())
        selected_years = st.sidebar.slider("Release Year", year_min, year_max, (year_min, year_max))

        era_options = df['era'].unique()
        selected_eras = st.sidebar.multiselect("Era", options=era_options, default=era_options)

        key_options = df['key'].cat.categories if 'key' in df.columns else []
        selected_keys = st.sidebar.multiselect("Musical Key", options=key_options, default=key_options)

        popularity_min, popularity_max = None, None
        if 'popularity' in df.columns:
            popularity_min, popularity_max = int(df['popularity'].min()), int(df['popularity'].max())
            selected_popularity = st.sidebar.slider("Popularity", popularity_min, popularity_max, (popularity_min, popularity_max))
        else:
            selected_popularity = None

        filtered_df = df[
            (df['release_year'] >= selected_years[0]) &
            (df['release_year'] <= selected_years[1]) &
            (df['era'].isin(selected_eras)) &
            (df['key'].isin(selected_keys))
        ]

        if selected_popularity:
            filtered_df = filtered_df[
                (filtered_df['popularity'] >= selected_popularity[0]) &
                (filtered_df['popularity'] <= selected_popularity[1])
            ]

        st.write(f"### Filtered Data: {filtered_df.shape[0]} rows")

        plot_stats_by_decade(filtered_df)
        scatter_plot(filtered_df)
        correlation_heatmap(filtered_df)
        interactive_clustering(filtered_df)

    else:
        st.warning("Error loading CSV")
else:
    st.info("Upload CSV for start")
