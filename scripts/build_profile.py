import json
import os
import re
import urllib.request
from html import unescape

USERNAME = "zoltex999"

os.makedirs("data", exist_ok=True)

url = f"https://github.com/users/{USERNAME}/contributions"

request = urllib.request.Request(
    url,
    headers={"User-Agent": "Mozilla/5.0"}
)

with urllib.request.urlopen(request) as response:
    html = response.read().decode("utf-8")

days = []

pattern = r'<td[^>]*data-date="([^"]+)"[^>]*data-level="([^"]+)"'

for date, level in re.findall(pattern, html):
    days.append({
        "date": date,
        "level": int(level)
    })

with open("data/contributions.json", "w", encoding="utf-8") as file:
    json.dump(days, file, indent=2)

colors = [
    "#161b22",
    "#0e4429",
    "#006d32",
    "#26a641",
    "#39d353"
]

svg = [
    '<svg xmlns="http://www.w3.org/2000/svg" width="860" height="150">',
    '<rect width="100%" height="100%" rx="12" fill="#0d1117"/>',
    '<text x="20" y="25" fill="#c9d1d9" font-family="monospace" font-size="14">',
    f'{USERNAME} contributions',
    '</text>'
]

for index, day in enumerate(days[-371:]):
    column = index // 7
    row = index % 7
    x = 20 + column * 15
    y = 40 + row * 15
    level = min(day["level"], 4)
    color = colors[level]

    svg.append(
        f'<rect x="{x}" y="{y}" width="11" height="11" rx="2" fill="{color}">'
        f'<title>{day["date"]}</title></rect>'
    )

svg.append(
    '<text x="20" y="140" fill="#8b949e" '
    'font-family="monospace" font-size="12">'
    'Less contributions                         More contributions'
    '</text>'
)

svg.append("</svg>")

with open("contrib-heatmap.svg", "w", encoding="utf-8") as file:
    file.write("\n".join(svg))

info_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="490" height="240">
<rect width="100%" height="100%" rx="12" fill="#0d1117"/>
<text x="25" y="40" fill="#39d353" font-family="monospace" font-size="22">
{USERNAME}
</text>
<text x="25" y="80" fill="#c9d1d9" font-family="monospace" font-size="15">
Role: Developer
</text>
<text x="25" y="115" fill="#c9d1d9" font-family="monospace" font-size="15">
Stack: Python, GitHub
</text>
<text x="25" y="150" fill="#c9d1d9" font-family="monospace" font-size="15">
Focus: Automation
</text>
<text x="25" y="185" fill="#c9d1d9" font-family="monospace" font-size="15">
Status: Building
</text>
</svg>'''

with open("info-card.svg", "w", encoding="utf-8") as file:
    file.write(info_svg)

ascii_svg = '''<svg xmlns="http://www.w3.org/2000/svg" width="370" height="240">
<rect width="100%" height="100%" rx="12" fill="#0d1117"/>
<text x="35" y="55" fill="#c9d1d9" font-family="monospace" font-size="16">
      .--------.
</text>
<text x="35" y="80" fill="#c9d1d9" font-family="monospace" font-size="16">
     /  o    o  \\
</text>
<text x="35" y="105" fill="#c9d1d9" font-family="monospace" font-size="16">
    |     ^     |
</text>
<text x="35" y="130" fill="#c9d1d9" font-family="monospace" font-size="16">
    |   -----   |
</text>
<text x="35" y="155" fill="#c9d1d9" font-family="monospace" font-size="16">
     \\________/
</text>
<text x="35" y="200" fill="#39d353" font-family="monospace" font-size="14">
     hello, world
</text>
</svg>'''

with open("avi-ascii.svg", "w", encoding="utf-8") as file:
    file.write(ascii_svg)

print("Fichiers créés avec succès.")
