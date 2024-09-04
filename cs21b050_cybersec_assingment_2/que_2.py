import hashlib
import hmac

def hmac_md5(key, message):
    """
    Computes HMAC using MD5 hash algorithm.
    
    :param key: The secret key (bytes)
    :param message: The message to hash (bytes)
    :return: The resulting HMAC as a hexadecimal string
    """
    return hmac.new(key, message, hashlib.md5).hexdigest()

def test_hmac_md5():
    key = b"key"
    message = b"The quick brown fox jumps over the lazy dog"
    expected_hmac = "80070713463e7749b90c2dc24911e275"

    computed_hmac = hmac_md5(key, message)

    print(f"Expected HMAC: {expected_hmac}")
    print(f"Computed HMAC: {computed_hmac}")
    
    assert computed_hmac == expected_hmac, "Test failed!"
    print("Test passed!")

test_hmac_md5()
