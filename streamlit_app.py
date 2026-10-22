import streamlit as html_app  # Using Streamlit for the web app structure
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="David Julian | Personal Blog",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Styling
custom_css = """
<style>
    /* Global Styles */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        color: #2D3748;
    }

    /* Header Banner */
    .header-banner {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        border-radius: 16px;
        padding: 48px 32px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.1);
    }
    .header-title {
        font-size: 2.8rem;
        font-weight: 700;
        margin-bottom: 8px;
        letter-spacing: -0.02em;
    }
    .header-subtitle {
        font-size: 1.2rem;
        opacity: 0.9;
        font-weight: 300;
    }

    /* Navigation Bar */
    .nav-bar {
        display: flex;
        justify-content: center;
        gap: 24px;
        background-color: #F7FAFC;
        padding: 12px;
        border-radius: 12px;
        border: 1px solid #E2E8F0;
        margin-bottom: 2rem;
    }
    .nav-item {
        color: #4A5568;
        text-decoration: none;
        font-weight: 600;
        padding: 8px 16px;
        border-radius: 8px;
        transition: all 0.2s ease;
    }
    .nav-item:hover {
        background-color: #EDF2F7;
        color: #2B6CB0;
    }

    /* About Section */
    .about-card {
        background: white;
        border-radius: 16px;
        padding: 24px;
        border: 1px solid #E2E8F0;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.03);
        margin-bottom: 2rem;
    }
    .profile-img {
        border-radius: 50%;
        width: 120px;
        height: 120px;
        object-fit: cover;
        margin-bottom: 1rem;
        border: 4px solid #EBF8FF;
    }

    /* Article Cards */
    .article-card {
        background: white;
        border-radius: 12px;
        border: 1px solid #E2E8F0;
        padding: 20px;
        margin-bottom: 1.5rem;
        transition: transform 0.2s, box-shadow 0.2s;
    }
    .article-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.06);
    }
    .article-tag {
        display: inline-block;
        background-color: #EBF8FF;
        color: #2B6CB0;
        font-size: 0.8rem;
        font-weight: 600;
        padding: 4px 10px;
        border-radius: 20px;
        margin-bottom: 10px;
    }
    .article-title {
        font-size: 1.35rem;
        font-weight: 700;
        color: #1A202C;
        margin-bottom: 8px;
    }
    .article-meta {
        font-size: 0.85rem;
        color: #718096;
        margin-bottom: 12px;
    }

    /* Footer */
    .footer {
        border-top: 1px solid #E2E8F0;
        padding-top: 2rem;
        margin-top: 3rem;
        text-align: center;
        color: #718096;
    }
    .social-links {
        display: flex;
        justify-content: center;
        gap: 20px;
        margin-bottom: 1rem;
    }
    .social-link {
        color: #4A5568;
        text-decoration: none;
        font-weight: 600;
        font-size: 1rem;
        padding: 8px 16px;
        border-radius: 8px;
        background-color: #F7FAFC;
        border: 1px solid #E2E8F0;
        transition: all 0.2s;
    }
    .social-link:hover {
        background-color: #2B6CB0;
        color: white;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# 1. HEADER CO ANH BIA
st.markdown("""
<div class="header-banner">
    <div class="header-title">✨ David's Tech & Life Blog</div>
    <div class="header-subtitle">Chia sẻ hành trình lập trình, tư duy công nghệ và góc nhìn cuộc sống</div>
</div>
""", unsafe_allow_html=True)

# 2. THANH TRANG CHU (Navigation)
st.markdown("""
<div class="nav-bar">
    <a href="#about" class="nav-item">🏠 Trang Chủ</a>
    <a href="#about" class="nav-item">👤 Về Tôi</a>
    <a href="#articles" class="nav-item">📚 Bài Viết</a>
    <a href="#contact" class="nav-item">📫 Liên Hệ</a>
