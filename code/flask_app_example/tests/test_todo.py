import os
import json

import pytest


HERE = os.path.dirname(os.path.abspath(__file__))
CONFIG_FILE = os.path.abspath(os.path.join(HERE, os.path.pardir, 'conf/test_config.py'))
HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json",
}


@pytest.fixture(scope="function")
def client():
    from mysite import create_app
    app = create_app(config_file=CONFIG_FILE)
    with app.app_context():
        from mysite import db
        db.create_all()
    app.config['TESTING'] = True
    with app.test_client() as c:
        yield c


def test_todo(client):
    # 插入一条记录
    payload = {'message': 'test message'}
    response = client.post('/api/todo/', data=json.dumps(payload), headers=HEADERS)
    result = json.loads(response.data)
    assert result['status'] == 0, result

    # 查询所有的记录
    response = client.get('/api/todo/')
    result = json.loads(response.data)
    assert result['status'] == 0, result
    assert len(result['data']) == 1, result

    # 删除一条记录
    id = result['data'][0]['id']
    payload = {'id': id}
    response = client.delete('/api/todo/', data=json.dumps(payload), headers=HEADERS)
    result = json.loads(response.data)
    assert result['status'] == 0, result
    assert result['data']['id'] == id, result

    # 查询所有的记录
    response = client.get('/api/todo/')
    result = json.loads(response.data)
    assert result['status'] == 0, result
    assert len(result['data']) == 0, result
