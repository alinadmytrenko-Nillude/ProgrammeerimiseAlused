class Math:       # Klass matemaatiliste abimeetodite jaoks
    @staticmethod
    def add5(x):      # Staatiline meetod – lisab arvule 5
        return x + 5    # Tagastab x + 5

    @staticmethod
    def add10(x):      # Staatiline meetod – lisab arvule 10
        return x + 10    # Tagastab x + 10

    @staticmethod
    def pr():      # Staatiline meetod – väljastab sõnumi
        print("run")    # Prindib konsooli sõna "run"
Math.pr()                # → run  (väljastab sõnumi)