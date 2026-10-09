# ============================================================
# FIFTH AI - DAY 5 FUNDAMENTAL ASSIGNMENT
# Name: PRAJWAL MRITHYUNJAY HULAMANI
#
# Project: Subscriber Analytics Dashboard
# File: subscriber_analytics_dashboard.py
# ============================================================


# ============================================================
# IMPORTS
# ============================================================

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
import plotly.express as px

import matplotlib
matplotlib.use("Agg")


# ============================================================
# STREAMLIT PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Subscriber Intelligence Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM DASHBOARD STYLING
# ============================================================

st.markdown(
    """
    <style>

    /* --------------------------------------------------------
       THEME NOTE

       Streamlit sets CSS "color-scheme" on the app container
       from the active theme, so light-dark(light, dark) below
       follows the Light / Dark switch instantly.

       The plain declaration above each light-dark() line is the
       fallback for browsers that lack light-dark() support.
    -------------------------------------------------------- */


    /* --------------------------------------------------------
       MAIN APPLICATION
    -------------------------------------------------------- */

    .stApp {
        background-color: #f6f8fc;

        background-color: light-dark(
            #f6f8fc,
            #0e1117
        );
    }

    .block-container {
        padding-top: 2.2rem;
        padding-bottom: 3rem;
        max-width: 1500px;
    }


    /* --------------------------------------------------------
       DASHBOARD HEADER
    -------------------------------------------------------- */

    .dashboard-title {
        font-size: 38px;
        font-weight: 800;

        color: #102a43;

        color: light-dark(
            #102a43,
            #e8eef7
        );

        margin-bottom: 3px;
        letter-spacing: -0.5px;
    }

    .dashboard-subtitle {
        font-size: 16px;

        color: #718096;

        color: light-dark(
            #718096,
            #a3b1c4
        );

        margin-bottom: 28px;
    }


    /* --------------------------------------------------------
       SECTION HEADINGS
    -------------------------------------------------------- */

    .section-heading {
        font-size: 23px;
        font-weight: 750;

        color: #102a43;

        color: light-dark(
            #102a43,
            #e8eef7
        );

        margin-top: 24px;
        margin-bottom: 10px;
    }


    /* --------------------------------------------------------
       STREAMLIT METRIC CARDS
    -------------------------------------------------------- */

    div[data-testid="stMetric"] {
        background-color: white;

        background-color: light-dark(
            #ffffff,
            #1a2130
        );

        border: 1px solid #e6ebf2;

        border-color: light-dark(
            #e6ebf2,
            #2c3444
        );

        padding: 22px 24px;
        border-radius: 16px;

        box-shadow:
            0px 5px 20px
            rgba(15, 39, 71, 0.07);

        box-shadow:
            0px 5px 20px
            light-dark(
                rgba(15, 39, 71, 0.07),
                rgba(0, 0, 0, 0.45)
            );

        min-height: 135px;
    }


    div[data-testid="stMetric"]:hover {
        transform: translateY(-2px);

        box-shadow:
            0px 8px 24px
            rgba(15, 39, 71, 0.11);

        box-shadow:
            0px 8px 24px
            light-dark(
                rgba(15, 39, 71, 0.11),
                rgba(0, 0, 0, 0.6)
            );

        transition: 0.2s ease-in-out;
    }


    div[data-testid="stMetricLabel"],
    div[data-testid="stMetricLabel"] * {
        font-size: 13px;
        font-weight: 700;

        color: #64748b;

        color: light-dark(
            #64748b,
            #9fb0c7
        );

        text-transform: uppercase;
        letter-spacing: 0.5px;
    }


    div[data-testid="stMetricValue"] {
        font-size: 31px;
        font-weight: 800;

        color: #102a43;

        color: light-dark(
            #102a43,
            #f2f6fb
        );
    }


    /* --------------------------------------------------------
       DATAFRAMES
    -------------------------------------------------------- */

    div[data-testid="stDataFrame"] {
        background-color: white;

        background-color: light-dark(
            #ffffff,
            #1a2130
        );

        border-radius: 14px;
        overflow: hidden;
    }


    /* --------------------------------------------------------
       SIDEBAR
    -------------------------------------------------------- */

    section[data-testid="stSidebar"] {
        background-color: #eef2f7;

        background-color: light-dark(
            #eef2f7,
            #151b26
        );

        border-right: 1px solid #dde3ea;

        border-right-color: light-dark(
            #dde3ea,
            #272f3d
        );
    }


    /* --------------------------------------------------------
       BUTTONS
    -------------------------------------------------------- */

    .stDownloadButton > button {
        border-radius: 10px;
        height: 46px;
        font-weight: 600;
    }


    /* --------------------------------------------------------
       DIVIDERS
    -------------------------------------------------------- */

    hr {
        border-color: #e5e9f0;

        border-color: light-dark(
            #e5e9f0,
            #2c3444
        );
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_data():

    df = pd.read_csv(
        "subscribers.csv",
        parse_dates=["signup_date"]
    )

    return df


try:

    df_original = load_data()

except FileNotFoundError:

    st.error(
        "subscribers.csv was not found. "
        "Make sure subscribers.csv is in the same folder "
        "as subscriber_analytics_dashboard.py."
    )

    st.stop()


# ============================================================
# BASIC DATASET INFORMATION
# ============================================================

initial_rows = len(df_original)


# ============================================================
# TODO 1
#
# REPORT COMPLETENESS FOR EVERY COLUMN
# ============================================================

completeness = pd.DataFrame({

    "Column":
        df_original.columns,

    "Non-Null Values":
        df_original.notna().sum().values,

    "Missing Values":
        df_original.isna().sum().values,

    "Completeness (%)":
        (
            df_original.notna().mean().values
            * 100
        ).round(2)

})


# ============================================================
# TODO 2
#
# DROP DUPLICATE subscriber_id
# KEEP THE LATEST RECORD
# ============================================================

df = df_original.copy()


rows_before_duplicates = len(df)


# Sort by signup date so that "last"
# represents the latest record.

df = (
    df
    .sort_values("signup_date")
    .drop_duplicates(
        subset="subscriber_id",
        keep="last"
    )
    .copy()
)


rows_after_duplicates = len(df)


duplicates_removed = (
    rows_before_duplicates
    - rows_after_duplicates
)


# ============================================================
# CLEAN NUMERIC COLUMNS
# ============================================================

df["total_spend"] = pd.to_numeric(
    df["total_spend"],
    errors="coerce"
)


df["churned"] = pd.to_numeric(
    df["churned"],
    errors="coerce"
)


# ============================================================
# TODO 3
#
# CREATE:
# 1. tenure_days
# 2. spend_per_month_of_tenure
# ============================================================

today = pd.Timestamp.today().normalize()


df["tenure_days"] = (
    today
    - df["signup_date"]
).dt.days


# Prevent zero or negative values from causing
# division-by-zero problems.

safe_tenure_days = (
    df["tenure_days"]
    .clip(lower=1)
)


tenure_months = (
    safe_tenure_days
    / 30.44
)


df["spend_per_month_of_tenure"] = (
    df["total_spend"]
    / tenure_months
).round(2)


# ============================================================
# TODO 4
#
# KPI TABLE BY REGION
#
# - Subscribers
# - Average Spend
# - Churn Rate
# ============================================================

kpi_by_region = (

    df
    .dropna(
        subset=["region"]
    )

    .groupby(
        "region"
    )

    .agg(

        subscribers=(
            "subscriber_id",
            "nunique"
        ),

        avg_spend=(
            "total_spend",
            "mean"
        ),

        churn_rate=(
            "churned",
            "mean"
        )

    )

    .reset_index()
)


kpi_by_region["avg_spend"] = (
    kpi_by_region["avg_spend"]
    .round(2)
)


kpi_by_region["churn_rate"] = (
    kpi_by_region["churn_rate"]
    * 100
).round(2)


# ============================================================
# TODO 5
#
# SAVE CHURN RATE BY REGION CHART
# ============================================================

plt.figure(
    figsize=(10, 6)
)


bars = plt.bar(

    kpi_by_region["region"],

    kpi_by_region["churn_rate"]

)


plt.title(
    "Churn Rate by Region",
    fontsize=16,
    fontweight="bold"
)


plt.xlabel(
    "Region"
)


plt.ylabel(
    "Churn Rate (%)"
)


# Add percentage above every bar

for bar in bars:

    value = bar.get_height()

    plt.text(

        bar.get_x()
        + bar.get_width() / 2,

        value,

        f"{value:.1f}%",

        ha="center",

        va="bottom",

        fontsize=10

    )


plt.tight_layout()


plt.savefig(
    "churn_rate_by_region.png",
    dpi=300,
    bbox_inches="tight"
)


plt.close()


# ============================================================
# TODO 6
#
# SAVE KPI TABLE
# ============================================================

kpi_by_region.to_csv(
    "kpi_by_region.csv",
    index=False
)


df.to_csv(
    "cleaned_subscribers.csv",
    index=False
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        "## 📊 Subscriber Analytics"
    )

    st.divider()

    # --------------------------------------------------------
    # FILTERS
    # --------------------------------------------------------

    st.markdown(
        "### 🔎 Dashboard Filters"
    )

    available_regions = sorted(

        df["region"]

        .dropna()

        .unique()

        .tolist()

    )

    selected_regions = st.multiselect(

        "Region",

        options=available_regions,

        default=available_regions

    )

    available_plans = sorted(

        df["plan_type"]

        .dropna()

        .unique()

        .tolist()

    )

    selected_plans = st.multiselect(

        "Plan Type",

        options=available_plans,

        default=available_plans

    )

    churn_filter = st.selectbox(

        "Subscription Status",

        options=[

            "All Subscribers",

            "Active Only",

            "Churned Only"

        ]

    )

    st.divider()

    # --------------------------------------------------------
    # DATASET INFORMATION
    # --------------------------------------------------------

    st.markdown(
        "### 📁 Dataset Information"
    )

    st.write(
        f"Original rows: **{initial_rows}**"
    )

    st.write(
        f"Clean rows: **{len(df)}**"
    )

    st.write(
        f"Duplicates removed: **{duplicates_removed}**"
    )

    st.write(
        f"Columns: **{len(df.columns)}**"
    )

    missing_total = (
        df_original
        .isna()
        .sum()
        .sum()
    )

    st.write(
        f"Missing values: **{missing_total}**"
    )


# ============================================================
# APPLY FILTERS
# ============================================================

filtered_df = df.copy()


# Region filter

if selected_regions:

    filtered_df = filtered_df[

        filtered_df["region"]
        .isin(selected_regions)

    ]


# Plan filter

if selected_plans:

    filtered_df = filtered_df[

        filtered_df["plan_type"]
        .isin(selected_plans)

    ]


# Churn filter

if churn_filter == "Active Only":

    filtered_df = filtered_df[

        filtered_df["churned"]
        == 0

    ]


elif churn_filter == "Churned Only":

    filtered_df = filtered_df[

        filtered_df["churned"]
        == 1

    ]


# ============================================================
# DASHBOARD HEADER
# ============================================================

st.markdown(

    """
    <div class="dashboard-title">
        Subscriber Intelligence Dashboard
    </div>
    """,

    unsafe_allow_html=True
)


st.markdown(

    """
    <div class="dashboard-subtitle">

        Customer retention, spending,
        subscription and regional KPI analytics

    </div>
    """,

    unsafe_allow_html=True
)


# ============================================================
# CALCULATE DASHBOARD KPIs
# ============================================================

total_subscribers = (
    filtered_df[
        "subscriber_id"
    ]
    .nunique()
)


average_spend = (
    filtered_df[
        "total_spend"
    ]
    .mean()
)


churn_rate = (
    filtered_df[
        "churned"
    ]
    .mean()
    * 100
)


average_tenure = (
    filtered_df[
        "tenure_days"
    ]
    .mean()
)


# Handle empty filters

if pd.isna(
    average_spend
):

    average_spend = 0


if pd.isna(
    churn_rate
):

    churn_rate = 0


if pd.isna(
    average_tenure
):

    average_tenure = 0


# ============================================================
# KPI CARDS
#
# FIXED VERSION USING STREAMLIT NATIVE METRICS
# ============================================================

metric1, metric2, metric3, metric4 = (
    st.columns(4)
)


with metric1:

    st.metric(

        label="Total Subscribers",

        value=f"{total_subscribers:,}"

    )


with metric2:

    st.metric(

        label="Average Spend",

        value=f"${average_spend:,.2f}"

    )


with metric3:

    st.metric(

        label="Churn Rate",

        value=f"{churn_rate:.1f}%"

    )


with metric4:

    st.metric(

        label="Average Tenure",

        value=f"{average_tenure:,.0f} days"

    )


# ============================================================
# REGIONAL PERFORMANCE
# ============================================================

st.markdown(

    """
    <div class="section-heading">
        🌎 Regional Performance
    </div>
    """,

    unsafe_allow_html=True
)


regional_filtered = (

    filtered_df

    .dropna(
        subset=["region"]
    )

    .groupby(
        "region"
    )

    .agg(

        Subscribers=(
            "subscriber_id",
            "nunique"
        ),

        Average_Spend=(
            "total_spend",
            "mean"
        ),

        Churn_Rate=(
            "churned",
            "mean"
        )

    )

    .reset_index()

)


regional_filtered[
    "Churn_Rate"
] = (

    regional_filtered[
        "Churn_Rate"
    ]

    * 100

)


# ============================================================
# REGIONAL CHARTS
# ============================================================

chart1, chart2 = (
    st.columns(2)
)


# ------------------------------------------------------------
# CHURN RATE BY REGION
# ------------------------------------------------------------

with chart1:

    if not regional_filtered.empty:

        fig_churn = px.bar(

            regional_filtered,

            x="region",

            y="Churn_Rate",

            text="Churn_Rate",

            title="Churn Rate by Region",

            labels={

                "region":
                    "Region",

                "Churn_Rate":
                    "Churn Rate (%)"

            }

        )

        fig_churn.update_traces(

            texttemplate="%{text:.1f}%",

            textposition="outside"

        )

        fig_churn.update_layout(

            height=430,

            template="plotly_white",

            title_font_size=20,

            xaxis_title=None,

            yaxis_title="Churn Rate (%)",

            margin=dict(

                l=20,

                r=20,

                t=65,

                b=20

            )

        )

        st.plotly_chart(

            fig_churn,

            use_container_width=True

        )

    else:

        st.info(
            "No regional data available "
            "for the selected filters."
        )


# ------------------------------------------------------------
# SUBSCRIBER DISTRIBUTION
# ------------------------------------------------------------

with chart2:

    if not regional_filtered.empty:

        fig_region = px.pie(

            regional_filtered,

            names="region",

            values="Subscribers",

            hole=0.58,

            title="Subscriber Distribution by Region"

        )

        fig_region.update_traces(

            textposition="outside",

            textinfo="percent+label"

        )

        fig_region.update_layout(

            height=430,

            template="plotly_white",

            title_font_size=20,

            showlegend=False,

            margin=dict(

                l=20,

                r=20,

                t=65,

                b=20

            )

        )

        st.plotly_chart(

            fig_region,

            use_container_width=True

        )

    else:

        st.info(
            "No subscriber distribution data "
            "available for the selected filters."
        )


# ============================================================
# REVENUE AND CUSTOMER INSIGHTS
# ============================================================

st.markdown(

    """
    <div class="section-heading">
        💰 Customer & Revenue Insights
    </div>
    """,

    unsafe_allow_html=True
)


chart3, chart4 = (
    st.columns(2)
)


# ------------------------------------------------------------
# AVERAGE SPEND BY PLAN
# ------------------------------------------------------------

with chart3:

    spend_by_plan = (

        filtered_df

        .dropna(
            subset=[
                "plan_type",
                "total_spend"
            ]
        )

        .groupby(
            "plan_type"
        )[
            "total_spend"
        ]

        .mean()

        .reset_index()

    )

    if not spend_by_plan.empty:

        fig_spend = px.bar(

            spend_by_plan,

            x="plan_type",

            y="total_spend",

            text="total_spend",

            title="Average Spend by Subscription Plan",

            labels={

                "plan_type":
                    "Subscription Plan",

                "total_spend":
                    "Average Spend ($)"

            }

        )

        fig_spend.update_traces(

            texttemplate="$%{text:.2f}",

            textposition="outside"

        )

        fig_spend.update_layout(

            height=430,

            template="plotly_white",

            title_font_size=20,

            xaxis_title=None,

            margin=dict(

                l=20,

                r=20,

                t=65,

                b=20

            )

        )

        st.plotly_chart(

            fig_spend,

            use_container_width=True

        )

    else:

        st.info(
            "No spending data available."
        )


# ------------------------------------------------------------
# TENURE VS SPEND
# ------------------------------------------------------------

with chart4:

    scatter_data = (

        filtered_df

        .dropna(
            subset=[
                "tenure_days",
                "total_spend",
                "region"
            ]
        )

        .copy()

    )

    if not scatter_data.empty:

        fig_scatter = px.scatter(

            scatter_data,

            x="tenure_days",

            y="total_spend",

            color="region",

            hover_name="subscriber_name",

            title="Subscriber Spend vs Tenure",

            labels={

                "tenure_days":
                    "Tenure (Days)",

                "total_spend":
                    "Total Spend ($)",

                "region":
                    "Region"

            }

        )

        fig_scatter.update_traces(

            marker=dict(
                size=11,
                opacity=0.75
            )

        )

        fig_scatter.update_layout(

            height=430,

            template="plotly_white",

            title_font_size=20,

            margin=dict(

                l=20,

                r=20,

                t=65,

                b=20

            )

        )

        st.plotly_chart(

            fig_scatter,

            use_container_width=True

        )

    else:

        st.info(
            "No tenure/spend data available."
        )


# ============================================================
# DATA QUALITY SECTION
# ============================================================

st.markdown(

    """
    <div class="section-heading">
        🧹 Data Quality & Completeness
    </div>
    """,

    unsafe_allow_html=True
)


quality1, quality2 = (
    st.columns(
        [1.4, 1]
    )
)


# ------------------------------------------------------------
# COMPLETENESS CHART
# ------------------------------------------------------------

with quality1:

    fig_complete = px.bar(

        completeness,

        x="Column",

        y="Completeness (%)",

        text="Completeness (%)",

        title="Column Completeness",

        labels={

            "Completeness (%)":
                "Completeness (%)"

        }

    )

    fig_complete.update_traces(

        texttemplate="%{text:.1f}%",

        textposition="outside"

    )

    fig_complete.update_yaxes(

        range=[
            0,
            105
        ]

    )

    fig_complete.update_layout(

        height=430,

        template="plotly_white",

        title_font_size=20,

        xaxis_title=None,

        margin=dict(

            l=20,

            r=20,

            t=65,

            b=20

        )

    )

    st.plotly_chart(

        fig_complete,

        use_container_width=True

    )


# ------------------------------------------------------------
# COMPLETENESS TABLE
# ------------------------------------------------------------

with quality2:

    st.markdown(
        "#### Completeness Report"
    )

    st.dataframe(

        completeness,

        use_container_width=True,

        hide_index=True,

        height=380

    )


# ============================================================
# REGIONAL KPI TABLE
# ============================================================

st.markdown(

    """
    <div class="section-heading">
        📈 Regional KPI Summary
    </div>
    """,

    unsafe_allow_html=True
)


display_kpi = (
    kpi_by_region
    .copy()
)


display_kpi.columns = [

    "Region",

    "Subscribers",

    "Average Spend ($)",

    "Churn Rate (%)"

]


st.dataframe(

    display_kpi,

    use_container_width=True,

    hide_index=True

)


# ============================================================
# CLEANED SUBSCRIBER DATASET
# ============================================================

st.markdown(

    """
    <div class="section-heading">
        📋 Cleaned Subscriber Dataset
    </div>
    """,

    unsafe_allow_html=True
)


display_columns = [

    "subscriber_id",

    "subscriber_name",

    "email",

    "signup_date",

    "region",

    "plan_type",

    "total_spend",

    "churned",

    "tenure_days",

    "spend_per_month_of_tenure"

]


available_display_columns = [

    column

    for column
    in display_columns

    if column
    in filtered_df.columns

]


st.dataframe(

    filtered_df[
        available_display_columns
    ],

    use_container_width=True,

    hide_index=True,

    height=430

)


# ============================================================
# EXPORT RESULTS
# ============================================================

st.markdown(

    """
    <div class="section-heading">
        📥 Export Results
    </div>
    """,

    unsafe_allow_html=True
)


download1, download2 = (
    st.columns(2)
)


# ------------------------------------------------------------
# DOWNLOAD KPI CSV
# ------------------------------------------------------------

with download1:

    kpi_csv = (

        kpi_by_region

        .to_csv(
            index=False
        )

        .encode(
            "utf-8"
        )

    )

    st.download_button(

        label="⬇️ Download Regional KPI Report",

        data=kpi_csv,

        file_name="kpi_by_region.csv",

        mime="text/csv",

        use_container_width=True

    )


# ------------------------------------------------------------
# DOWNLOAD CLEANED DATA
# ------------------------------------------------------------

with download2:

    cleaned_csv = (

        df

        .to_csv(
            index=False
        )

        .encode(
            "utf-8"
        )

    )

    st.download_button(

        label="⬇️ Download Cleaned Subscriber Data",

        data=cleaned_csv,

        file_name="cleaned_subscribers.csv",

        mime="text/csv",

        use_container_width=True

    )


# ============================================================
# ASSIGNMENT PROCESS SUMMARY
# ============================================================

st.markdown(

    """
    <div class="section-heading">
        ✅ Data Processing Summary
    </div>
    """,

    unsafe_allow_html=True
)


summary1, summary2, summary3 = (
    st.columns(3)
)


with summary1:

    st.success(
        f"Loaded {initial_rows} records "
        f"from subscribers.csv"
    )


with summary2:

    st.success(
        f"Removed {duplicates_removed} "
        f"duplicate subscriber records"
    )


with summary3:

    st.success(
        f"Final cleaned dataset contains "
        f"{len(df)} records"
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()


st.caption(

    "Subscriber Intelligence Dashboard  |  "
    "Prajwal Mrithyunjay Hulamani"

)
