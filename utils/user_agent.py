from fake_useragent import UserAgent

def make_user_agent():
    ua = UserAgent(
    platforms=["mobile", "tablet"], 
    os=["Android","iOS"],
    fallback="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
)
    return ua.random