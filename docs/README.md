git 操作方法
1:リモートリポジトリを作成
2:git init
3:git remote add origin URL
4:git add .
5:git commit -m "Initial commit"
6:git push -u origin main

flowchart 作成方法

1.拡張機能 PlantUML をインストール
2.task_flow.puml を作成(例)
3.jdk をインストール
4.plantuml-x.xxxx.x.jar をインストールし任意のディレクトリに保存
5.java -jar C:/tools/plantuml/plantuml-1.2024.8.jar task_flow.puml

ブランチを作成したらリモートリポジトリにプッシュする
git push -u origin <ブランチ名>
