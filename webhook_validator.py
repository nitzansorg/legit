import hashlib
import hmac


def is_signature_verified(payload_body, secret_token: str, signature_header: str) -> bool:
    """
    Verify that the payload was sent from GitHub by validating SHA256.
    :param payload_body: original request body to verify (request.body())
    :param secret_token: GitHub app webhook token
    :param signature_header: header received from GitHub (x-hub-signature-256)
    :return true if the signature is verified
    """
    if not signature_header:
        return False
    hash_object = hmac.new(secret_token.encode('utf-8'), msg=payload_body, digestmod=hashlib.sha256)
    expected_signature = "sha256=" + hash_object.hexdigest()
    return hmac.compare_digest(expected_signature, signature_header)
