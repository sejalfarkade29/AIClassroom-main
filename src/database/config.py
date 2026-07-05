import streamlit as st
from supabase import create_client, Client
supabase: Client = create_client(
    st.secrets["SUPABASE_URL"],
    st.secrets["SUPABASE_KEY"]
)



#import streamlit as st
#from supabase import create_client

#st.write("URL:", st.secrets["SUPABASE_URL"])
#st.write("KEY starts with:", st.secrets["SUPABASE_KEY"][:20])

#supabase = create_client(
#    st.secrets["SUPABASE_URL"],
#    st.secrets["SUPABASE_KEY"]
#)

