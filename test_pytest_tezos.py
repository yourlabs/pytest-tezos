from pytest_tezos.TestTypes import Nat


def test_tezos(tezos):
    assert tezos.addresses[0]
    assert tezos.client.balance() > 10
    for i in range(0, 4):
        assert tezos.clients[i].balance() > 10


def test_types():
    assert Nat(0).compile() == '0n'
