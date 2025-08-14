import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# 데이터 정의
labels = ['1월', '2월', '3월', '4월', '5월', '6월', '7월', '8월', '9월', '10월', '11월', '12월']
sales = [12000000, 13500000, 11000000, 18000000, 21000000, 24000000,
         22500000, 23000000, 19500000, 25000000, 26500000, 28000000]
previous_sales = [10500000, 11200000, 12800000, 15200000, 18500000, 20100000,
                  19000000, 20500000, 18000000, 21500000, 23000000, 25000000]
growth = [14.3, 20.5, -14.1, 18.4, 13.5, 19.4, 18.4, 12.2, 8.3, 16.3, 15.2, 12.0]

df = pd.DataFrame({
    '월': labels,
    '2024년 매출': sales,
    '2023년 매출': previous_sales,
    '증감률': growth
})

# 통계 요약
avg_sales = np.mean(sales)
max_sales = np.max(sales)
min_sales = np.min(sales)
avg_growth = np.mean(growth)

max_month = labels[sales.index(max_sales)]
min_month = labels[sales.index(min_sales)]

# 페이지 설정
st.set_page_config(layout="centered", page_title="2024년 매출 대시보드")
st.title("📊 2024년 월별 매출 분석 대시보드")
st.markdown("2024년 월별 매출과 전년도 데이터를 비교하여 분석한 결과입니다.")

# 카드 스타일 요약
col1, col2, col3, col4 = st.columns(4)
col1.metric("평균 매출액", f"{avg_sales/10000:,.0f}만 원")
col2.metric("최고 매출액", f"{max_sales/10000:,.0f}만 원", f"{max_month}")
col3.metric("최저 매출액", f"{min_sales/10000:,.0f}만 원", f"{min_month}")
col4.metric("평균 증감률", f"{avg_growth:.1f}%")

st.markdown("---")

# 📈 매출 추이 그래프
fig_trend = go.Figure()
fig_trend.add_trace(go.Scatter(
    x=labels, y=sales, mode='lines+markers', name='2024년 매출',
    line=dict(color='royalblue'), fill='tozeroy'
))
fig_trend.add_trace(go.Scatter(
    x=labels, y=previous_sales, mode='lines+markers', name='2023년 매출',
    line=dict(dash='dash', color='gray')
))
fig_trend.update_layout(title="월별 매출 추이", yaxis_title="매출액 (원)", xaxis_title="월")
st.plotly_chart(fig_trend, use_container_width=True)

# 📊 증감률 막대그래프
fig_growth = go.Figure()
fig_growth.add_trace(go.Bar(
    x=labels,
    y=growth,
    marker_color=['#48bb78' if g >= 0 else '#e53e3e' for g in growth],
    name="전년 동월 대비 증감률"
))
fig_growth.update_layout(title="전년 동월 대비 증감률 (%)", yaxis_title="증감률 (%)", xaxis_title="월")
st.plotly_chart(fig_growth, use_container_width=True)
