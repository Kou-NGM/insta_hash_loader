import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import re
import time
import random
from selenium.webdriver.chrome.options import Options
import csv
import pandas as pd
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
from tkinter import ttk
from tqdm import tqdm
import matplotlib.pyplot as plt
import os
import threading
import matplotlib
import sys
from matplotlib import font_manager
import matplotlib.backends.backend_tkagg as tkagg
import matplotlib.colors as mcolors
import datetime


fonts = [f.name for f in font_manager.fontManager.ttflist]
available_fonts = ['Meiryo', 'MS Gothic', 'MS Mincho', 'Takao']

for font in available_fonts:
    if font in fonts:
        matplotlib.rcParams['font.family'] = font
        break
else:
    print("日本語を表示するためのフォントがシステムにインストールされていません。")
    print("インストール可能な一般的な日本語フォントとしては 'Meiryo', 'MS Gothic', 'MS Mincho', 'Takao' があります。")
    print("以下は、例えば 'Meiryo' フォントをWindowsにインストールする手順です：")
    print("1. [スタート] メニューを開き、[設定] を選択します。")
    print("2. [個人用設定] を選択し、その後 [フォント] を選択します。")
    print("3. [新しいフォントをインストールする] を選択し、ダウンロードしたフォントファイル (.ttf, .ttc, .otf) を指定します。")
    print("4. 指示に従ってインストールを進めます。")
    print("それぞれのOSや環境でインストール方法は異なるため、具体的な手順はWebで検索してください。")

    continue_program = input("日本語フォントが見つからない場合でもプログラムを続行しますか？ (y/n): ")
    if continue_program.lower() != 'y':
        sys.exit("プログラムを終了します。")



def human_format(num):
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    return '%.1f%s' % (num, ['', 'K', 'M', 'B'][magnitude])

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--lang=en')


# seleniumのバージョンをチェック
selenium_version = tuple(int(num) for num in selenium.__version__.split('.')[:2])

# seleniumのバージョンに応じた初期化方法を選択
if selenium_version >= (4, 0):
    webdriver_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=webdriver_service, options=options)
else:
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)



base_url = 'https://www.instagram.com/explore/tags/'

root = tk.Tk()
root.title("Instagram Hashtag Loader")
root.withdraw()

results = []
root.deiconify()
progressbar = ttk.Progressbar(root, length=200)
progressbar.pack()

word_label = tk.Label(root, text="")
word_label.pack()

percentage_label = tk.Label(root, text="")
percentage_label.pack()

posts_count_label = tk.Label(root, text="")
posts_count_label.pack()

gif_label = tk.Label(root)
gif_label.pack()
gif = tk.PhotoImage(file='gaming.gif')
gif_label.config(image=gif)
gif_index = 0

scheduled_event_id = None

def next_frame():
    global gif_index
    global scheduled_event_id
    try:
        gif.configure(format="gif -index {}".format(gif_index))
        gif_index += 1
    except tk.TclError:
        gif_index = 0
        return next_frame()
    else:
        scheduled_event_id = root.after(100, next_frame)

def start_animation():
    global scheduled_event_id
    root.after_idle(next_frame)

def stop_animation():
    global scheduled_event_id
    root.after_cancel(scheduled_event_id)

start_animation()

load_from_csv = messagebox.askyesno(title='Input method', message='Do you want to load words from a CSV file?')
if load_from_csv:
    csv_file_path = filedialog.askopenfilename()
    df = pd.read_csv(csv_file_path)
    words = df['word'].tolist()
else:
    words = simpledialog.askstring(title='Input Words', prompt='Enter words separated by comma').split(',')

messagebox.showinfo(title='Select Output Directory', message='Please select a destination directory for output files')
output_directory = filedialog.askdirectory(title='Select Output Directory')

progressbar["maximum"] = len(words)

total_posts = 0
for i, word in enumerate(words):
    url = base_url + word.strip() + '/'
    driver.get(url)
    WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located((By.TAG_NAME, 'body')))
    match = re.search(r'([\d.,]+[KMB]?)\s*posts', driver.page_source, re.IGNORECASE)

    if match:
        posts_count_str = match.group(1).replace(',', '')
        if 'K' in posts_count_str:
            posts_count = int(float(posts_count_str.replace('K', '')) * 1000)
        elif 'M' in posts_count_str:
            posts_count = int(float(posts_count_str.replace('M', '')) * 1000000)
        elif 'B' in posts_count_str:
            posts_count = int(float(posts_count_str.replace('B', '')) * 1000000000)
        else:
            posts_count = int(float(posts_count_str))
        total_posts += posts_count
        results.append([word, posts_count])
        progressbar["value"] = i + 1
        word_label["text"] = "Current word: " + word
        percentage_label["text"] = "Progress: {}%".format(round((i + 1) / len(words) * 100, 2))
        posts_count_label["text"] = "Total posts count: " + f'{total_posts:,}'
        root.update()

    else:
        results.append([word, 0])

    time.sleep(random.randint(2, 5))



