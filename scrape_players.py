import requests
from bs4 import BeautifulSoup
import json
import time

def scrape():
    # 模拟真实浏览器请求，防止 403 封锁
    url = "https://liquipedia.net/counterstrike/Portal:Rating"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        print("开始抓取 Liquipedia 排名...")
        res = requests.get(url, headers=headers, timeout=15)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, 'html.parser')
        
        players = []
        # 定位表格中的选手行 (Liquipedia 排名页通常使用 wikitable 样式)
        rows = soup.select('table.wikitable tr')
        
        # 只取前 50 名有效数据 (跳过表头)
        for row in rows[1:51]:
            cols = row.find_all('td')
            if len(cols) < 3: continue
            
            # 尝试提取 ID
            p_id = cols[2].text.strip()
            # 尝试提取队伍
            team = cols[3].text.strip() if len(cols) > 3 else "Unknown"
            
            # 这里的 Age, Country, Role 等信息在主表不一定全
            # 我们先填充基础数据，保证游戏能跑通
            players.append({
                "name": p_id,
                "team": team,
                "cont": "Europe", # 默认填充，后续可根据国家映射
                "country": "TBD",
                "age": 22,
                "role": "Rifler",
                "majors": 5
            })
            
        # 加上时间戳记录更新
        final_data = {
            "update_time": time.strftime("%Y-%m-%d %H:%M:%S"),
            "players": players
        }
        
        # 为了配合你之前的游戏逻辑，我们还是存为纯列表格式
        # 如果你后端改了，这里也可以调整
        with open('players.json', 'w', encoding='utf-8') as f:
            json.dump(players, f, ensure_ascii=False, indent=4)
            
        print(f"抓取完成！共获得 {len(players)} 名选手。")

    except Exception as e:
        print(f"发生错误: {e}")

if __name__ == "__main__":
    scrape()
