######################
# Import libraries
######################

import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

######################
# Page Title
######################

image = Image.open(r"C:\Users\Ron\Documents\Scrape\FOR PORTFOLIO\DNA COUNT\dnalogo.png")

st.image(image, use_column_width=True)

st.write("""
# DNA Nucleotide Count and Conversion Web App

This app counts and converts the nucleotide composition of query DNA!

***
""")


######################
# Input Text Box
######################

#st.sidebar.header('Enter DNA sequence')
st.header('Enter DNA sequence')

sequence_input = ">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

#sequence = st.sidebar.text_area("Sequence input", sequence_input, height=250)
sequence = st.text_area("Sequence input", sequence_input, height=250)
sequence = sequence.splitlines()
# st.write(sequence)
sequence1 = sequence[1:] # Skips the sequence name (first line)
# st.write(sequence)
sequence = ''.join(sequence1) # Concatenates list to string
# st.write(sequence)

st.write("""
***
""")

## Prints the input DNA sequence
st.header('INPUT (DNA Query)')
sequence

## DNA nucleotide count
st.header('OUTPUT (DNA Nucleotide Count)')

### 1. Print dictionary
st.subheader('1. Print dictionary')
def DNA_nucleotide_count(seq):
  d = dict([
            ('A',seq.count('A')),
            ('T',seq.count('T')),
            ('G',seq.count('G')),
            ('C',seq.count('C'))
            ])
  return d

X = DNA_nucleotide_count(sequence)
st.write(X)
#X_label = list(X)
#X_values = list(X.values())

# X

### 2. Print text
st.subheader('2. Print text')
st.write('There are  ' + str(X['A']) + ' adenine (A)')
st.write('There are  ' + str(X['T']) + ' thymine (T)')
st.write('There are  ' + str(X['G']) + ' guanine (G)')
st.write('There are  ' + str(X['C']) + ' cytosine (C)')

### 3. Display DataFrame
st.subheader('3. Display DataFrame')
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns = {'index':'nucleotide'})
st.write(df)

### 4. Display Bar Chart using Altair
st.subheader('4. Display Bar chart')
p = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
)
p = p.properties(
    width=alt.Step(80)  # controls width of bar.
)
st.write(p)

### 5. Conversion MRNA/TRNA
st.subheader('5. Conversion to MRNA/TRNA')
convert_dna = st.selectbox('Convert',['MRNA','TRNA'])

def list_to_convert(x):
  to_MRNA = {
    'A':'U',
    'C':'G',
    'T':'A',
    'C':'G'
  }
  to_TRNA = {
    'A':'A',
    'C':'C',
    'T':'U',
    'C':'C'
  }
  converted = []
  temp_convert = []
  if convert_dna == 'MRNA':
    for sublist in x:
      sub_list = []
      for index, item in enumerate(sublist):
          if item in to_MRNA:
            sub_list.append(to_MRNA[item])
      temp_convert.append(sub_list)
  else:
    for sublist in x:
      sub_list = []
      for index, item in enumerate(sublist):
          if item in to_TRNA:
            sub_list.append(to_TRNA[item])
      temp_convert.append(sub_list)
  for sub in temp_convert:
    new_sequence = "".join(sub)
    converted.append(new_sequence)
  return new_sequence
st.write(list_to_convert(sequence1))
