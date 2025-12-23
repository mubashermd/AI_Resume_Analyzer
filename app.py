import streamlit as st
import tempfile, os
import pandas as pd

from modules.file_utils import extract_zip, read_resume_texts
from modules.gemini_extractor import extract_resume_data

st.set_page_config(page_title="AI Resume Analyzer", layout="wide")
st.title("🔍 AI Resume Analyzer (Gemini 2.5 Flash)")

uploaded_file = st.file_uploader("Upload ZIP of resumes", type="zip")

if uploaded_file:
    with tempfile.TemporaryDirectory() as tmpdir:
        extract_zip(uploaded_file, tmpdir)
        resumes = read_resume_texts(tmpdir)

        if not resumes:
            st.error("No resumes found in ZIP.")
        else:
            st.info(f"Processing {len(resumes)} resumes...")
            results = []
            progress = st.progress(0)

            for i, (fn, text) in enumerate(resumes.items(), start=1):
                data = extract_resume_data(text)
                data.filename = fn
                results.append(data)
                progress.progress(i/len(resumes))

            df = pd.DataFrame(results)
            out_path = "outputs/extracted_resumes.csv"
            os.makedirs("outputs", exist_ok=True)
            df.to_csv(out_path, index=False)

            st.success("Extraction complete!")
            st.download_button(
                label="Download CSV",
                data=open(out_path, "rb"),
                file_name="extracted_resumes.csv",
                mime="text/csv"
            )
