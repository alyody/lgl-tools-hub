import streamlit as st

st.set_page_config(page_title="LGL Tools Hub", layout="centered")

st.markdown("""
    <style>
        .tool-card {
            background-color: #f0f8ff;
            border-radius: 12px;
            padding: 20px;
            margin: 10px 0;
            box-shadow: 0 2px 6px rgba(0,0,0,0.1);
        }
        .tool-card h3 {
            margin-bottom: 10px;
        }
        .tool-card p {
            margin-bottom: 15px;
        }
        .stButton>button {
            background-color: #007acc;
            color: white;
            border-radius: 8px;
            padding: 10px 20px;
            border: none;
        }
        .stButton>button:hover {
            background-color: #005f99;
        }
    </style>
""", unsafe_allow_html=True)

st.title("📱 LGL Tools Hub")
st.markdown("Welcome! Choose a tool below:")

tools = [
    {
        "name": "🔄 LGL Dubai Dynamic Bot",
        "desc": "Real-time dynamic port info and updates.",
        "url": "https://lgldubaidynamicbot.streamlit.app/"
    },
    {
        "name": "🧭 LGL Ports Agents",
        "desc": "Browse agents by area, country, and port.",
        "url": "https://lglportsagents.streamlit.app/"
    },
    {
        "name": "🤖 LGL Dubai Bot",
        "desc": "Chatbot for vessel, voyage, and port call details.",
        "url": "https://lgldubaibot.streamlit.app/"
    }
]

for tool in tools:
    with st.container():
        st.markdown(f"""
        <div class="tool-card">
            <h3>{tool['name']}</h3>
            <p>{tool['desc']}</p>
        </div>
        """, unsafe_allow_html=True)
        st.link_button(f"Launch {tool['name']}", tool["url"])
