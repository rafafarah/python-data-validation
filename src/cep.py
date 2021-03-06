import requests

class Address:
    def __init__(self, cep):
        cep = str(cep)
        if self.is_cep_valid(cep):
            self._cep = cep
        else:
            raise ValueError("Invalid CEP")

    def __str__(self):
        return self.format()

    def is_cep_valid(self, cep):
        return (8 == len(cep))

    def format(self):
        return "{}-{}".format(self._cep[:5], self._cep[5:])

    # return bairro, localidade and uf
    def access_via_cep(self):
        req = requests.get("https://viacep.com.br/ws/" + self._cep + "/json").json()
        return req['bairro'], req['localidade'], req['uf']
