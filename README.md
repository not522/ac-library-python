# ac-library-python

[日本語のREADME](README_ja.md)

## Description

ac-library-python is a Python port of [AtCoder Library (ACL)](https://atcoder.jp/posts/517). For more information, see [References](#References).

## Progress

All features are ported but may contain bugs. Some of them need to be improved speed, especially `modint` and `lazysegtree`.

We are working on adding unit tests and documents.


## Install

```
pip install git+https://github.com/not522/ac-library-python
```

## Usage

The following command outputs a single combined code which can run in online judge systems.

```
python -m atcoder [your-source-code] -o [single-combined-code]
```

## FAQ

+ Comming soon.

## Requirement

### For all users

+ Python 3.6.0+, 3.7.0+, 3.8.0+
+ pip

### For developer

#### Test framework and CI

+ [Pytest](https://docs.pytest.org/en/stable/)
+ [GitHub Actions](https://docs.github.com/en/actions/language-and-framework-guides/using-python-with-github-actions)

#### Lint

+ [flake8](https://pypi.org/project/flake8/)
+ [pep8-naming](https://pypi.org/project/pep8-naming/)
+ [mypy](https://pypi.org/project/mypy/)

## How to contribute

+ Comming soon.

## References

[AtCoder Library (ACL) - AtCoder](https://atcoder.jp/posts/517)

[AtCoder Library - Codeforces](https://codeforces.com/blog/entry/82400)

[AtCoder Library (ACL) - GitHub repository](https://github.com/atcoder/ac-library)

## Related Projects

[ac-library-c](https://github.com/siumai1223/ac-library-c) - C port.

[single-file-ac-library](https://github.com/TumoiYorozu/single-file-ac-library) - [The official library](https://atcoder.jp/posts/517) is made available as a single file. You can also view [the official documentation](https://tumoiyorozu.github.io/single-file-ac-library/document_ja/) in your favorite browser.

[ac-library-cs](https://github.com/key-moon/ac-library-cs) - C# port.

[ac-library-d](https://github.com/arkark/ac-library-d) - D port.

[ac-library-go](https://github.com/monkukui/ac-library-go) - Go port.

[AtCoderLibraryForJava](https://github.com/NASU41/AtCoderLibraryForJava) - Java port.

[ACL.jl](https://github.com/abap34/ACL.jl) - Julia port.

[ac-library-kt](https://github.com/da-louis/ac-library-kt) - Kotlin port. This project is based on [Java port](https://github.com/NASU41/AtCoderLibraryForJava).

[Nim-ACL](https://github.com/zer0-star/Nim-ACL) - Nim port.

[ACL-Python](https://github.com/Mitarushi/ACL-Python) - PyPy port.

[ac-library-ruby](https://github.com/universato/ac-library-rb) - Ruby port.

[ac-library-rs](https://github.com/rust-lang-ja/ac-library-rs) - Rust port.

## LICENSE

[CC0](https://creativecommons.org/share-your-work/public-domain/cc0)