</div>
""", unsafe_allow_html=True)

# Main layout split into 2 columns: About + Content
col_left, col_right = st.columns([1, 2.2], gap="large")

# 3. ABOUT: DAVID JULIAN
with col_left:
    st.markdown('<div id="about"></div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="about-card">
        <center>
            <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&q=80&w=400" class="profile-img" alt="David Julian">
            <h3 style="margin-bottom: 4px; font-weight: 700;">David Julian</h3>
            <p style="color: #4A5568; font-size: 0.95rem; margin-bottom: 16px;">Software Engineer & Content Creator</p>
        </center>
        <p style="color: #4A5568; font-size: 0.9rem; line-height: 1.6;">
            Chào bạn! Tôi là <b>David Julian</b>, một kỹ sư phần mềm yêu thích viết lách. 
            Nơi đây là không gian lưu giữ kiến thức về Python, AI, phát triển ứng dụng web và kinh nghiệm thực chiến.
        </p>
        <hr style="margin: 16px 0; border: none; border-top: 1px solid #E2E8F0;">
        <p style="font-size: 0.85rem; color: #718096; margin-bottom: 6px;">📍 Ho Chi Minh City, Vietnam</p>
        <p style="font-size: 0.85rem; color: #718096; margin-bottom: 6px;">🎯 Focus: Python, Streamlit, LLMs</p>
        <p style="font-size: 0.85rem; color: #718096;">☕ Coffee Lover & Lifelong Learner</p>
    </div>
    """, unsafe_allow_html=True)

# 4. DANH SACH CAC BAI VIET
with col_right:
    st.markdown('<div id="articles"></div>', unsafe_allow_html=True)
    st.subheader("📌 Bài Viết Mới Nhất")
    
    # Category Filter Widget (Streamlit Interactive Component)
    selected_category = st.select_slider(
        "Lọc bài viết theo chủ đề:",
        options=["Tất cả", "Lập trình", "Trí tuệ nhân tạo", "Kinh nghiệm"],
        value="Tất cả"
    )

    articles = [
        {
            "title": "Xây dựng Web App với Streamlit trong 15 phút",
            "tag": "Lập trình",
            "date": "20 Tháng 10, 2026",
            "read_time": "5 phút đọc",
            "desc": "Hướng dẫn chi tiết từng bước tạo ứng dụng web tương tác hoàn chỉnh chỉ bằng ngôn ngữ Python đơn giản và mạnh mẽ."
        },
        {
            "title": "Tích hợp Generative AI vào ứng dụng thực tế",
            "tag": "Trí tuệ nhân tạo",
            "date": "15 Tháng 10, 2026",
            "read_time": "8 phút đọc",
            "desc": "Khám phá cách tận dụng các mô hình ngôn ngữ lớn (LLM) để tối ưu hóa quy trình làm việc và tạo ra các sản phẩm đột phá."
        },
        {
            "title": "Hành trình từ Zero đến Senior Developer",
            "tag": "Kinh nghiệm",
            "date": "01 Tháng 10, 2026",
            "read_time": "10 phút đọc",
            "desc": "Bài học xương máu, những sai lầm nên tránh và lộ trình tư duy dành cho những ai muốn theo đuổi sự nghiệp lập trình lâu dài."
        }
    ]

    for article in articles:
        if selected_category == "Tất cả" or article["tag"] == selected_category:
            st.markdown(f"""
            <div class="article-card">
                <span class="article-tag">{article['tag']}</span>
                <div class="article-title">{article['title']}</div>
                <div class="article-meta">📅 {article['date']} • ⏱️ {article['read_time']}</div>
                <p style="color: #4A5568; font-size: 0.95rem; line-height: 1.5; margin-bottom: 12px;">
                    {article['desc']}
                </p>
                <a href="#" style="color: #2B6CB0; font-weight: 600; text-decoration: none; font-size: 0.9rem;">Đọc tiếp &rarr;</a>
            </div>
            """, unsafe_allow_html=True)

# 5. FOOTER: SOCIAL LINK
st.markdown('<div id="contact"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="footer">
    <div class="social-links">
        <a href="https://github.com" target="_blank" class="social-link">💻 GitHub</a>
        <a href="https://linkedin.com" target="_blank" class="social-link">💼 LinkedIn</a>
        <a href="https://twitter.com" target="_blank" class="social-link">🐦 Twitter / X</a>
        <a href="mailto:david.julian@example.com" class="social-link">✉️ Email</a>
    </div>
    <p style="font-size: 0.85rem;">© 2026 David Julian. Built with Streamlit & HTML/CSS layout.</p>
</div>
""", unsafe_allow_html=True)
