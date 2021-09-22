import base64

class PasswordEncoder():
    def __init__() -> None:
        super.__init__()
    
    def pass_encrypt(string : str):
        strbytes = string.encode("ascii")
        strb64 = base64.b64encode(strbytes)
        message = strb64.decode("ascii")

        i = len(message) - 1
        translated = ""

        while i >= 0:
            translated = translated + message[i]
            i -= 1
        
        return translated

    def pass_decrypt(string : str):

        i = len(string) - 1
        translated = ""

        while i >= 0:
            translated = translated + string[i]
            i -= 1

        strbytes = translated.encode("ascii")
        strb64 = base64.b64decode(strbytes)
        message = strb64.decode("ascii")
        
        return message
    