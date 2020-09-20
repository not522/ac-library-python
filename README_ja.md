# ac-library-python

## 説明

ac-library-pythonは、[AtCoder Library (ACL)](https://atcoder.jp/posts/517)のPython移植版です。 詳しくは、[公式情報](#公式情報)をご参照ください.

## 進捗状況

**注: 現時点ではテストコードがないため、ご利用には十分ご注意ください。**

### 実装済み

#### データ構造

+ [Fenwick Tree](https://github.com/atcoder/ac-library/blob/master/document_ja/fenwicktree.md)
+ segtree
+ lazysegtree

#### 数学

+ convolution
+ math
+ modint

#### グラフ

+ [Disjoint Set Union (DSU)](https://github.com/atcoder/ac-library/blob/master/document_ja/dsu.md)
+ maxflow
+ mincostflow
+ scc
+ twosat

### 準備中

#### データ構造

+ string

## インストール

```
pip install git+https://github.com/not522/ac-library-python
```

## 使い方

以下のコマンドでオンラインジャッジで実行可能な結合されたソースコードが出力されます。

```
python -m atcoder [your-source-code] -o [single-combined-code]
```

## よくある質問

+ 準備中。

## 利用環境、開発環境に関する情報

### 利用者、開発者向け情報

+ Python 3.8.2
+ pip

### 開発者向け情報

#### テストフレームワーク、CI

+ [Pytest](https://docs.pytest.org/en/stable/)
+ [GitHub Actions](https://docs.github.com/en/actions/language-and-framework-guides/using-python-with-github-actions)

#### Lint

+ [flake8](https://pypi.org/project/flake8/)
+ [pep8-naming](https://pypi.org/project/pep8-naming/)

## 本レポジトリに貢献する方法

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
