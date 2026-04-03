import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv("data/clean_jobs.csv")

# --- FILTERS ---
st.sidebar.header("Filters")

selected_location = st.sidebar.selectbox(
    "Select Location",
    ["All"] + list(df['location'].unique())
)

if selected_location != "All":
    df = df[df['location'] == selected_location]

# --- TITLE ---
st.title("🚀 Job Market Intelligence Dashboard")

# --- METRICS ---
st.subheader("📊 Key Metrics")

col1, col2 = st.columns(2)

col1.metric("Total Jobs", len(df))
col2.metric("Unique Companies", df['company'].nunique())

# --- SAMPLE DATA ---
st.subheader("📄 Sample Data")
st.dataframe(df.head())

# --- PROCESS SKILLS ---
df['skills'] = df['skills'].apply(lambda x: eval(x) if isinstance(x, str) else [])

# --- TOP SKILLS ---
st.subheader("🔥 Top Skills")

all_skills = [skill for sublist in df['skills'] for skill in sublist]
skills_series = pd.Series(all_skills)
top_skills = skills_series.value_counts().head(10)

st.bar_chart(top_skills)

st.write("💡 Insight: These are the most in-demand skills based on current job listings.")

# --- TOP COMPANIES ---
st.subheader("🏢 Top Hiring Companies")

top_companies = df['company'].value_counts().head(10)
st.bar_chart(top_companies)

st.write("💡 Insight: These companies are actively hiring across roles.")

# --- JOBS BY LOCATION ---
st.subheader("🌍 Jobs by Location")

top_locations = df['location'].value_counts().head(10)
st.bar_chart(top_locations)

st.write("💡 Insight: Job distribution varies significantly by location.")