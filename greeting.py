import streamlit as st

# Initialize session state
if "page" not in st.session_state:
    st.session_state.page = "home"
if "option" not in st.session_state:
    st.session_state.option = "NULL"
if "choice" not in st.session_state:
    st.session_state.choice = None
if "wishes" not in st.session_state:
    st.session_state.wishes = ""
if "to" not in st.session_state:
    st.session_state.to = ""
if "from" not in st.session_state:
    st.session_state.from_name = ""

# Navigation logic
if st.session_state.page == "home":
    st.title("Welcome to Greetings.py")
    option = st.selectbox("Choose your Option", 
                          ["NULL", "Birthday", "Valentine's Day", "Anniversary", "Baby Shower"])
    st.write("You selected:", option)

    st.session_state.option = option

    if option == "Birthday":
        st.text("Got it 🎉")
        st.balloons()
    elif option == "Valentine's Day":
        st.text("Got it ❤️")
        st.snow()
    elif option == "Anniversary":
        st.text("Got it 💍")
        st.balloons()
    elif option == "Baby Shower":
        st.text("Got it 👶")
        st.balloons()

    if st.button("Create Now"):
        st.session_state.page = "next"

# 2nd and edit page
elif st.session_state.page == "next":
    st.write("Edit your Greeting")

    option = st.session_state.option  

    st.session_state.to = st.text_input("TO : ")

    if option == "Birthday":
        st.title("Happy Birthday")
        choice = st.radio("Pick one:", [""""🌟 Good Wishes

                Wishing you a day filled with love, laughter, and cake. Happy Birthday!
    May your birthday be as special as you are. Cheers to another amazing year!
    Happy Birthday! Hope all your dreams come true today and always.
    
    On your special day, I wish you endless happiness, good health, and success. You deserve the very best!
    Happy Birthday to someone who makes the world brighter just by being in it.
    May this year bring you closer to your dreams and surround you with love.
    
    Happy Birthday! Time to eat cake, make memories, and dance like nobody’s watching.
    Another year older, wiser, and even more fabulous—cheers to you!
    Birthdays are nature’s way of telling us to eat more cake. Enjoy every bite!
    
    Wishing you continued success and happiness on your birthday and always.
    Happy Birthday! May this year be filled with achievements and joyful moments.
    Best wishes for a wonderful birthday and a prosperous year ahead.""",
                                       
                       """ 🎂 Poem 
                       
Another year, a brighter light,  
A candle’s glow, a wish takes flight.  
Laughter rings and hearts unite,  
To celebrate your joy tonight.  

May dreams unfold, both big and small,  
And happiness surround it all.  
With love and cheer, the day is yours,  
A journey blessed with open doors.  

So dance, so smile, let spirits soar,  
This birthday shines forevermore!
"""])
        
    elif option == "Valentine's Day":
        st.title("Happy Valentine's Day")
        choice = st.radio("Pick one:", ["""✨ Good Wishes
            
                Happy Valentine’s Day to the love of my life. You make every day brighter just by being you.
    With you, every moment feels like a fairytale. Wishing you endless love today and always.
    You are my heart, my soul, my everything. Happy Valentine’s Day!
    You are my heart, my soul, my everything. Happy Valentine’s Day!

    Happy Valentine’s Day! You’re my favorite person to laugh with, dream with, and eat chocolate with.
    Roses are red, violets are blue, life is sweeter because of you.
    You make my world sparkle. Sending hugs and kisses your way today!
            
    Happy Valentine’s Day to a wonderful friend! Thanks for filling my life with joy and laughter.
    Valentine’s Day isn’t just for couples—it’s for celebrating amazing friends like you.
    Wishing you love, happiness, and lots of chocolate today!
            
    Wishing you a day filled with appreciation and kindness. Happy Valentine’s Day!
    May this Valentine’s Day remind you of the value of love, friendship, and teamwork.
    Best wishes for a joyful Valentine’s Day and continued success.""",
                                        
                        """ ❤️ Poem 
                        
In every smile, in every glance,  
I find a spark, a sweet romance.  
The world feels brighter, skies more blue,  
Because my heart belongs to you.  

Like roses blooming, love takes flight,  
It paints the day in colors bright.  
So here’s my wish, both true and clear,  
Happy Valentine’s, my dear!
"""])
    
    elif option == "Anniversary":
        st.title("Happy Anniversary")
        choice = st.radio("Pick one:", ["""🌟 Good Wishes

            Happy Anniversary to my soulmate. Every day with you is a blessing, and I look forward to a lifetime more.
    Another year, another chapter in our love story. Thank you for being my forever.
    Happy Anniversary! You are my today and all of my tomorrows.
    
    Wishing you both endless love and happiness as you celebrate another year together.
    Happy Anniversary! May your bond grow stronger and your love deeper with each passing year.
    Cheers to the beautiful journey you’ve shared and the many more milestones ahead.
    
    Happy Anniversary! You two are proof that love and laughter make the best recipe for a happy marriage.
    Another year of putting up with each other—congratulations!
    Happy Anniversary! May your love continue to be as fun and fabulous as you are.
    
    Wishing you continued joy and companionship on your anniversary.
    Happy Anniversary! May your partnership be blessed with harmony and success.
    Best wishes for a wonderful anniversary and many more years of happiness together.""",

                        """ 🌹 Poem 
                        
Through every dawn, through every night,  
Your love has been my guiding light.  
The years may pass, yet still we find,  
A deeper bond, a heart aligned.  

With laughter shared and trials too,  
I’ve grown in love because of you.  
So here’s to us, our endless song,  
A journey sweet, forever strong.  

Happy Anniversary, my love so true,  
My world is brighter, all with you.
"""])
        
    elif option == "Baby Shower":
        st.title("Happy Baby Shower")
        choice = st.radio("Pick one:", ["""🌟 Good Wishes
                
                Wishing you endless love and happiness as you welcome your little bundle of joy.
    May your baby bring you more smiles, laughter, and love than you ever imagined.
    Congratulations on this beautiful new chapter—your family is about to grow in the most wonderful way.

    Get ready for sleepless nights, endless giggles, and a lifetime of love. Congratulations!
    Tiny hands, tiny feet, and a whole lot of cuteness—your adventure begins now!
    Babies are the best kind of surprise—wishing you joy, diapers, and lots of coffee!

    So excited to meet the newest member of the family. This baby is already so loved!
    Your little one is lucky to have parents as amazing as you. Wishing you all the happiness in the world.
    From lullabies to first steps, may every moment be filled with love and wonder.

    Best wishes as you prepare to welcome your new arrival. May parenthood bring you joy and fulfillment.
    Congratulations on this exciting milestone. Wishing you and your family health and happiness.
    May your baby shower be the start of a journey filled with love, laughter, and cherished memories.""",
                                        
                        """ 🎀 Pome 
                        
Tiny kicks and gentle dreams,  
A future brighter than it seems.  
Little hands and eyes so new,  
A world of love awaits for you.  

Today we gather, hearts aglow,  
To celebrate the joy we know.  
A precious gift, a life so dear,  
A baby’s laughter soon to hear.  

May blessings bloom, both near and far,  
For this sweet child, our shining star.
"""])

    st.session_state.choice = choice
    st.write(f"You picked:\n{st.session_state.choice}")

    st.session_state.wishes = st.text_input("Type your Good wishes: ")
    st.session_state.from_name = st.text_input("From: ")

    # Go Back button
    if st.button("Go Back"):
        st.session_state.page = "home"

    if st.button("Save & Continue"):
        st.session_state.page = "final"

# Final preview page
elif st.session_state.page == "final":
    st.title("🎉 Your Final Greeting 🎉")

    st.subheader(st.session_state.option)
    st.write(f"**To:** {st.session_state.to}")
    st.write(f"**Template Chosen:**\n{st.session_state.choice}")
    st.write(f"**MY Feeings:**\n{st.session_state.wishes}")
    st.write(f"**From:** {st.session_state.from_name}")

    st.success("Your greeting is ready ✅")

    if st.button("Go Back to Edit"):
        st.session_state.page = "next"
    if st.button("Start Over"):
        st.session_state.page = "home"