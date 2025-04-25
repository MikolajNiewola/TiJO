class RulesOfGame:

    """
        Metoda zwraca true, tylko gdy przejscie z polozenia source na destination w jednym ruchu jest zgodne
        z zasadami gry w szachy.
    """
    def is_correct_move(self, source, destination):
        raise NotImplementedError("Subclasses must implement this method")


class Bishop(RulesOfGame):
    def is_correct_move(self, source, destination):
        if source is None or destination is None:
            return False
        source_col, source_row = source
        dest_col, dest_row = destination

        return abs(source_col - dest_col) == abs(source_row - dest_row) and source != destination


class Knight(RulesOfGame):
    def is_correct_move(self, source, destination):
        if source is None or destination is None:
            return False
        source_col, source_row = source
        dest_col, dest_row = destination

        return ((abs(dest_row - source_row) == 2 and abs(dest_col - source_col) == 1)
                or (abs(dest_col - source_col) == 2 and abs(dest_row - source_row) == 1)
                and source != destination)


class King(RulesOfGame):
    def is_correct_move(self, source, destination):
        if source is None or destination is None:
            return False
        source_col, source_row = source
        dest_col, dest_row = destination

        return abs(dest_row - source_row) == 1 or abs(dest_col - source_col) == 1 and source != destination


class Queen(RulesOfGame):
    def is_correct_move(self, source, destination):
        if source is None or destination is None:
            return False
        source_col, source_row = source
        dest_col, dest_row = destination

        if source == destination:
            return False

        return ((abs(source_col - dest_col) == abs(source_row - dest_row))
                or (abs(source_col - dest_col) == 0)
                or (abs(source_row - dest_row) == 0))


class Rook(RulesOfGame):
    def is_correct_move(self, source, destination):
        if source is None or destination is None:
            return False
        source_col, source_row = source
        dest_col, dest_row = destination

        if source == destination:
            return False

        return abs(source_col - dest_col) == 0 or abs(source_row - dest_row) == 0


class Pawn(RulesOfGame):
    def is_correct_move(self, source, destination):
        if source is None or destination is None:
            return False
        source_col, source_row = source
        dest_col, dest_row = destination

        if source == destination:
            return False

        if source_row == 2:
            return (dest_row == source_row+2 or dest_row == source_row+1) and dest_col == source_col

        return dest_row == source_row+1 and dest_col == source_col
