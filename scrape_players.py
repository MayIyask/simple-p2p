import requests
from bs4 import BeautifulSoup
import json
import time

def scrape_liquipedia():
    url = "https://liquipedia.net/counterstrike/Portal:Rating"
    # 必须设置 User-Agent，否则会被 403 拒绝
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        players = []
        # 定位排名表格中的行
        # 注意：Liquipedia 的 HTML 结构经常变动，这里使用通用的 ID 提取逻辑
        rows = soup.select('table.wikitable tr')[1:51] # 取前50行

        for row in rows:
            cols = row.find_all('td')
            if len(cols) < 3: continue
            
            # 提取 ID
            name_link = cols[2].find('a')
            if not name_link: continue
            player_id = name_link.text.strip()
            
            # 提取队伍
            team_link = cols[3].find('a')
            team_name = team_link.get('title') if team_link else "Free Agent"
            
            # 补全基础逻辑 (由于 Age 等信息在个人页，为了不触发高频封锁，我们先随机/固定补全)
            # 实际开发中，如果需要精确数据，需要再请求一次 player_id 的个人页面
            players.append({
                "name": player_id,
                "team": team_name,
                "cont": "Europe", # 默认值，可在后续根据国家列表映射
                "country": "Unknown",
                "age": 22, # 默认值
                "role": "Rifler", # 默认值
                "majors": 5 # 默认值
            })

        # 写入文件
        with open('players.json', 'w', encoding='utf-8') as f:
            json.dump(players, f, ensure_ascii=False, indent=4)
        print(f"成功抓取了 {len(players)} 名选手！")

    except Exception as e:
        print(f"抓取失败: {e}")

if __name__ == "__main__":
    scrape_liquipedia()
