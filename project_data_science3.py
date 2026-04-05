import pandas as pd
import streamlit as st
from PIL import Image
import yfinance as yf
import altair as alt

# عنوان
st.header("This Shows the Most Popular Programming Language")

# عرض الصورة
image = Image.open('image.png')
st.image(image, use_column_width=True)

# اختيار لغة البرمجة
programms = st.selectbox(
    "Which programming language do you like?", 
    ["Python", "JavaScript", "Java", "C#", "C++", "Go", "Ruby", "Swift", "Kotlin", "PHP"]
)
st.write("You selected:", programms)

# نص تسلسلي للغات
sequence = """Python
JavaScript
Java
C#
C++
Go
Ruby
Swift
Kotlin
PHP"""

sequence = st.text_area("Sequence input", sequence, height=250)

# تحويل النص لائحة مفصولة بفواصل
sequence_list = [x.strip() for x in sequence.splitlines() if x.strip()]
sequence_str = ', '.join(sequence_list)
st.write("The most popular programming languages are:", sequence_str)

# دالة للحصول على معلومات عن كل لغة
def get_info(seq_list):
    info_dict = {}
    for i in seq_list:
        try:
            result = yf.Ticker(i)
            info_dict[i] = result.info  # خزن المعلومات في dictionary
            st.write(f"Information about {i}:")
            st.write(result.info)
        except Exception as e:
            st.write(f"Error fetching {i}: {e}")
    return info_dict

# استدعاء الدالة
X = get_info(sequence_list)

# إذا بغينا رسم line chart، خاصنا نأخذ بيانات صحيحة من history
# خذنا مثلا لغة واحدة صحيحة باش نجرب
sample_ticker = yf.Ticker("AAPL")  # مثال: Apple
df_history = sample_ticker.history(start='2020-1-1', end='2020-12-31')

st.line_chart(df_history['Close'])
st.line_chart(df_history['Volume'])

# إنشاء DataFrame من dictionary
df_info = pd.DataFrame.from_dict(X, orient='index')
df_info = df_info.reset_index()  # reset index
df_info = df_info.rename(columns={'index': 'Language'})  # إعادة تسمية العمود
st.subheader("The most popular programming languages info")
st.write(df_info)

# عرض bar chart باستخدام Altair
st.subheader("Display Bar Chart")
# مثال على bar chart: نقدر نستخدم مثلا عدد الحروف في الاسم كمثال توضيحي
df_info['NameLength'] = df_info['Language'].apply(len)

chart = alt.Chart(df_info).mark_bar().encode(
    x='Language',
    y='NameLength'
)
st.altair_chart(chart, use_container_width=True)


    