import streamlit as st
from transformers import pipeline

st.title("Tłumacz EN → DE")
st.write(
    "Aplikacja tłumaczy tekst z angielskiego na niemiecki "
    "z wykorzystaniem modelu z Hugging Face. Wpisz tekst po angielsku i kliknij **Przetłumacz**."
)

def load_translator():
    return pipeline("translation_en_to_de")


text = st.text_area("Tekst po angielsku")

if st.button("Przetłumacz"):
    if not text.strip():
        st.warning("Wpisz tekst do tłumaczenia.")
    else:
        with st.spinner("Pracuję..."):
            translator = load_translator()
            result = translator(text)
        st.success("Gotowe!")
        st.write(result[0]["translation_text"])

st.write("Numer indeksu: s27404")