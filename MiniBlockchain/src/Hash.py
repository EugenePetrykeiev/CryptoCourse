class Hash:
    @staticmethod
    def toSHA1(message_to_hash: str) -> str:
        from hashlib import sha1
        return sha1(message_to_hash.encode('utf-8')).hexdigest()
