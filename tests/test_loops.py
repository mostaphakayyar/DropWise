from dropwise.loops import create_loop

def test_create_loop():
    loop = create_loop("I love chatgpt")
    assert loop["title"] == "I love chatgpt"
    assert loop["completed"] is False

