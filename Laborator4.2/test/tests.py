from logik.replace import replace

def test_replace():
    assert replace('meine_datei.txt','hund','gans')=='gans katze gans'
    assert replace('meine_datei.txt', 'katze', 'hund') == 'hund hund hund'