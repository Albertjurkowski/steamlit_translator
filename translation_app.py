import streamlit as st
from transformers import pipeline

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

st.write("Numer indeksu: s27404")