# session check code in SQLAlchemy

次の 2 点の挙動を確認する。

- `sessionmaker`と`scoped_session`の Session 生成の違い
- `in_transaction`の挙動

## Environment

- Python
- pipenv

## Usage

```
$ pip install -r requirements.txt
$ pipenv shell
$ pipenv sync
$ python main.py
```
