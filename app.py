from PIL import Image
import streamlit as st
from googletrans import Translator

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="AI Multi-Language Translator",
    page_icon="assets/565635.png",
    layout="wide"
)

# =========================
# LOAD LOGO
# =========================
logo = Image.open("assets/logo.png")

# =========================
# CUSTOM CSS
# =========================
st.markdown("""
<style>

.main {
    background-color: #ffffff;
}

.title {
    font-size: 42px;
    font-weight: bold;
    color: #4285F4;
}

.subtitle {
    font-size: 18px;
    color: gray;
}

.stTextArea textarea {
    font-size: 20px;
    border-radius: 10px;
    border: 1px solid #dcdcdc;
}

.stButton button {
    background-color: #4285F4;
    color: white;
    border-radius: 10px;
    height: 50px;
    width: 200px;
    font-size: 18px;
    border: none;
}

.stButton button:hover {
    background-color: #3367D6;
    color: white;
}

.block-container {
    padding-top: 2rem;
}

</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================
col1, col2 = st.columns([1,10])

with col1:
    st.image(logo, width=70)

with col2:
    st.markdown(
        """
        <h1 style='color:#4285F4;
        font-size:40px;
        margin-top:10px;'>
        AI Multi-Language Translator
        </h1>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        "<p style='font-size:20px;color:gray;'>Natural Language Processing Project</p>",
        unsafe_allow_html=True
    )

# =========================
# SIDEBAR
# =========================
st.sidebar.title("📚 NLP Syllabus Topics Covered")

st.sidebar.markdown("""
## NLP Concepts Used
- Machine Translation
- Text Processing
- Language Modeling
- Lexical Analysis
- Encoder-Decoder Architecture
""")

st.sidebar.markdown("---")
st.sidebar.info("Mini Project for Natural Language Processing Subject")

# =========================
# TRANSLATOR
# =========================
translator = Translator()

languages = {
    "English": "en",
    "Hindi": "hi",
    "Tamil": "ta",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Japanese": "ja",
    "Chinese": "zh-cn",
    "Kannada": "kn",
    "Telugu": "te",
    "Malayalam": "ml"
}

# =========================
# LANGUAGE SELECTORS
# =========================
col1, col2 = st.columns(2)

with col1:
    source_lang = st.selectbox(
        "From",
        list(languages.keys()),
        index=0
    )

with col2:
    target_lang = st.selectbox(
        "To",
        list(languages.keys()),
        index=1
    )

# =========================
# TEXT AREAS
# =========================
left_col, right_col = st.columns(2)

with left_col:
    text = st.text_area(
        "Enter Text",
        height=300,
        placeholder="Type text here..."
    )

with right_col:
    output_placeholder = st.empty()

# =========================
# TRANSLATE BUTTON
# =========================
st.write("")
center_col1, center_col2, center_col3 = st.columns([2,2,2])

with center_col2:
    translate_button = st.button("Translate")

# =========================
# TRANSLATION LOGIC
# =========================
if translate_button:

    if text.strip() == "":
        st.warning("Please enter some text.")

    else:
        try:
            translated = translator.translate(
                text,
                src=languages[source_lang],
                dest=languages[target_lang]
            )

            output_placeholder.text_area(
                "Translated Text",
                translated.text,
                height=300
            )

            st.success("Translation Completed Successfully!")

        except Exception as e:
            st.error(f"Error: {e}")

# =========================
# FOOTER
# =========================
st.markdown("---")
st.markdown(
    "<center>Developed using NLP and Machine Translation Done By Srajan M</center>",
    unsafe_allow_html=True
)