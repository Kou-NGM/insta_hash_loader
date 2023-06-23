# Python Instagram Hashtag scraper





## プロジェクトの概要（Project Overview）
このプロジェクトでは、Instagramのハッシュタグを使って投稿数を取得し、それらの結果をCSVファイルに保存し、さらにそれらの結果を可視化するためのバーグラフを作成します。プロジェクトのソースコードはPythonで書かれています。

This project uses Instagram hashtags to retrieve post counts, saves these results in a CSV file, and then creates a bar graph to visualize these results. The project's source code is written in Python.





## 環境設定・インストール（Setting Up Your Environment）
まず最初に、このプロジェクトを実行するためにはPythonが必要です。Pythonは公式ウェブサイトからダウンロード可能です。このプロジェクトはPython 3.7以上で動作します。

また、次にPythonのパッケージマネージャであるpipを使用して、必要なPythonライブラリをインストールする必要があります。以下のコマンドを使用してライブラリをインストールできます。

Firstly, you will need Python to run this project. You can download Python from the official website. This project works with Python 3.7 and above.

Next, you'll need to install the necessary Python libraries using pip, which is Python's package manager. You can install the libraries using the following command:

```
$ pip install selenium webdriver_manager pandas tkinter matplotlib tqdm
```




## 実行（Running the Program）
必要なソフトウェアとライブラリがインストールされていることを確認したら、以下のステップでプロジェクトをセットアップします：

1. このリポジトリをクローンまたはダウンロードします。
2. ターミナルを開き、リポジトリのディレクトリに移動します。
3. `gif_GUI_Insta_hash.py` を実行して、スクリプトを起動します。

You can run the program from the command line as follows:

```
python gif_GUI_Insta_hash.py
```

## 使用方法
ターミナルを開き、リポジトリのディレクトリに移動します。次に、`python3 gif_GUI_Insta_hash.py` を実行してスクリプトを起動します。スクリプトは自動的にウェブブラウザを開き、指定されたWebページ（この例では https://python.org）を表示します。



### Pythonのインストール

#### Windows:
1. MicrosoftストアからPythonをインストールします。ストアを開き、Pythonを検索して最新バージョンをインストールします。
2. 公式インストーラを使用してPythonをダウンロードすることもできます。ただし、これは自動更新が得られないため、Microsoftストアへのアクセスがない場合のみ推奨されます。 (参考: [source](https://python.land/installing-python/))

#### MacOS:
1. Homebrewを使用してPythonをインストールします。Homebrewをインストールした後、`brew install python`というコマンドを使用してPythonをインストールします。
2. 公式インストーラを使用してPythonをダウンロードすることもできます。ただし、これは自動更新が得られないため、コマンドラインシェルの使用に慣れていない場合のみ推奨されます。 (参考: [source](https://python.land/installing-python/))

#### Linux:
1. Linuxの配布版によっては、デフォルトのパッケージマネージャ（Yum、APTなど）を使用してPythonをインストールできます。
2. Homebrewを使用してPythonをインストールすることも可能です。これは、OSが出荷時に提供するバージョンの代わりにPythonの最新バージョンを得ることができ、システムへのルートアクセスが不要であるため、特に有用です。 (参考: [source](https://python.land/installing-python/))




## コードの説明
主な機能と流れは以下のとおりです：

seleniumライブラリを使用してInstagramのウェブサイトからデータを取得します。
tkinterライブラリを使用してユーザーからの入力を受け付け、プログレスバーで進行状況を表示します。
tqdmライブラリを使用して、コンソール上でのプログレスバーを表示します。
pandasライブラリを使用してデータを処理し、CSVファイルに結果を保存します。
matplotlibライブラリを使用して、取得したデータをバーチャートで視覚化します。
注意点として、このプログラムはシステムに日本語フォント（'Meiryo', 'MS Gothic', 'MS Mincho', 'Takao'など）がインストールされていることを前提としています。これらのフォントが見つからない場合、プログラムはユーザーにフォントのインストールを促し、その手順を示します。もしユーザーがインストールを選ばなかった場合、プログラムを終了するかどうか尋ねます。



The main features and flow are as follows:

It uses the selenium library to retrieve data from the Instagram website.
It uses the tkinter library to accept user input and display progress with a progress bar.
It uses the tqdm library to display the progress bar on the console.
It uses the pandas library to process the data and save the results in a CSV file.
It uses the matplotlib library to visualize the retrieved data with a bar chart.
Please note that this program assumes that Japanese fonts ('Meiryo', 'MS Gothic', 'MS Mincho', 'Takao', etc.) are installed on your system. If these fonts are not found, the program will prompt the user to install the font and provide instructions on how to do so. If the user chooses not to install, it will ask whether to terminate the program or not.

## コントリビューション（CONTRIBUTION）
プロジェクトへの貢献は大歓迎です
まずは、新しいブランチを作成し、変更を行ってください。変更が完了したら、プルリクエストを作成してください。プルリクエストはレビュー後にマージされます。


Contributions to the project are welcome!
First, please create a new branch and make your changes. Once you have completed your changes, please create a pull request. Pull requests will be merged after review.


## ライセンス
このプロジェクトはMITライセンスの下で公開されています。詳細は[LICENSE](LICENSE)をご覧ください。
This project is released under the MIT License. See [LICENSE](LICENSE) for more information.
