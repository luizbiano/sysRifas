class PerfilQuery:

    @staticmethod
    def get_all():
        return """
                SELECT Id, Descricao
            FROM Perfil;
        """

    @staticmethod
    def get_by_id():
        return """
                SELECT Id, Descricao
            FROM Perfil
            WHERE Id = :id;
        """