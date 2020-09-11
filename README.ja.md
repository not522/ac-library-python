# ac-library-python

## 説明

ac-library-pythonは、[AtCoder Library (ACL)](https://atcoder.jp/posts/517)のPython移植版です。 詳しくは、[公式情報](#公式情報)をご参照ください.

## 進捗状況

**注: 現時点ではテストコードがないため、ご利用には十分ご注意ください。**

### 実装済み

#### グラフ

+ [Disjoint Set Union (DSU)](https://github.com/not522/ac-library-python/blob/master/atcoder/dsu.py) - [通称、蟻本](https://www.amazon.co.jp/%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0%E3%82%B3%E3%83%B3%E3%83%86%E3%82%B9%E3%83%88%E3%83%81%E3%83%A3%E3%83%AC%E3%83%B3%E3%82%B8%E3%83%96%E3%83%83%E3%82%AF-%E7%AC%AC2%E7%89%88-%EF%BD%9E%E5%95%8F%E9%A1%8C%E8%A7%A3%E6%B1%BA%E3%81%AE%E3%82%A2%E3%83%AB%E3%82%B4%E3%83%AA%E3%82%BA%E3%83%A0%E6%B4%BB%E7%94%A8%E5%8A%9B%E3%81%A8%E3%82%B3%E3%83%BC%E3%83%87%E3%82%A3%E3%83%B3%E3%82%B0%E3%83%86%E3%82%AF%E3%83%8B%E3%83%83%E3%82%AF%E3%82%92%E9%8D%9B%E3%81%88%E3%82%8B%EF%BD%9E-%E7%A7%8B%E8%91%89-%E6%8B%93%E5%93%89-ebook/dp/B00CY9256C/ref=tmm_kin_swatch_0?_encoding=UTF8&qid=&sr=)では、Union-Find木として紹介されています。

### 準備中

#### データ構造

+ fenwicktree
+ segtree
+ lazysegtree
+ string

#### 数学

+ math
+ convolution
+ modint

#### グラフ

+ maxflow
+ mincostflow
+ scc
+ twosat

## 使い方

提出用のコードに本ライブラリの必要な部分をコピー&ペーストしてご利用ください。

## よくある質問

+ 準備中。

## 利用環境、開発環境に関する情報

### 利用者、開発者向け情報

+ Python 3.8.2
+ pip

### 開発者向け情報

#### テストフレームワーク、CI

+ 準備中。

#### 任意のツール

+ 準備中。

## 本レポジトリに貢献する方法

ターミナルに以下のコマンドを貼り付けてください(注: $マークは、コマンドを実行する際には不要です)。

```md
$ mkdir your_dir_name
$ cd your_dir_name
$ git clone git@github.com:not522/ac-library-python.git
```

1. 作業を始める前に、Issueを立てるか、Pull Request(PR)の草案を用意するといいと思います。
2. Pull Request(PR)を作成し、全てのテストが通ることを確認してください。

## 連絡方法

+ 準備中。

## 公式情報

[AtCoder Library (ACL) - AtCoder](https://atcoder.jp/posts/517)

[AtCoder Library - Codeforces](https://codeforces.com/blog/entry/82400)

[AtCoder Library (ACL)のGitHubレポジトリ](https://github.com/atcoder/ac-library)

## 関連プロジェクト

[ac-library-c](https://github.com/siumai1223/ac-library-c) - C版。

[single-file-ac-library](https://github.com/TumoiYorozu/single-file-ac-library) - [公式ライブラリ](https://atcoder.jp/posts/517)を一つのファイルにまとめて利用できます。また、[公式ドキュメント](https://tumoiyorozu.github.io/single-file-ac-library/document_ja/)をブラウザで見ることもできます。

[ac-library-cs](https://github.com/key-moon/ac-library-cs) - C#版。

[ac-library-d](https://github.com/arkark/ac-library-d) - D版。

[ac-library-go](https://github.com/monkukui/ac-library-go) - Go版。

[AtCoderLibraryForJava](https://github.com/NASU41/AtCoderLibraryForJava) - Java版。

[ACL.jl](https://github.com/abap34/ACL.jl) - Julia版。

[ac-library-kt](https://github.com/da-louis/ac-library-kt) - Kotlin版。[AtCoderLibraryForJava](https://github.com/NASU41/AtCoderLibraryForJava)に基づいて作成されています。

[Nim-ACL](https://github.com/zer0-star/Nim-ACL) - Nim版。

[ACL-Python](https://github.com/Mitarushi/ACL-Python) - PyPy版。

[ac-library-ruby](https://github.com/universato/ac-library-rb) - Ruby版。

[ac-library-rs](https://github.com/rust-lang-ja/ac-library-rs) - Rust版。

## ライセンス

[CC0](https://creativecommons.org/share-your-work/public-domain/cc0)
