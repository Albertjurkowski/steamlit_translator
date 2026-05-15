import warnings
import streamlit as st
from transformers import pipeline
from pathlib import Path

st.set_page_config(page_title="Tłumacz angielsko-niemiecki", layout="wide")

st.title("Tłumacz ang na niem")

base_path = Path(__file__).parent
col1, col2 = st.columns(2)
with col1:
    st.image(str(base_path / "flaga.png"), caption="Flaga Niemiec", width=250)
with col2:
    st.image(str(base_path / "image.png"), caption="Flaga Wielkiej Brytanii", width=250)

st.title("Tłumacz ang na niem")
st.write(
    "Aplikacja tłumaczy tekst z angielskiego na niemiecki z wykorzystaniem modelu z Hugging Face. Wpisz tekst po angielsku i kliknij Przetłumacz."
)

text = st.text_area("Tekst po angielsku")

if st.button("Przetłumacz"):
    with st.spinner("Pracuję..."):
        translator = pipeline("translation_en_to_de", model="t5-base")
        result = translator(text)
    st.success("Gotowe!")
    st.write(result[0]["translation_text"])
    st.balloons()

st.write("Numer indeksu: s27404")