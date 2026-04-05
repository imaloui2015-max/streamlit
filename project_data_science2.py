import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

####################
#PAGE TITLE
####################

image = Image.open('image.png')

st.image(image, use_column_width=True)

st.write("""
# DNA NUCLEOTIDE WEB APP

This App Count the nucleotide composition of query DNA:

***
""")

##################
# INPUT TEXT BOX
##################

#ST HEADER
st.header('ENTER DNA SEQUENCE')

sequence_input = "DNA Query 1: \n AECTAGCAGCTAGCTAGCTAGCTAGCTAGCTAGC\nEGCTAGCTAGCTAGFVHGCTAGCTAGCTAGCTAGC\nAGCTAGCHAGUFAGCGAGCTAGCTAGCTAGCTAGC\n"

sequence = st.text_area("Sequence input", sequence_input, height=250)
sequence = sequence.splitlines()
sequence = sequence[1:] # Skipping the first line which is the header
sequence = ''.join(sequence) #COMBINE

st.write("""
***      
""")

#PRINT THE OUTPUT DNA SEQUENCE
st.header('INPUT (DNA Query)')
sequence

## DNA COUNT
st.header('OUTPUT (DNA Nucleotide Count)')
st.subheader('1. Print Dictionary')
def DNA_nucleotide_count(seq):
    d = dict([
        ('A', seq.count('A')),
        ('T', seq.count('T')),
        ('G', seq.count('G')),
        ('C', seq.count('C'))
    ])
    return d

X = DNA_nucleotide_count(sequence)

### Print Text
st.subheader('2. Print Text')
st.write('There are ' + str(X['A']) + ' adenine (A)')
st.write('There are ' + str(X['T']) + ' thymine (T)')
st.write('There are ' + str(X['G']) + ' guanine (G)')
st.write('There are ' + str(X['C']) + ' cytosine (C)')

### Display DataFrame
st.subheader('3. Display DataFrame')
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns={'index': 'nucleotide'})
st.write(df)

### Display Bar Chart using Altair
st.subheader('4. Display Bar Chart')
chart = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
)
p = chart.properties(
    width=alt.Step(80)
)
st.write(p)
