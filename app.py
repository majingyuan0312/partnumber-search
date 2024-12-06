import streamlit as st
import pandas as pd

# 设置页面标题
st.title("件号搜索工具")

# 初始化一个空的 DataFrame
data = None

# 添加两个按钮供用户选择文件
col1, col2 = st.columns(2)  # 将按钮放在两列中
with col1:
    if st.button("检索 data.csv"):
        file_name = "data.csv"
with col2:
    if st.button("检索 breaker.csv"):
        file_name = "breaker.csv"

# 检查是否选择了文件
if 'file_name' in locals():
    try:
        # 根据选择加载数据
        data = pd.read_csv(file_name)
        st.success(f"已加载文件：{file_name}")
    except FileNotFoundError:
        st.error(f"未找到数据文件 {file_name}，请检查文件是否存在于程序目录中。")
        st.stop()
else:
    st.warning("请先选择要检索的文件！")

# 搜索功能
if data is not None:
    keyword = st.text_input("请输入搜索关键词")
    if keyword:
        results = data[data.apply(lambda row: keyword.lower() in row.to_string().lower(), axis=1)]
        st.write(f"共找到 {len(results)} 条结果：")
        st.dataframe(results, use_container_width=True)
    else:
        st.info("技术资料仅供参考，不作为维修依据")
