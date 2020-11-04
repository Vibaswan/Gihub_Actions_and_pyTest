import pytest
import json
from abstract_open_traffic_generator.config import Config
from abstract_open_traffic_generator.control import *


@pytest.mark.ConfigTest
def test_json_config(serializer, api, tx_port, rx_port, b2b_devices):
    config = Config(ports=[tx_port, rx_port], devices=b2b_devices)
    state = State(ConfigState(config=config, state='set'))
    state = serializer.json(state)
    api.set_state(state)


@pytest.mark.skip(reason='ixnetwork_restpy.errors.NotFoundError: The requested resource /api/v1/sessions/1/'
                         'ixnetwork/topology/2/deviceGroup/1 cannot be found')
def test_dict_config(serializer, api, tx_port, rx_port, b2b_devices):
    config = Config(ports=[tx_port, rx_port], devices=b2b_devices)
    state = State(ConfigState(config=config, state='set'))
    state = serializer.json_to_dict(serializer.json(state))
    api.set_state(state)


@pytest.mark.ConfigTest
def test_config(serializer, api, tx_port, rx_port, b2b_devices):
    config = Config(ports=[tx_port, rx_port], devices=b2b_devices)
    state = State(ConfigState(config=config, state='set'))
    api.set_state(state)


if __name__ == '__main__':
    pytest.main(['-s', __file__])
