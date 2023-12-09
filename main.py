import base64
import plotly.express as px
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Simple Make up Blog", page_icon="💄", layout="wide")

df = px.data.iris()

@st.cache_data
def get_img_as_base64(file):
        with open(file, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()


img = get_img_as_base64("a1.jpg")
page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
    background-image: url("data:image/png;base64,{img}");
    background-position: center; 
    background-repeat: no-repeat;
    background-size: 110%;
    background-attachment: local;
    }}

    [data-testid="stHeader"] {{
    background: rgba(0,0,0,0);
    }}

    [data-testid="stToolbar"] {{
    right: 2rem;
    }}
    </style>
    """


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style.css")

# ---- LOAD ASSETS ----
img_contact_form = Image.open("a2.jpg")
img_lottie_animation = Image.open("a1.jpg")

# ---- HEADER SECTION ----

with st.container():
    cols1, cols2 = st.columns([3,1])
    with cols1:
        st.subheader("Hello Everyone😜, Welcome to my Blog")
        st.title("A BSCpE Student from SNSU")
        st.write(
            "Live your best, act your best, and think your best each day. For there may be no tomorrow.."
        )
    with cols2:
        st.image("me.png")
        st.write("[Learn More About](https://www.facebook.com/junuel.paragat.31)")
# ---- WHAT I DO ----
with st.container():
    st.write("---")
    st.title("SIMPLE GLAM MAKE UP TUTORIAL💄")
    left_column, right_column = st.columns(2)
    with left_column:
         col1, col2 = st.columns(2)
        
    v1 = col1.button("READ CONTENT")
    if v1:
            with st.container():
                col1, col2,  = st.columns(2)
                # Replace 'your_video_file1.mp4' and 'your_video_file2.mp4' with the paths to your video files
                with col1:
                    st.subheader("Make Up💄")
                    st.write("""
                                    Unlock Your Beauty: The Art of Makeup by Junuel Madelo Paragat

                                    - ✔️ Welcome to the enchanting world of makeup, where colors become your palette, and your face is the canvas for self-expression. Junuel Madelo Paragat, a talented makeup artist with a passion for creativity, invites you to embark on a journey of beauty and transformation.

                                    Express Yourself Through Colors:
                                    For Junuel, makeup is more than just a routine; it's a form of artistic expression. From vibrant eyeshadows that tell a story to bold lip colors that speak volumes, Junuel believes that makeup is a powerful tool for showcasing your unique personality and style.

                                    Every Face Tells a Story:
                                    - ✔️ As a makeup artist, Junuel understands that every face is a unique canvas with its own story to tell. Whether enhancing natural features or creating bold, avant-garde looks, Junuel's approach to makeup is personalized, ensuring that each creation reflects the individuality of the wearer.

                                    Tutorials and Tips for All Skill Levels:
                                    - ✔️ Junuel is committed to sharing their knowledge and expertise with the community. Dive into their makeup tutorials, where they break down techniques, share product recommendations, and offer valuable tips for makeup enthusiasts of all skill levels. From beginners looking to master the basics to seasoned makeup artists seeking inspiration, there's something for everyone.

                                    Beyond Beauty: Empowering Confidence:
                                    - ✔️ More than just a cosmetic enhancement, Junuel believes that makeup has the power to boost confidence and empower individuals. Through the transformative nature of makeup, Junuel aims to inspire others to embrace their uniqueness and feel confident in their own skin.

                                    Makeup as a Ritual:
                                    - ✔️ For Junuel, applying makeup is a ritual—a moment of self-care and reflection. Whether it's the daily routine of enhancing natural features or the excitement of experimenting with bold looks for special occasions, Junuel encourages everyone to find joy and mindfulness in the process of applying makeup.




  
                             """)
                   
                with col2:
                    st.image("makeup.jpg")
                    st.write("""
                         
                            Connect with the Community:
                            - ✔️ Join Junuel's makeup community, a space where beauty enthusiasts come together to share tips, inspiration, and the joy of all things makeup. Engage in discussions, ask questions, and be part of a supportive community that celebrates the diverse ways individuals express themselves through makeup.

                            Get Ready to Transform:
                           - ✔️ Whether you're a makeup aficionado or a curious beginner, Junuel Madelo Paragat invites you to explore the world of makeup as a form of art, self-expression, and empowerment. Unlock your beauty potential and let your inner creativity shine through the magical touch of makeup
                           - ✔️ Cosmetics designed to enhance or alter one's appearance (makeup) can be used to conceal blemishes.
                           - ✔️ Enhance one's natural features (such as the eyebrows and eyelashes), add color to a person's face.
                           - ✔️ change the appearance of the face entirely to resemble a different person, creature or object.
                                        
                            
                            """)
                    st.write("[Watch](https://youtu.be/0GzaX2781Tg)")
                    st.write("[Read More](https://www.mbmmakeupstudio.com/dos-and-donts-of-achieving-a-natural-makeup-look/)")
# ---- PROJECTS ----
    v2 = col1.button("MORE ABOUT THE AUTHOR")
    if v2:
            with st.container():
                col1, col2,  = st.columns(2)
                image_column, text_column = st.columns((1, 2))
                # Replace 'your_video_file1.mp4' and 'your_video_file2.mp4' with the paths to your video files
                with col1:
                    st.subheader("ABOUT THE AUTHOR🙎")
                    st.write("""
                            Junuel Madelo Paragat is a vibrant and creative individual hailing from the picturesque town of Kitcharao in Agusan del Norte, Philippines. At the young age of 20, Junuel has already carved a niche for themselves in various fields, showcasing a diverse range of interests and talents.

                            Dancer Extraordinaire:
                            - ✔️ One of Junuel's greatest passions is dancing. With an innate sense of rhythm and a flair for choreography, they bring energy and grace to every performance. Whether it's the latest dance trends or traditional cultural expressions, Junuel's dance moves are a captivating sight.

                            Makeup Maven:
                            - ✔️ Beyond the dance floor, Junuel is also a skilled makeup artist. They have a keen eye for colors, textures, and the transformative power of makeup. From subtle everyday looks to bold and artistic creations, Junuel's makeup artistry reflects a deep appreciation for self-expression and beauty.

                            Gamer at Heart:
                            - ✔️ In the virtual realm, Junuel is an avid online gamer. From immersive RPGs to competitive multiplayer battles, they navigate digital worlds with enthusiasm and skill. Gaming provides a unique platform for Junuel to unwind, connect with friends, and explore fantastical landscapes.

                            Creative Spirit:
                            - ✔️ Whether through dance, makeup, or gaming, Junuel's creativity knows no bounds. They approach life with an open mind, always seeking new avenues for self-expression and personal growth.

                        
                            
                            """)
                with col2:
                   st.image(img_contact_form)
                   st.write("""
                            
                            Community Contributor:
                            - ✔️ In addition to their personal pursuits, Junuel actively contributes to their local community. Whether it's organizing dance workshops, participating in charitable events, or sharing makeup tutorials, Junuel believes in giving back and making a positive impact.

                            As Junuel continues to evolve and explore their passions, they invite you to join them on this journey of self-discovery, creativity, and community engagement. Through their various endeavors, Junuel Madelo Paragat exemplifies the spirit of a young individual making waves and leaving a mark in their corner of the world.
                    
                            """)
                   st.write("[Learn More About](https://www.facebook.com/junuel.paragat.31)")
# ---- PROJECTS

       

# ---- CONTACT ----
st.markdown("---")    
st.header(":mailbox: Get In Touch With Me!")
contact_form = """
        <form action="https://formsubmit.co/paragatjunuel@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here"></textarea>
        <button type="submit">Send</button>
        </form>
        """
st.markdown(contact_form, unsafe_allow_html=True)

        # Use Local CSS File
def local_css(file_name):
                with open(file_name) as f:
                        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style.css")