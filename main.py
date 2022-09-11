import sqlalchemy
from sqlalchemy.orm import scoped_session, sessionmaker


def print_transaction_status(s1, s2):
    print("トランザクションの確認")
    print(f"[${s1}] transaction status: " + str(s1.in_transaction()))
    print(f"[${s2}] transaction status: " + str(s2.in_transaction()))
    print("")


def begin_transaction(session):
    if not session.in_transaction():
        print(f"[${session}] トランザクションを開始します\n")
        session.begin()
    else:
        print(f"[${session}] 既にトランザクションが開始されてます\n")


def main(Session):
    session1 = Session()
    session2 = Session()

    print_transaction_status(session1, session2)

    print(f"[${session1}] transaction開始")
    begin_transaction(session1)
    print_transaction_status(session1, session2)

    print(f"[${session2}] transaction開始")
    begin_transaction(session2)
    print_transaction_status(session1, session2)


if __name__ == "__main__":

    engine = sqlalchemy.create_engine("sqlite:///sample.sqlite3")
    sessions = [
        sessionmaker(bind=engine, autocommit=False, autoflush=True),
        scoped_session(sessionmaker(bind=engine, autocommit=False, autoflush=True)),
    ]

    for session in sessions:
        print("------------------------------------")
        print("main 開始")
        print("------------------------------------\n")
        main(session)
        print("------------------------------------")
        print("main 終了")
        print("------------------------------------\n")
        # print("------------------------------------")
