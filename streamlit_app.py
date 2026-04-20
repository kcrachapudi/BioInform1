import streamlit as st
import os
import sys
import zipfile
import pandas as pd

# --- FIX IMPORT PATH (parent dir) ---
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from scripts.pipeline import run_fastqc


# -----------------------------
# CONFIG
# -----------------------------
st.set_page_config(page_title="BioInform1 QC App", layout="wide")

st.title("🧬 BioInform1 - NGS Quality Control Dashboard")


# -----------------------------
# SIDEBAR
# -----------------------------
page = st.sidebar.selectbox(
    "Navigation",
    ["Run Pipeline", "QC Metrics", "About"]
)


# -----------------------------
# HELPER: Parse FastQC ZIP
# -----------------------------
def parse_fastqc(zip_path):
    data = {}

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        file_name = [f for f in zip_ref.namelist() if "fastqc_data.txt" in f][0]

        with zip_ref.open(file_name) as f:
            lines = f.read().decode().split("\n")

    current_section = None

    for line in lines:
        if line.startswith(">>"):
            current_section = line.split("\t")[0]
            data[current_section] = []
        elif current_section and not line.startswith("#") and line.strip():
            data[current_section].append(line.split("\t"))

    return data


# -----------------------------
# PAGE 1: RUN PIPELINE
# -----------------------------
if page == "Run Pipeline":

    st.subheader("Run FastQC Pipeline")

    option = st.radio(
        "Choose input type:",
        ["Use Sample Data", "Upload FASTQ File"]
    )

    input_path = None

    # Sample
    if option == "Use Sample Data":
        input_path = "data/sample.fastq"
        st.info("Using sample FASTQ")

    # Upload
    else:
        uploaded_file = st.file_uploader("Upload FASTQ", type=["fastq"])

        if uploaded_file:
            input_path = "data/upload.fastq"
            with open(input_path, "wb") as f:
                f.write(uploaded_file.read())
            st.success("File uploaded")

    # Run
    if st.button("Run QC Pipeline") and input_path:
        with st.spinner("Running FastQC..."):
            run_fastqc(input_path)
        st.success("Pipeline completed")

        # Show quick summary
        st.subheader("✅ QC Completed")
        zip_files = [f for f in os.listdir("results") if f.endswith(".zip")]
        if zip_files:
            st.info("Results generated successfully")
            st.markdown("👉 Go to **QC Metrics** page to view detailed analysis")

# -----------------------------
# PAGE 2: QC METRICS
# -----------------------------
elif page == "QC Metrics":
    col1, col2, col3 = st.columns(3)

    col1.metric("Total Reads", "3")   # mock for now
    col2.metric("QC Status", "PASS")
    col3.metric("File Type", "FASTQ")

    st.subheader("QC Metrics & Visualizations")

    result_files = os.listdir("results") if os.path.exists("results") else []
    zip_files = [f for f in result_files if f.endswith(".zip")]

    if not zip_files:
        st.warning("No FastQC results found. Run pipeline first.")
    else:
        latest_zip = os.path.join("results", sorted(zip_files)[-1])
        qc_data = parse_fastqc(latest_zip)

        st.success("Loaded FastQC Data")

        # ---- Sections ----
        st.write("Available Sections:")
        st.write(list(qc_data.keys()))

        df_quality = None
        df_gc = None
        # ---- Per Base Quality ----
        if ">>Per base sequence quality" in qc_data:
            section = qc_data[">>Per base sequence quality"]

            df_quality = pd.DataFrame(section[1:], columns=section[0])
            df_quality = df_quality.astype(float)

        # ---- GC Content ----
        if ">>Per sequence GC content" in qc_data:
            section = qc_data[">>Per sequence GC content"]
            df_gc = pd.DataFrame(section[1:], columns=section[0])
            df_gc = df_gc.astype(float)

        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Quality Scores")
            st.line_chart(df_quality)
            st.markdown("""
            **Phred Quality Score:**
            Higher = better sequencing accuracy  
            Q20 = 1% error, Q30 = 0.1% error
            """)
        with col2:
            st.subheader("GC Content")
            st.bar_chart(df_gc.set_index(df_gc.columns[0]))
            st.markdown("""
            **GC Content:**
            % of G/C bases in DNA  
            Deviations may indicate contamination or bias
            """)


# -----------------------------
# PAGE 3: ABOUT
# -----------------------------
else:

    st.subheader("About BioInform1")

    st.markdown("""
    ### 🧬 Overview
    This app performs quality control on sequencing data using FastQC.

    ### 🔬 Pipeline
    FASTQ → QC Analysis → Metrics → Visualization

    ### 💻 Tech
    - Python
    - Streamlit
    - FastQC

    ### 🧠 Concepts
    - Phred Quality Scores
    - GC Content
    - Read Quality Assessment

    ### 🎯 Use Case
    Ensures sequencing data is high-quality before downstream analysis
    """)
