# Minecraft Mod Installation Assistant
<img src="https://cdn.discordapp.com/attachments/1284685543711440896/1295234438669664326/Minecraft-Mod-Installation-Assistant.ico?ex=670de892&is=670c9712&hm=ff7f3fe04d6bddc335b283c527d6dff833d0db32f97bd62cbb7bdce58f761336&" alt="ロゴ" title="ロゴ">
MinecraftのMod導入をアシストするツールです。


# 使い方
### クライアント向け
ソフト起動後、**modsフォルダ**とサーバー管理者より配布された**jsonファイル**を選択。  
赤文字：未導入  
緑文字：導入済み  
  
リンクをクリックすることで、ダウンロードサイトへジャンプできます。

### サーバー管理者向け
クライアント向けにmodリストを用意する必要があります。  
現在、**"json"** のみ対応しております。

#### 記述例
```json:sanmple.json  
{

	"必須MOD":[

		{

			"folder": "1.20.1",

			"file": "example1.jar",

			"link": "https://",

			"description": "example1"

		}
	]

} 
```

#### 記述方式
jsonの記述方式に従ってください。

##### 項目ごとの解説
2行目：  
"" 内はソフトでリストを表示する際の区分分けに用いられます。  
"必須MOD" や "推奨MOD" などでリストを分けたいときに使用してください。  
区分分けを行わない場合、**"MOD一覧"** としてください。  
  
4~7行目：
"folder": "フォルダ名"（modsフォルダ直下の場合は空白）  
"file": "modファイル名"  
"link": "modのダウンロードリンク"  
"description": "*補足"  

*仕様上に見くくなってしまうので "補足：example1" などにすることを推奨。


> [!TIP]
> リリースにjsonのサンプルを置いています。参考程度にどうぞ。  