stop_animation()

# WebDriverのセッションを終了する前に、少し待つ
time.sleep(2)
driver.quit()


def get_timestamp():
    now = datetime.datetime.now()
    timestamp = now.strftime('%Y%m%d_%H%M%S')
    return timestamp




df = pd.DataFrame(results, columns=['word', 'posts_count'])
# CSVファイルを書き込む際にエンコーディングをutf-8に変更
df.to_csv(os.path.join(output_directory, 'results.csv'), index=False, encoding='utf-8')
# CSVファイルを書き込む際にエンコーディングをcp932に変更，日本語に特化
# このエンコーディングは日本語以外の一部の文字をサポートしていないため，データによっては問題が発生する可能性あり
df.to_csv(os.path.join(output_directory, 'results_jp.csv'), index=False, encoding='cp932')


# Load the results from 'results.csv' into a new DataFrame
df_results = pd.read_csv(os.path.join(output_directory, 'results.csv'))

# Drop rows with missing 'posts_count' values
df_results = df_results.dropna(subset=['posts_count'])

# Convert 'posts_count' column to int
df_results['posts_count'] = df_results['posts_count'].astype(int)

# Sort the DataFrame in descending order by 'posts_count'
df_results = df_results.sort_values(by='posts_count', ascending=False)

# Write the sorted results back to a CSV file
timestamp = get_timestamp()
sorted_results_path = os.path.join(output_directory, f'sorted_results_{timestamp}.csv')
# CSVファイルを書き込む際にエンコーディングをutf-8-sigに変更
df_results.to_csv(sorted_results_path, index=False, encoding='utf-8-sig')

...

# Save the bar chart as a PNG file
chart_path = os.path.join(output_directory, f'bar_chart_{timestamp}.png')
plt.savefig(chart_path)

# Get the list of Tableau colors
tableau_colors = list(mcolors.TABLEAU_COLORS)

# Create a list of colors for the bars in the bar chart
bar_colors = [tableau_colors[i%len(tableau_colors)] for i in range(len(df_results['word']))]

# Plot a bar chart using the 'word' column as the x-axis and the 'posts_count' column as the y-axis
plt.figure(figsize=(10, 5))  # Set the figure size
bars = plt.bar(df_results['word'], df_results['posts_count'], color=bar_colors)
plt.xlabel('Word')
plt.ylabel('Posts Count')
plt.title('Number of posts count for each word')
plt.xticks(rotation=45)  # Rotate the x-axis labels for better readability

# Format y-axis
ax = plt.gca()
ax.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: human_format(x)))

# Add the actual values at the tips of the bars
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval, f'{int(yval):,}', ha='center', va='bottom')

plt.tight_layout()  # Adjust the layout to fit the labels

# Save the bar chart as a PNG file
chart_path = os.path.join(output_directory, f'bar_chart_{timestamp}.png')
plt.savefig(chart_path)







# 以下のコードは、すべての処理が終了した後にウィンドウが閉じられるようにするためのものです。
def close_window():
    root.destroy()


# Get the list of Tableau colors
tableau_colors = list(mcolors.TABLEAU_COLORS)

# Create a list of colors for the bars in the bar chart
bar_colors = [tableau_colors[i%len(tableau_colors)] for i in range(len(df_results['word']))]

# matplotlibのFigureとAxesを作成します。
fig, ax = plt.subplots(figsize=(10, 5))

bars = ax.bar(df_results['word'], df_results['posts_count'], color=bar_colors)
ax.set_xlabel('Word')
ax.set_ylabel('Posts Count')
ax.set_title('Number of posts count for each word')
plt.xticks(rotation=45)  # Rotate the x-axis labels for better readability

# Format y-axis
ax.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: human_format(x)))

# Add the actual values at the tips of the bars
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval, f'{int(yval):,}', ha='center', va='bottom')

fig.tight_layout()  # Adjust the layout to fit the labels

# Save the bar chart as a PNG file
chart_path = os.path.join(output_directory, f'bar_chart_{timestamp}.png')
fig.savefig(chart_path)

# tkinterで表示するためのキャンバスを作成し、そのキャンバスにグラフを描画します。
canvas = tkagg.FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# ウィンドウが閉じられるときに実行されるコマンドを設定します。
root.protocol("WM_DELETE_WINDOW", close_window)

# 終了メッセージを表示します。
messagebox.showinfo("終了", "作業が完了しました。画面を閉じてください。")

root.mainloop()
