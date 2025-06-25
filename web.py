import io

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
from PIL import Image


def ave_grade(scores):
    return sum(scores) / len(scores)


def distri_grades(scores):
    dis_dict = {"9 - 10": 0, "8 - 9": 0, "6 - 8": 0, "0 - 6": 0}
    for score in scores:
        if score <= 10 and score > 9:
            dis_dict["9 - 10"] += 1
        elif score <= 9 and score > 8:
            dis_dict["8 - 9"] += 1
        elif score <= 8 and score > 6:
            dis_dict["6 - 8"] += 1
        else:
            dis_dict["0 - 6"] += 1
    return dis_dict


st.title("Phân tích điểm thi")
upload_file = st.file_uploader("Chọn file xlsx (có cột 'Điểm số')", type=["xlsx"])
if upload_file:
    data = pd.read_excel(upload_file)
    data = data["Điểm số"].dropna().astype(float).tolist()
    st.write(f"Số lượng học sinh: {len(data)}")
    st.write(f"Điểm số trung bình: {round(ave_grade(data), 2)}")
    st.write(f"Điểm cao nhất là: {max(data)}")
    st.write(f"Điểm thấp nhất là: {min(data)}")
    dict_data = distri_grades(data)
    values = list(dict_data.values())
    labels = list(dict_data.keys())
    fig, axis = plt.subplots(figsize=(8, 10))
    axis.pie(values, labels=labels, autopct="%1.2f%%")
    axis.axis("equal")
    axis.legend()
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=300)
    buf.seek(0)
    st.markdown("Biểu đồ")
    img = Image.open(buf)
    col1, col2, col3 = st.columns([1, 4, 1])
    with col2:
        st.image(img)
        st.markdown("Biểu đồ phân bố điểm thi")
    data = {"Tên": ["Huy", "Nam", "Lan"], "Tuổi": [25, 30, 22], "Điểm": [8.5, 7.8, 9.2]}

    df = pd.DataFrame(data)

    st.write("**Bảng tĩnh (st.table):**")
    st.table(df)

    st.write("**Bảng động (st.dataframe):**")
    st.dataframe(df)
    st.sidebar.title("Tùy chọn")
    hobby = st.sidebar.multiselect(
        "Bạn thích hoạt động nào?",
        ["Đọc sách", "Nghe nhạc", "Chơi thể thao", "Lập trình"],
    )

    st.sidebar.write("Bạn chọn:", ", ".join(hobby))

    # Layout chia 2 cột
    col1, col2 = st.columns(2)

    # Cột bên trái: Nhập thông tin
    with col1:
        st.header("Thông tin cá nhân")
        name = st.text_input("Họ và tên")
        age = st.slider("Tuổi", 0, 100, 25)
        gender = st.radio("Giới tính", ["Nam", "Nữ", "Khác"])

    # Cột bên phải: Hiển thị kết quả
    with col2:
        st.header("Kết quả")
        if name:
            st.success(f"Xin chào {name}!")
            st.write(f"Tuổi của bạn: {age}")
            st.write(f"Giới tính: {gender}")
        else:
            st.warning("Vui lòng nhập họ tên để xem kết quả.")
