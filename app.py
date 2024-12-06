import streamlit as st
import pandas as pd

# 设置页面标题
st.title("搜索工具")

# 使用 Session State 存储用户选择的文件
if "file_name" not in st.session_state:
    st.session_state.file_name = None

# 文件选择按钮
col1, col2 = st.columns(2)
with col1:
    if st.button("件号"):
        st.session_state.file_name = "data.csv"
with col2:
    if st.button("跳开关"):
        st.session_state.file_name = "breaker.csv"

# 检查是否选择了文件
if st.session_state.file_name:
    file_name = st.session_state.file_name
    try:
        # 加载数据
        data = pd.read_csv(file_name)
        st.success(f"已加载文件：{file_name}")
    except FileNotFoundError:
        st.error(f"未找到数据文件 {file_name}，请检查文件是否存在于程序目录中。")
        st.stop()
else:
    st.warning("请点击上方按钮选择要检索的文件！")
    st.stop()

# 搜索功能
keyword = st.text_input("请输入搜索关键词")
if keyword:
    # 搜索逻辑
    results = data[data.apply(lambda row: keyword.lower() in row.to_string().lower(), axis=1)]
    # 自动获取当前文件的列名
    columns_to_display = list(data.columns)  # 自动获取全部列名
    if len(columns_to_display) != 3:
        st.error("每个文件应包含三列，请检查文件内容是否正确。")
        st.stop()

    # 保留指定列
    results = results[columns_to_display]

    st.write(f"共找到 {len(results)} 条结果：")

    # 显示结果表格（隐藏索引）
    st.dataframe(results.style.hide(axis="index"), use_container_width=True)
else:
    st.info("技术资料仅供参考，不作为维修依据")
