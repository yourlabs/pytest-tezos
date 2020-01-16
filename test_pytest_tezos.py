def test_tezos(tezos):
    assert tezos.addresses[0]
    assert tezos.clients[0]
    cli = tezos.clients[0]
    import ipdb; ipdb.set_trace()
