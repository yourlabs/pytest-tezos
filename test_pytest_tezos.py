from pytest_tezos.TestTypes import Nat


def test_tezos(tezos):
    assert tezos.addresses[0]
    assert tezos.clients[0]
    cli = tezos.clients[0]


def test_types():
    assert Nat(0).compile() == '0n'
