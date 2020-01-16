import pytest
from pytezos import pytezos

sandbox_ids = (
    'edsk3gUfUPyBSfrS9CCgmCiQsTCHGkviBDusMxDJstFtojtc1zcpsh',
    'edsk39qAm1fiMjgmPkw1EgQYkMzkJezLNewd7PLNHTkr6w9XA2zdfo',
    'edsk4ArLQgBTLWG5FJmnGnT689VKoqhXwmDPBuGx3z4cvwU9MmrPZZ',
    'edsk2uqQB9AY4FvioK2YMdfmyMrer5R8mGFyuaLLFfSRo8EoyNdht3',
    'edsk4QLrcijEffxV31gGdN2HU7UpyJjA8drFoNcmnB28n89YjPNRFm',
)


class Tezos:
    def __init__(self):
        self.addresses = []
        self.clients = []
        for i in sandbox_ids:
            key = pytezos.key.from_encoded_key(i)
            self.addresses.append(key.public_key_hash())
            self.clients.append(pytezos.using(
                key=key,
                shell='http://localhost:8732',
            ))


@pytest.fixture
def tezos():
    return Tezos()
