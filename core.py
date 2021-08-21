import json
import hashlib
from functions import returnPrimeListUnderSomeNumber


class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []

    def proofOfWork(self, lastEven):
        nowEven = lastEven+2
        primeList = returnPrimeListUnderSomeNumber(nowEven)
        while True:
            for i in range(0, len(primeList)):
                for j in range(0, len(primeList)):
                    if self.validProof(primeList[i], primeList[j], nowEven):
                        print(primeList[i], primeList[j], nowEven)
                        return primeList[i], primeList[j], nowEven
            nowEven += 2

    def validProof(self, primeA, primeB, sum):
        return primeA+primeB == sum

    def new_block(self):
        # 새로운 블록을 생성하고 체인에 넣는다
        """
        블록체인에 들어갈 새로운 블록을 만드는 코드이다.
        index는 블록의 번호, timestamp는 블록이 만들어진 시간이다.
        transaction은 블록에 포함될 거래이다.
        proof는 논스값이고, previous_hash는 이전 블록의 해시값이다.
        """
        block = {
            'index': len(self.chain)+1,
            'timestamp': time(),
            'transaction': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        # 거래의 리스트를 초기화한다.
        self.current_transactions = []

        self.chain.append(block)
        return block

    @staticmethod
    def hash(block):
        """
        SHA-256을 이용하여 블록의 해시값을 구한다.
        해시값을 만드는데 block이 input 값으로 사용된다.
        """

        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        # 체인의 가장 마지막 블록을 반환한다
        pass

    def new_transaction(self, sender, recipient, amount):
        """
        새로운 거래는 다음으로 채굴될 블록에 포함되게 된다. 거래는 3개의 인자로 구성되어 있다. 
        sender와 recipient는 string으로 각각 수신자와 송신자의 주소이다. 
        amount는 int로 전송되는 양을 의미한다. return은 해당 거래가 속해질 블록의 숫자를 의미한다.
        """

        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        return self.last_block['index']+1


# below is just for test.
coin = Blockchain()

coin.proofOfWork(54)
