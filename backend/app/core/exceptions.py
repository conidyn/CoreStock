class ProductAlreadyExistsException(Exception):
    pass


class ConflictError(Exception):
    pass


class NotFoundError(Exception):
    pass


class StockInsufficientException(Exception):
    pass
