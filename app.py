import streamlit as st
import datetime
import random
import base64

# ------------------- PAGE CONFIG -------------------
st.set_page_config(page_title="For My Ranjana ❤️", page_icon="💖", layout="centered")

# ------------------- BACKGROUND IMAGE -------------------
def add_bg_from_local(image_file):
    with open(image_file, "rb") as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg_from_local("bg.jpg")

# ------------------- FLOATING HEARTS -------------------
hearts_html = ""
hearts_list = ['❤️','💖','💕','💞','💗','💘','💓']
for i in range(25):
    left = random.randint(1,95)
    size = random.randint(20,50)
    duration = round(random.uniform(4,10),2)
    heart = random.choice(hearts_list)
    hearts_html += f'<div class="heart" style="left:{left}%; font-size:{size}px; animation-duration:{duration}s;">{heart}</div>'

st.markdown(
    """
    <style>
    .heart {
        position: fixed;
        bottom: 0;
        color: #ff4d6d;
        animation-name: floatHearts;
        animation-iteration-count: infinite;
        cursor: pointer;
    }

    @keyframes floatHearts {
        0% { transform: translateY(0) scale(1); opacity: 1; }
        100% { transform: translateY(-120vh) scale(1.5); opacity: 0; }
    }

    h1, h2, h3 {
        text-shadow: 2px 2px 10px #ff4d6d;
    }

    div.stButton > button {
        color: white;
        background: linear-gradient(45deg, #ff4d6d, #ff99ac);
        border-radius: 50px;
        padding: 14px 28px;
        font-size: 18px;
        font-weight: bold;
        border: none;
        box-shadow: 0px 4px 15px rgba(255,0,100,0.6);
        transition: all 0.3s ease-in-out;
    }
    div.stButton > button:hover {
        transform: scale(1.1);
        background: linear-gradient(45deg, #ff99ac, #ff4d6d);
    }

    .love-text {
        font-size: 65px;
        font-weight: bold;
        text-align: center;
        color: #ff0066;
        text-shadow: 0px 0px 20px #ff66b2, 0px 0px 40px #ff3399;
        animation: pulse 2s infinite;
    }

    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.1); }
        100% { transform: scale(1); }
    }
    </style>
    """ + hearts_html,
    unsafe_allow_html=True
)

# ------------------- MUSIC -------------------
try:
    st.audio("love.mp3", format="audio/mp3")
except:
    st.warning("🎶 Music file not found, but my heart still sings for you ❤️")

# ------------------- TITLE -------------------
st.markdown("<h1 style='text-align:center; color:#ff0066;'>💖 For My Shonu, Rani & Gullu 💖</h1>", unsafe_allow_html=True)

# ------------------- PHOTO & VIDEO -------------------
st.subheader("📸 A Memory I Love")
try:
    st.image("photo.jpg", caption="The First Photo with My Beautiful Girl Ranjana ❤️", use_container_width=True)
    st.image("photo1.jpg", caption="The Current and More to come with My Beautiful❤️", use_container_width=True)
except:
    st.warning("📷 Photo not found, but you’re always in my heart ❤️")

st.subheader("🎥 Special Moments")
try:
    st.video("video2.mp4")
    st.video("video1.mp4")
except:
    st.warning("🎥 Videos not found, but memories with you play in my heart 💕")

# ------------------- SURPRISES + COUNTDOWN -------------------
today = datetime.date.today()
birthday = datetime.date(today.year, 9, 29)
if birthday < today:
    birthday = datetime.date(today.year + 1, 9, 29)
days_left = (birthday - today).days

if st.button("🎉 Reveal All Surprises & Countdown 🎉"):
    # Messages
    messages = [
        "Shonu, you’re the most special person in my life 💖",
        "Rani, even Python can’t handle the exception of not loving you 😘",
        "Gullu, you are my favorite constant in this changing world 🌍",
        "Ranjana, if beauty was code, you’d be an infinite loop ✨",
        "You’re my forever debug solution 🐞❤️",
        "You make my heart run faster than any processor 💕",
        "In Short, Tu HMAAR JAAN HAU KAREJA aur HUM TOHRAKE BHUT PREM KRENI 😘",
    ]
    for msg in messages:
        st.success(msg)

    # BIG LOVE TEXT
    st.markdown("<div class='love-text'>I LOVE YOU ❤️</div>", unsafe_allow_html=True)

    # Birthday countdown
    st.markdown(f"<h3 style='text-align:center; color:#ff99cc;'>Only {days_left} days left until your birthday, Ranjana 🎉</h3>", unsafe_allow_html=True)

    # Advance birthday message
    st.markdown(
        """
        <h2 style='text-align:center; color:#ffccff; margin-top:30px;' >
        🎂 My Dearest Ranjana, Your birthday is coming soon 🎂
        </h2>
        <p style='text-align:center; font-size:20px; color:white;' >
        I can’t wait to celebrate the most beautiful day of my life – the day you were born.  
        You are my happiness, my strength, and my forever.  
        On your special day, I wish you endless joy, success, and love.  
        But most importantly, I wish you stay Happy & Healthy so I can see your Beautiful Smile 💕.  
        </p>
        """,
        unsafe_allow_html=True
    )

# ------------------- ACTUAL BIRTHDAY SURPRISE -------------------
if today.month == 9 and today.day == 29:
    st.balloons()
    st.success("🎂 Happiest 22nd advance Birthday My Jaan! 🎂")
    st.markdown(
        """
        <h2 style='text-align:center; color:#ff0066;'>💖 Wishing you the happiest birthday, Shonu 💖</h2>
        <h3 style='text-align:center;'>You're my everything! 🎉🎁✨</h3>
        """,
        unsafe_allow_html=True
    )

st.write("---")
st.caption("Made with ❤️, music, floating hearts & Python, only for you, my Shonu 💕")
