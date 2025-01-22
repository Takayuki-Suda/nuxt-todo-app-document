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

AsciiDoc 使用方法
1.gem install asciidoctor
2.gem install asciidoctor-diagram
3.VS Code: 拡張機能「AsciiDoc」をインストール。
4.asciidoctor -r asciidoctor-diagram xxx.adoc
(asciidoctor -r asciidoctor-diagram -D docs/html docs/adoc/a.adoc)
