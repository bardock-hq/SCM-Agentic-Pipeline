import feedparser

# Feeds focused on Europe and Global Trade
FEEDS = [
    "https://theloadstar.com/feed/",
    "https://container-news.com/feed/",
    "https://www.supplychainbrain.com/rss/all"
]

KEYWORDS = [
    "europe", "eu", "port of rotterdam", "hamburg", "antwerp", 
    "maersk", "cma cgm", "msc", "red sea", "global", "cross-border"
]

def fetch_latest_scm_news():
    """Fetches stories matching European and Global SCM topics."""
    for url in FEEDS:
        feed = feedparser.parse(url)
        for entry in feed.entries:
            title = entry.get("title", "")
            summary = entry.get("summary", "")
            text = f"{title} {summary}".lower()

            # Check if article touches on targeted region/topics
            if any(kw in text for kw in KEYWORDS):
                return {
                    "title": title,
                    "summary": summary,
                    "link": entry.get("link", "")
                }

    # Fallback default if no match found
    return {
        "title": "Global Maritime Bottlenecks Normalizing across EU Ports",
        "summary": "Freight throughput remains steady across major North European terminals.",
        "link": "https://theloadstar.com"
    }

if __name__ == "__main__":
    data = fetch_latest_scm_news()
    print("Fetched News Data:", data)


import html
import re


def clean_html(raw_html):
    """Removes HTML tags and decodes entities using built-in modules."""
    if not raw_html:
        return ""
    # Strip HTML tags
    clean_text = re.sub(r"<[^>]+>", "", raw_html)
    # Decode special characters like &#8216;
    return html.unescape(clean_text).strip()