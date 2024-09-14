class Vehiculo:
    """
    Representa un vehículo en el sistema.

    Attributes:
        marca (str): La marca del vehículo.
        modelo (str): El modelo del vehículo.
        año (int): El año de fabricación.
        kilometraje (float): El kilometraje del vehículo.
        estadoActual (str): El estado actual del vehículo.
        tipoCombustible (str): El tipo de combustible que utiliza el vehículo.
    """

    TIPOS_COMBUSTIBLE_VALIDOS = ["Gasolina", "Diesel", "Eléctrico"]

    def __init__(self, marca, modelo, año, kilometraje, estadoActual, 
    tipoCombustible):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.kilometraje = kilometraje
        self.estadoActual = estadoActual
        self.setTipoCombustible(tipoCombustible)

    # Getters
    def getMarca(self):
        """
        Obtiene la marca del vehículo.

        Returns:
            str: La marca del vehículo.
        """
        return self.marca

    def getModelo(self):
        """
        Obtiene el modelo del vehículo.

        Returns:
            str: El modelo del vehículo.
        """
        return self.modelo

    def getAño(self):
        """
        Obtiene el año de fabricación del vehículo.

        Returns:
            int: El año de fabricación del vehículo.
        """
        return self.año

    def getKilometraje(self):
        """
        Obtiene el kilometraje del vehículo.

        Returns:
            float: El kilometraje del vehículo.
        """
        return self.kilometraje

    def getEstadoActual(self):
        """
        Obtiene el estado actual del vehículo.

        Returns:
            str: El estado actual del vehículo.
        """
        return self.estadoActual

    def getTipoCombustible(self):
        """
        Obtiene el tipo de combustible que utiliza el vehículo.

        Returns:
            str: El tipo de combustible.
        """
        return self.tipoCombustible

    # Setters
    def setMarca(self, marca):
        """
        Establece la marca del vehículo.

        Args:
            marca (str): La nueva marca del vehículo.
        """
        self.marca = marca

    def setModelo(self, modelo):
        """
        Establece el modelo del vehículo.

        Args:
            modelo (str): El nuevo modelo del vehículo.
        """
        self.modelo = modelo

    def setAño(self, año):
        """
        Establece el año de fabricación del vehículo.

        Args:
            año (int): El nuevo año de fabricación.
        """
        self.año = año

    def setKilometraje(self, kilometraje):
        """
        Establece el kilometraje del vehículo.

        Args:
            kilometraje (float): El nuevo kilometraje del vehículo.
        """
        self.kilometraje = kilometraje

    def setEstadoActual(self, estadoActual):
        """
        Establece el estado actual del vehículo.

        Args:
            estadoActual (str): El nuevo estado actual del vehículo.
        """
        self.estadoActual = estadoActual

    def setTipoCombustible(self, tipoCombustible):
        """
        Establece el tipo de combustible que utiliza el vehículo.

        Args:
            tipoCombustible (str): El nuevo tipo de combustible.
        """
        if tipoCombustible not in Vehiculo.TIPOS_COMBUSTIBLE_VALIDOS:
            raise ValueError("Tipo de combustible inválido. Debe ser uno de: {Vehiculo.TIPOS_COMBUSTIBLE_VALIDOS}")
        self.tipoCombustible = tipoCombustible