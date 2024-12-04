import streamlit as st
import pandas as pd

# 设置页面标题
st.title("数据搜索工具")

# 加载数据
try:
    data = pd.read_csv('data.csv')  # 确保 data.csv 文件在同一目录下
except FileNotFoundError:
    st.error("未找到数据文件 data.csv，请检查文件是否存在于程序目录中。")
    st.stop()

# 显示原始数据表
st.write("原始数据：")
st.dataframe(data)

# 搜索功能
keyword = st.text_input("请输入搜索关键词")
if keyword:
    results = data[data.apply(lambda row: keyword.lower() in row.to_string().lower(), axis=1)]
    st.write(f"共找到 {len(results)} 条结果：")
    st.dataframe(results)
else:
    st.info("请在上方输入关键词以搜索数据")
